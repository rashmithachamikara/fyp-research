"""Kaggle stages for B, with an explicit benchmark/budget gate."""
import argparse
import copy
import gc
import gzip
import hashlib
import json
import os
import shutil
import statistics
import subprocess
import sys
import tarfile
import time
from pathlib import Path

import numpy as np
import torch
from ultralytics import YOLO,__version__
from ultralytics.nn.tasks import DetectionModel
from b_core import BTrainer,BDetectionModel,ramp
import pilot
from metrics import operating,select_threshold,masks,xyxy,match

ROOT=Path('/kaggle/working'); OUT=ROOT/'results'; OUT.mkdir(exist_ok=True)
CFG=json.loads(Path('experiment.json').read_text()); ARMS=CFG['arms']

def save(name,data): (OUT/name).write_text(json.dumps(data,indent=2,default=str))
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def find(name):
    files=list(Path('/kaggle/input').rglob(name))
    if not files: raise FileNotFoundError(name)
    if len(files)>1:
        assert len({sha(p) for p in files})==1,('Conflicting inputs',name)
    return files[0]

def setup():
    assert __version__==CFG['ultralytics'] and torch.cuda.is_available()
    if not (ROOT/'prepared/images').exists():
        with tarfile.open(find('prepared.tar.gz')) as f: f.extractall(ROOT,filter='data')
    manifest=ROOT/'prepared/manifest.json'; assert sha(manifest)==CFG['manifest_sha256']
    rows=json.loads(manifest.read_text())
    assert sum(r['split']=='train' for r in rows)==8264
    assert all(r['country']!='Japan' for r in rows)
    save('environment.json',dict(ultralytics=__version__,torch=torch.__version__,gpu=torch.cuda.get_device_name(0),vram_bytes=torch.cuda.get_device_properties(0).total_memory))
    (OUT/'pip-freeze.txt').write_text(subprocess.check_output([sys.executable,'-m','pip','freeze'],text=True))
    return rows

def coco():
    source=find('yolo11s.pt'); assert sha(source)==CFG['coco_sha256']
    target=ROOT/'yolo11s.pt'; shutil.copy2(source,target)
    return str(target)

def subset(rows):
    train=[r for r in rows if r['split']=='train']
    def key(r): return hashlib.sha256(r['id'].encode()).hexdigest()
    target=[]
    for r in train:
        mm=masks(xyxy(r['boxes'],r['width'],r['height']),r['width'],r['height'])
        if mm['small_or_thin'].any(): target.append(r)
    selected={r['id']:r for r in sorted(target,key=key)[:128]}
    for r in sorted(train,key=lambda r:(-len(r['boxes']),key(r)))[:64]: selected[r['id']]=r
    for r in sorted(train,key=key):
        if len(selected)>=256: break
        selected[r['id']]=r
    ids=sorted(selected)
    val=sorted([r for r in rows if r['split']=='selection'],key=key)[:64]
    (ROOT/'prepared/b-smoke.txt').write_text('\n'.join(str(ROOT/'prepared/images'/f'{i}.jpg') for i in ids))
    (ROOT/'prepared/b-smoke-val.txt').write_text('\n'.join(str(ROOT/'prepared/images'/f"{r['id']}.jpg") for r in val))
    save('smoke-subset.json',dict(train_ids=ids,selection_ids=[r['id'] for r in val]))
    return pilot.data_yaml('b-smoke','b-smoke-val','-b-smoke')

def configuration(arm,batch,smoke=False):
    d=pilot.settings(batch,2 if smoke else 50)
    d.update(project=str(ROOT/'training'),name=arm,close_mosaic=0 if smoke else 10,
             model=coco(),verbose=False)
    if smoke: d['data']=str(ROOT/'data-b-smoke.yaml')
    Path('b-config.json').write_text(json.dumps(dict(arm=arm,smoke=smoke,experiment=CFG)))
    return d

