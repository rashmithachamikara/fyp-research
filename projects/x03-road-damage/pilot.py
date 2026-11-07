"""Kaggle smoke/recovery, stock training and source-only evaluation."""
import argparse
import collections
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tarfile
import time
from pathlib import Path

import numpy as np
import torch
import yaml
from PIL import Image, ImageDraw
from ultralytics import YOLO, __version__
from metrics import xyxy,match,masks,operating,select_threshold,average_precision_binary,bootstrap,grid_cell

ROOT=Path('/kaggle/working'); OUT=ROOT/'results'; OUT.mkdir(exist_ok=True)

def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2,default=str))

def setup():
    assert __version__=='8.4.192', __version__
    assert torch.cuda.is_available(), 'GPU required for this stage'
    if not (ROOT/'prepared/images').exists():
        archive=next(Path('/kaggle/input').rglob('prepared.tar.gz'))
        with tarfile.open(archive) as f: f.extractall(ROOT,filter='data')
    env=dict(ultralytics=__version__,python=platform.python_version(),torch=torch.__version__,
             cuda=torch.version.cuda,gpu=torch.cuda.get_device_name(0),vram_bytes=torch.cuda.get_device_properties(0).total_memory)
    save('environment.json',env)
    (OUT/'pip-freeze.txt').write_text(subprocess.check_output([sys.executable,'-m','pip','freeze'],text=True))
    return json.loads((ROOT/'prepared/manifest.json').read_text())

def data_yaml(train='train',val='selection',suffix=''):
    p=ROOT/f'data{suffix}.yaml'
    p.write_text(yaml.safe_dump(dict(path=str(ROOT/'prepared'),train=str(ROOT/'prepared'/f'{train}.txt'),
                                   val=str(ROOT/'prepared'/f'{val}.txt'),names=['D00','D10','D20','D40'])))
    return str(p)

def settings(batch,epochs=50):
    return dict(data=data_yaml(),epochs=epochs,imgsz=640,batch=batch,device=0,amp=True,seed=42,
                deterministic=True,workers=2,cache=False,save=True,save_period=5,patience=100,
                project=str(ROOT/'training'),exist_ok=True,plots=True)

def smoke(records):
    ids=[r['id'] for r in records if r['split']=='train']
    # Deterministic small execution test, not the scientific pilot dataset.
    ids=sorted(ids,key=lambda s:hashlib.sha256(s.encode()).hexdigest())[:128]
    (ROOT/'prepared/smoke.txt').write_text('\n'.join(str(ROOT/'prepared/images'/f'{i}.jpg') for i in ids))
    vals=[r['id'] for r in records if r['split']=='selection'][:64]
    (ROOT/'prepared/smokeval.txt').write_text('\n'.join(str(ROOT/'prepared/images'/f'{i}.jpg') for i in vals))
    smoke_data=data_yaml('smoke','smokeval','-smoke')
    class PlannedInterruption(Exception): pass
    def interrupt(trainer):
        if trainer.epoch==0: raise PlannedInterruption('Deliberate interruption after epoch checkpoint')
    attempts=[]
    for modelname in ['yolo11s.pt','yolo11n.pt']:
        for batch in [16,8,4]:
            model=YOLO(modelname); model.add_callback('on_model_save',interrupt)
            args=settings(batch,2); args.update(data=smoke_data,name='smoke')
            try:
                model.train(**args)
                raise RuntimeError('interruption callback did not run')
            except PlannedInterruption: pass
            except torch.cuda.OutOfMemoryError:
                attempts.append(dict(model=modelname,batch=batch,status='OOM')); del model; torch.cuda.empty_cache(); continue
            checkpoint=ROOT/'training/smoke/weights/last.pt'
            state=torch.load(checkpoint,map_location='cpu',weights_only=False)
            assert state['epoch']==0 and state['optimizer'] is not None
            resume_model=YOLO(checkpoint)
            seen=[]
            resume_model.add_callback('on_train_start',lambda t:seen.append(dict(start_epoch=t.start_epoch,optimizer_state_entries=len(t.optimizer.state))))
            resume_model.train(resume=True,device=0)
            assert seen[0]['start_epoch']==1 and seen[0]['optimizer_state_entries']>0,seen
            save('smoke.json',dict(status='passed',model=modelname,batch=batch,recovery=seen,attempts=attempts))
            shutil.copy2(ROOT/'training/smoke/results.csv',OUT/'smoke-training.csv')
            return
    raise RuntimeError('Both model sizes failed at all batches')

def assignment_diagnostics(model,records):
    from ultralytics.utils.tal import TaskAlignedAssigner
    original=TaskAlignedAssigner.forward; rows=[]
    def wrapped(self,pd_scores,pd_bboxes,anc_points,gt_labels,gt_bboxes,mask_gt,**extra):
        original_gt=gt_bboxes.detach().clone()
        result=original(self,pd_scores,pd_bboxes,anc_points,gt_labels,gt_bboxes,mask_gt,**extra)
        _,_,scores,fg,idx=result
        for b in range(len(gt_labels)):
            for j in range(gt_labels.shape[1]):
                if not mask_gt[b,j].item(): continue
                sel=fg[b]&(idx[b]==j); size=(original_gt[b,j,2:]-original_gt[b,j,:2]).detach().cpu().tolist()
                rows.append(dict(cls=int(gt_labels[b,j].item()),width=size[0],height=size[1],positives=int(sel.sum()),score_mass=float(scores[b,sel].sum())))
        return result
    TaskAlignedAssigner.forward=wrapped
    net=model.model.to('cuda'); net.eval()
    try:
        from ultralytics.data import build_yolo_dataset,build_dataloader
        args=model.overrides.copy()
        from ultralytics.cfg import get_cfg
        if isinstance(net.args,dict): net.args=get_cfg(overrides=net.args)
        cfg=get_cfg(overrides=dict(imgsz=640,task='detect',mode='train',augment=False))
        train=[]
        for country in ['India','Czech']:
            train.extend(sorted([r for r in records if r['split']=='train' and r['country']==country],key=lambda r:hashlib.sha256(r['id'].encode()).hexdigest())[:128])
        txt=ROOT/'assignment.txt'; txt.write_text('\n'.join(str(ROOT/'prepared/images'/f"{r['id']}.jpg") for r in train))
        ds=build_yolo_dataset(cfg,str(txt),8,dict(names={i:c for i,c in enumerate(['D00','D10','D20','D40'])},nc=4,channels=3),mode='val',rect=False,stride=32)
        loader=build_dataloader(ds,8,0,shuffle=False)
        with torch.no_grad():
            for batch in loader:
                batch={k:v.to('cuda') if isinstance(v,torch.Tensor) else v for k,v in batch.items()}
                batch['img']=batch['img'].float()/255
                net.loss(batch)
        summaries={}
        for name,subset in [('all',rows),('small_or_thin',[r for r in rows if r['width']*r['height']<1024 or min(r['width'],r['height'])<16]),('other',[r for r in rows if r['width']*r['height']>=1024 and min(r['width'],r['height'])>=16])]:
            summaries[name]=dict(boxes=len(subset),zero_positive_fraction=sum(r['positives']==0 for r in subset)/len(subset) if subset else None,
                                  mean_positives=float(np.mean([r['positives'] for r in subset])) if subset else None,
                                  mean_score_mass=float(np.mean([r['score_mass'] for r in subset])) if subset else None)
        save('A-assignment.json',dict(records=rows,summary=summaries,images=len(train),note='Post-training frozen-best checkpoint, float32 evaluation mode, no gradients or optimizer steps; training-sample supervision diagnostic, not a log of actual training-time assignments.'))
    finally: TaskAlignedAssigner.forward=original

def train(records):
    smoke_file=next(Path('/kaggle/input').rglob('smoke.json'))
    smoke_info=json.loads(smoke_file.read_text()); assert smoke_info['status']=='passed'
    model=YOLO(smoke_info['model']); times=[]; started=time.time(); epoch_start=[0]
    model.add_callback('on_train_epoch_start',lambda t:epoch_start.__setitem__(0,time.time()))
    def end(t):
        times.append(dict(epoch=t.epoch+1,seconds=time.time()-epoch_start[0],allocated=torch.cuda.max_memory_allocated(),reserved=torch.cuda.max_memory_reserved()))
        save('timing.json',dict(epochs=times,elapsed_seconds=time.time()-started))
    model.add_callback('on_fit_epoch_end',end)
    model.train(**settings(smoke_info['batch']),name='baseline')
    save('training-complete.json',dict(status='complete',epochs=50,model=smoke_info['model'],batch=smoke_info['batch'],seconds=time.time()-started))
    for name in ['best.pt','last.pt']: shutil.copy2(ROOT/'training/baseline/weights'/name,OUT/name)
    for name in ['results.csv','args.yaml']: shutil.copy2(ROOT/'training/baseline'/name,OUT/name)
    save('checkpoint-sha256.json',{n:hashlib.sha256((OUT/n).read_bytes()).hexdigest() for n in ['best.pt','last.pt']})