def export_checkpoint(native,target):
    """EMA weights become a normal stock DetectionModel; training-only subclass removed."""
    source=YOLO(native).model.to('cuda').float().eval()
    plain=copy.deepcopy(source); plain.__class__=DetectionModel; plain.criterion=None
    if hasattr(plain,'_b_context'): delattr(plain,'_b_context')
    x=torch.zeros(1,3,640,640,device='cuda')
    with torch.no_grad(): a=source(x)[0]; b=plain(x)[0]
    assert torch.allclose(a,b,atol=1e-6,rtol=1e-6),'Export changed predictions'
    ckpt=torch.load(native,map_location='cpu',weights_only=False)
    checkpoint=dict(model=plain.cpu().half(),ema=None,optimizer=None,epoch=-1,train_args=ckpt['train_args'],version=__version__,license='AGPL-3.0')
    torch.save(checkpoint,target)
    restored=YOLO(target).model.to('cuda').float().eval()
    with torch.no_grad(): c=restored(x)[0]
    assert torch.allclose(a,c,atol=1e-6,rtol=1e-6),'Export roundtrip changed predictions'
    del source,plain,restored; gc.collect(); torch.cuda.empty_cache()
    return sha(target)

class PlannedStop(Exception): pass

def run_smoke_arm(arm,batch):
    torch.cuda.reset_peak_memory_stats()
    args=configuration(arm,batch,True)
    model=YOLO(args.pop('model'))
    def interrupt(trainer):
        if trainer.epoch==0:
            # on_model_save precedes on_fit_epoch_end; preserve first-epoch telemetry before stopping.
            trainer.b_epoch_end(trainer)
            raise PlannedStop('Intentional optimizer/EMA recovery test')
    model.add_callback('on_model_save',interrupt)
    before=time.perf_counter()
    try: model.train(trainer=BTrainer,**args)
    except PlannedStop: pass
    else: raise AssertionError('Intentional stop did not fire')
    checkpoint=ROOT/'training'/arm/'weights/last.pt'
    state=torch.load(checkpoint,map_location='cpu',weights_only=False)
    assert state['epoch']==0 and state['optimizer'] is not None and state['updates']>0
    first=json.loads((OUT/'timing.json').read_text())
    del model; gc.collect(); torch.cuda.empty_cache()
    model=YOLO(checkpoint); model.train(trainer=BTrainer,resume=True,device=0)
    observed=json.loads((OUT/'resume-observed.json').read_text())
    assert observed['start_epoch']==1 and observed['optimizer_state_entries']>0
    assert observed['teacher_updates']==state['updates'] and observed['initial_ramp']==.2
    timings=first+json.loads((OUT/'timing.json').read_text())
    unique={}
    for t in timings: unique.setdefault(t['epoch'],t)
    assert set(unique)=={1,2}
    digest=export_checkpoint(ROOT/'training'/arm/'weights/best.pt',OUT/f'{arm}-smoke-export.pt')
    result=dict(arm=arm,batch=batch,seconds=time.perf_counter()-before,timing=list(unique.values()),resume=observed,export_sha256=digest)
    if arm!='baseline':
        result['usable']=sum(t.get('usable',0) for t in unique.values())
        result['selected']=sum(t.get('selected',0) for t in unique.values())
        assert result['usable']>0,('No usable consistency signal',arm,result)
    save(f'smoke-{arm}.json',result)
    del model,state; gc.collect(); torch.cuda.empty_cache()
    return result

def smoke(rows):
    subprocess.run([sys.executable,'-m','unittest','test_b_core','-v'],check=True)
    subset(rows); attempts=[]
    for batch in CFG['batch_candidates']:
        results=[]
        try:
            for arm in ARMS:
                # Remove prior arm's temporary telemetry; keep dedicated smoke record.
                for name in ['aux-batches.jsonl','timing.json']:
                    (OUT/name).unlink(missing_ok=True)
                results.append(run_smoke_arm(arm,batch))
        except RuntimeError as e:
            if not any(s in str(e).lower() for s in ['out of memory','cuda backend memory','cublas_status_alloc_failed']): raise
            attempts.append(dict(batch=batch,error=str(e)))
            gc.collect(); torch.cuda.empty_cache(); continue
        base=results[0]['timing'][-1]['steady_batch_median_seconds']
        ratios={r['arm']:r['timing'][-1]['steady_batch_median_seconds']/base for r in results}
        measured=sum(r['seconds'] for r in results)/3600
        projected=1.2*(1.52815234*sum(ratios.values()))+measured+1.0
        gate=dict(status='passed' if projected<=12 else 'budget_exceeded',batch=batch,ratios=ratios,
                  projected_gpu_hours=projected,budget=12,attempts=attempts,arms=results,
                  benchmark_note='Median synchronized batch times after first2 batches of resumed smoke epoch; conservative20% contingency plus1h selection/evaluation. Baseline extrapolation1.528h. Verify full-run speed.')
        save('budget-gate.json',gate); print(json.dumps(gate,indent=2),flush=True)
        if projected>12: raise RuntimeError('Full comparison exceeds authorised12h estimate; revise budget before launching')
        return
    raise RuntimeError('Consistency cannot fit at either permitted common batch')

def train(rows,arm):
    gate=json.loads(find('budget-gate.json').read_text()); assert gate['status']=='passed'
    batch=gate['batch']; args=configuration(arm,batch)
    model=YOLO(args.pop('model')); started=time.perf_counter()
    model.train(trainer=BTrainer,**args)
    assert model.trainer.batch_size==batch
    native=ROOT/'training'/arm/'weights/best.pt'
    digest=export_checkpoint(native,OUT/f'{arm}-best.pt')
    shutil.copy2(ROOT/'training'/arm/'results.csv',OUT/f'{arm}-history.csv')
    shutil.copy2(ROOT/'training'/arm/'args.yaml',OUT/f'{arm}-args.yaml')
    # Preserve optimizer-bearing recovery checkpoints on Kaggle; exported best is for inference.
    if (OUT/'aux-batches.jsonl').exists():
        with open(OUT/'aux-batches.jsonl','rb') as src,gzip.open(OUT/'aux-batches.jsonl.gz','wb',compresslevel=3) as dst: shutil.copyfileobj(src,dst)
        (OUT/'aux-batches.jsonl').unlink()
    record=dict(status='complete',arm=arm,epochs=50,batch=batch,seed=42,seconds=time.perf_counter()-started,
                best_sha256=digest,coco_sha256=CFG['coco_sha256'],manifest_sha256=CFG['manifest_sha256'],experiment=CFG)
    save(f'{arm}-record.json',record)

def select(rows):
    selection=[r for r in rows if r['split']=='selection']; assert len(selection)==1034
    frozen={}
    for arm in ARMS:
        record=json.loads(find(f'{arm}-record.json').read_text()); assert record['status']=='complete'
        checkpoint=find(f'{arm}-best.pt'); assert sha(checkpoint)==record['best_sha256']
        model=YOLO(checkpoint)
        # Compare the exported detector to the native selected EMA on actual source images.
        # Native weights remain upstream for recovery; no audit/US images enter this check.
        from PIL import Image
        from ultralytics.data.augment import LetterBox
        candidates=[p for p in Path('/kaggle/input').rglob('best.pt') if p.parent.parent.name==arm]
        assert len(candidates)==1,('Missing/ambiguous native checkpoint',arm,candidates)
        native=YOLO(candidates[0]).model.to('cuda').float().eval()
        exported=model.model.to('cuda').float().eval(); parity=[]
        for r in sorted(selection,key=lambda r:r['id'])[:3]:
            pixels=np.asarray(Image.open(ROOT/'prepared/images'/f"{r['id']}.jpg").convert('RGB'))
            pixels=LetterBox((640,640),auto=False)(image=pixels)
            x=torch.from_numpy(np.ascontiguousarray(pixels.transpose(2,0,1))).to('cuda').float()[None]/255
            with torch.no_grad(): a=native(x)[0]; b=exported(x)[0]
            assert torch.allclose(a,b,atol=1e-6,rtol=1e-6),('Source-image export mismatch',arm,r['id'])
            parity.append(dict(id=r['id'],max_absolute_difference=float((a-b).abs().max())))
        save(f'export-parity-{arm}.json',parity)
        del native; gc.collect(); torch.cuda.empty_cache()
        predictions=pilot.predict(model,selection,640)
        threshold,decision=select_threshold(selection,predictions)
        frozen[arm]=dict(threshold=threshold,decision=decision,checkpoint_sha256=sha(checkpoint),record=record)
        pilot.save(f'predictions-selection-{arm}.json',predictions)
        del model; gc.collect(); torch.cuda.empty_cache()
    save('frozen-models.json',dict(arms=frozen,selection_ids=[r['id'] for r in selection],manifest_sha256=CFG['manifest_sha256']))