def predict(model,records,size):
    data={}; paths=[str(ROOT/'prepared/images'/f"{r['id']}.jpg") for r in records]
    for result in model.predict(source=paths,imgsz=size,rect=False,conf=.001,iou=.7,max_det=300,batch=8,device=0,stream=True,verbose=False):
        boxes=result.boxes
        data[Path(result.path).stem]=torch.cat([boxes.xyxy,boxes.conf[:,None],boxes.cls[:,None]],1).cpu().tolist()
    return data

def c_diagnostics(records,preds,threshold):
    labels=[]; scores=[]; positives=0; collisions=0; positive_images=0
    for r in records:
        gt=xyxy(r['boxes'],r['width'],r['height']); pred=np.asarray(preds[r['id']],float).reshape(-1,6)
        _,_,miss=match(gt,pred,threshold); m=masks(gt,r['width'],r['height'])['small_or_thin']
        target=np.zeros((40,40),bool); weak=np.zeros((40,40))
        # Grid is on square letterboxed 640 view, not a stretched original image.
        def cell(x,y): return grid_cell(x,y,r['width'],r['height'])
        for j in miss:
            if not m[j]: continue
            y,x=cell((gt[j,1]+gt[j,3])/2,(gt[j,2]+gt[j,4])/2)
            collisions+=int(target[y,x]); target[y,x]=True
        for p in pred:
            if .05<=p[4]<threshold:
                y,x=cell((p[0]+p[2])/2,(p[1]+p[3])/2); weak[y,x]=max(weak[y,x],p[4])
        positives+=int(target.sum()); positive_images+=int(target.any()); labels.extend(target.ravel()); scores.extend(weak.ravel())
    prevalence=positives/max(1,len(labels)); ap=average_precision_binary(labels,scores)
    return dict(positive_cells=positives,positive_images=positive_images,collisions=collisions,prevalence=prevalence,
                weak_map_average_precision=ap,ap_over_prevalence=ap/prevalence if ap is not None and prevalence else None,
                weak_map_empty_by_threshold=threshold<=.05,grid='40x40 square-letterbox coordinate system')