def evaluate(rows):
    frozen=json.loads(find('frozen-models.json').read_text()); assert set(frozen['arms'])==set(ARMS)
    assert set(frozen['selection_ids'])=={r['id'] for r in rows if r['split']=='selection'}
    summary={}; base_threshold=frozen['arms']['baseline']['threshold']
    for arm in ARMS:
        spec=frozen['arms'][arm]; checkpoint=find(f'{arm}-best.pt'); assert sha(checkpoint)==spec['checkpoint_sha256']
        model=YOLO(checkpoint); summary[arm]={}
        for country in ['India','Czech','United_States']:
            subset=[r for r in rows if r['country']==country and r['split'] in ['source_audit','unseen']]
            pred=pilot.predict(model,subset,640); pilot.save(f'predictions-{arm}-{country}.json',pred)
            op=operating(subset,pred,spec['threshold']); op['common_threshold']=operating(subset,pred,base_threshold)
            op['byclass']={}
            for cls in range(4):
                tp=fp=gt_count=target_tp=target_count=0
                for r in subset:
                    gt=xyxy(r['boxes'],r['width'],r['height']); pp=np.asarray(pred[r['id']],float).reshape(-1,6)
                    pairs,false,_=match(gt,pp,spec['threshold']); target=masks(gt,r['width'],r['height'])['small_or_thin']
                    gt_count+=int((gt[:,0]==cls).sum()); tp+=sum(gt[j,0]==cls for _,j in pairs); fp+=sum(pp[i,5]==cls for i in false)
                    target_count+=int(((gt[:,0]==cls)&target).sum()); target_tp+=sum(gt[j,0]==cls and target[j] for _,j in pairs)
                op['byclass'][cls]=dict(gt=int(gt_count),tp=int(tp),fp=int(fp),target_gt=int(target_count),target_tp=int(target_tp))
            # Score all labels with exactly the previous baseline's evaluator configuration.
            (ROOT/'prepared'/f'{country}.txt').write_text('\n'.join(str(ROOT/'prepared/images'/f"{r['id']}.jpg") for r in subset))
            val=model.val(data=pilot.data_yaml(val=country,suffix='-'+country),imgsz=640,rect=False,batch=8,device=0,conf=.001,iou=.7,max_det=300,plots=False,verbose=False,project=str(ROOT/'validation'),name=f'{arm}-{country}')
            op['AP']=dict(map50=float(val.box.map50),map50_95=float(val.box.map),per_class=val.box.all_ap.tolist(),class_index=val.box.ap_class_index.tolist())
            # Hash-selected examples, aligned across arms and labelled by image ID.
            from PIL import Image,ImageDraw
            for r in sorted(subset,key=lambda r:hashlib.sha256(r['id'].encode()).hexdigest())[:6]:
                im=Image.open(ROOT/'prepared/images'/f"{r['id']}.jpg").convert('RGB'); draw=ImageDraw.Draw(im)
                gt=xyxy(r['boxes'],r['width'],r['height']); pp=np.asarray(pred[r['id']],float).reshape(-1,6)
                _,_,miss=match(gt,pp,spec['threshold'])
                for j,b in enumerate(gt): draw.rectangle(b[1:].tolist(),outline='red' if j in miss else 'green',width=3)
                for b in pp:
                    if b[4]>=spec['threshold']: draw.rectangle(b[:4].tolist(),outline='cyan',width=2)
                im.thumbnail((960,960)); im.save(OUT/f'example-{arm}-{r["id"]}.jpg')
            summary[arm][country]=op; save('b-summary.json',summary)
        del model; gc.collect(); torch.cuda.empty_cache()
    save('evaluation-complete.json',dict(status='complete',frozen=frozen,experiment=CFG))

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('stage',choices=['smoke','train','select','evaluate']); parser.add_argument('--arm',choices=ARMS)
    args=parser.parse_args(); stage_started=time.perf_counter(); rows=setup()
    try:
        if args.stage=='train': train(rows,args.arm)
        else: globals()[args.stage](rows)
    finally:
        save('stage-resources.json',dict(stage=args.stage,arm=args.arm,seconds_including_preparation=time.perf_counter()-stage_started,
             allocated=torch.cuda.max_memory_allocated(),reserved=torch.cuda.max_memory_reserved(),
             working_bytes_before_cleanup=sum(p.stat().st_size for p in ROOT.rglob('*') if p.is_file())))
        shutil.rmtree(ROOT/'prepared',ignore_errors=True)