def evaluate(records):
    checkpoint=next(p for p in Path('/kaggle/input').rglob('best.pt') if p.parent.name=='results')
    coco=list(Path('/kaggle/input').rglob('yolo11s.pt'))
    save('initial-weight-provenance.json',dict(files={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in coco},
         observed_training_download='https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo11s.pt'))
    model=YOLO(checkpoint); selected=[r for r in records if r['split']=='selection']
    # Keep diagnostics in the evaluation stage so library/API issues cannot spoil a completed training job.
    assignment_diagnostics(YOLO(checkpoint),records)
    assert all(r['country'] in ['India','Czech'] for r in selected)
    selection_preds=predict(model,selected,640)
    save('predictions-source-selection-640.json',selection_preds)
    threshold,decision=select_threshold(selected,selection_preds); save('threshold.json',dict(value=threshold,selection_ids=[r['id'] for r in selected],**decision))
    summary={}; samples=[]
    for country in ['India','Czech','United_States']:
        subset=[r for r in records if r['country']==country and r['split'] in ['source_audit','unseen']]
        preds=predict(model,subset,640); half=predict(model,subset,320)
        save(f'predictions-{country}-640.json',preds); save(f'predictions-{country}-320.json',half)
        op=operating(subset,preds,threshold); op['bootstrap95']=bootstrap(subset,op['per_image']); op['C']=c_diagnostics(subset,preds,threshold)
        positive=[r for r in subset if r['boxes']]; negative=[r for r in subset if not r['boxes']]
        op['positive_images_operating']=operating(positive,preds,threshold) if positive else None
        op['negative_images_operating']=operating(negative,preds,threshold) if negative else None
        op['scale320']=operating(subset,half,threshold)
        transitions={k:collections.Counter() for k in ['all','small_or_thin','B_eligible']}
        for r in subset:
            gt=xyxy(r['boxes'],r['width'],r['height']); mm=masks(gt,r['width'],r['height'])
            hits=[]
            for predictions in [preds,half]:
                pp=np.asarray(predictions[r['id']],float).reshape(-1,6)
                hits.append({j for _,j in match(gt,pp,threshold)[0]})
            for k,counts in transitions.items():
                for j in np.flatnonzero(mm[k]):
                    state='both' if j in hits[0] and j in hits[1] else '640_only' if j in hits[0] else '320_only' if j in hits[1] else 'neither'
                    counts[state]+=1
        op['B_scale_transitions']={k:dict(v) for k,v in transitions.items()}
        byclass={}
        for cls in range(4):
            counts=dict(gt=0,tp=0,fp=0,small_or_thin_gt=0,small_or_thin_tp=0)
            for r in subset:
                gt=xyxy(r['boxes'],r['width'],r['height']); pp=np.asarray(preds[r['id']],float).reshape(-1,6)
                pairs,fp,_=match(gt,pp,threshold)
                counts['gt']+=int((gt[:,0]==cls).sum()); counts['tp']+=sum(gt[j,0]==cls for _,j in pairs); counts['fp']+=sum(pp[i,5]==cls for i in fp)
                gm=masks(gt,r['width'],r['height'])['small_or_thin']
                counts['small_or_thin_gt']+=int(((gt[:,0]==cls)&gm).sum())
                counts['small_or_thin_tp']+=sum(gt[j,0]==cls and gm[j] for _,j in pairs)
            byclass[cls]={k:int(v) for k,v in counts.items()}
            byclass[cls].update(precision=float(counts['tp']/(counts['tp']+counts['fp'])) if counts['tp']+counts['fp'] else None,
                                recall=float(counts['tp']/counts['gt']) if counts['gt'] else None,sparse=counts['gt']<30,
                                small_or_thin_recall=float(counts['small_or_thin_tp']/counts['small_or_thin_gt']) if counts['small_or_thin_gt'] else None,
                                small_or_thin_sparse=counts['small_or_thin_gt']<30)
        op['byclass']=byclass
        (ROOT/'prepared'/f'{country}.txt').write_text('\n'.join(str(ROOT/'prepared/images'/f"{r['id']}.jpg") for r in subset))
        val=model.val(data=data_yaml(val=country,suffix='-'+country),imgsz=640,rect=False,batch=8,device=0,conf=.001,iou=.7,max_det=300,plots=False,verbose=False,project=str(ROOT/'validation'),name=country)
        op['AP']=dict(map50=float(val.box.map50),map50_95=float(val.box.map),per_class_ap=val.box.all_ap.tolist(),ap_class_index=val.box.ap_class_index.tolist())
        summary[country]=op
        # Fixed hash sample: no cherry-picking by apparent severity.
        for r in sorted(subset,key=lambda r:hashlib.sha256(r['id'].encode()).hexdigest())[:12]:
            im=Image.open(ROOT/'prepared/images'/f"{r['id']}.jpg").convert('RGB'); draw=ImageDraw.Draw(im)
            gt=xyxy(r['boxes'],r['width'],r['height']); pp=np.asarray(preds[r['id']],float).reshape(-1,6)
            _,_,miss=match(gt,pp,threshold)
            for j,b in enumerate(gt): draw.rectangle(b[1:].tolist(),outline='red' if j in miss else 'green',width=3)
            for b in pp:
                if b[4]>=threshold: draw.rectangle(b[:4].tolist(),outline='cyan',width=2)
            im.thumbnail((960,960)); im.save(OUT/f"example-{r['id']}.jpg")
    summary['source_macro_AP']={k:float(np.mean([summary[c]['AP'][k] for c in ['India','Czech']])) for k in ['map50','map50_95']}
    # Verify feature extraction without caching the dataset.
    hooks=[]; shapes={}
    for idx in [16,19]:
        hooks.append(model.model.model[idx].register_forward_hook(lambda m,i,o,idx=idx:shapes.__setitem__(str(idx),list(o.shape))))
    model.predict(source=str(ROOT/'prepared/images'/f"{selected[0]['id']}.jpg"),imgsz=640,rect=False,device=0,verbose=False)
    for h in hooks: h.remove()
    assert shapes['16'][-2:]==[80,80] and shapes['19'][-2:]==[40,40],shapes
    summary['feature_shapes']=shapes
    save('summary.json',summary)
    save('storage.json',dict(output_bytes=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())))
    print(json.dumps({c:{k:v for k,v in m.items() if k in ['AP','precision','fp_per_image','C']} for c,m in summary.items() if isinstance(m,dict)},indent=2),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('stage',choices=['smoke','train','evaluate']); args=parser.parse_args()
    records=setup(); globals()[args.stage](records)
    # Prepared input is already preserved upstream. Avoid duplicating it in every saved kernel output.
    shutil.rmtree(ROOT/'prepared')
