"""Source-only scale consistency for the pinned YOLO11 detector.

No target images, pseudo-labels, extra detection supervision, or architecture changes.
"""
import json
import statistics
import time
import weakref
from pathlib import Path

import torch
import torch.nn.functional as F
from ultralytics.models.yolo.detect import DetectionTrainer
from ultralytics.nn.tasks import DetectionModel
from ultralytics.utils.tal import TaskAlignedAssigner,make_anchors,dist2bbox


def ramp(epoch,batch_index,batches):
    return min(1.,max(0.,(epoch+batch_index/max(1,batches))/5.))


def geometry_selection(batch,batch_size,max_gt,focused):
    """Use augmented normalized WH directly, avoiding xyxy cancellation."""
    bidx=batch['batch_idx'].long().view(-1)
    sides=torch.round(batch['bboxes'][:,2:4].double()*640*1e6)/1e6
    visible=sides.min(-1).values>=8
    small_thin=(sides.prod(-1)<1024)|(sides.min(-1).values<16)
    chosen=visible&(small_thin if focused else torch.ones_like(visible))
    counts=torch.bincount(bidx,minlength=batch_size)
    offsets=torch.cat([counts.new_zeros(1),counts.cumsum(0)[:-1]])
    local=torch.arange(len(bidx),device=bidx.device)-offsets[bidx]
    out=torch.zeros((batch_size,max_gt),device=bidx.device,dtype=torch.bool)
    if len(bidx): out[bidx,local]=chosen
    return out,dict(total=int(len(bidx)),visible=int(visible.sum()),target=int((visible&small_thin).sum()),selected=int(chosen.sum()))


class RecordingAssigner(TaskAlignedAssigner):
    def get_pos_mask(self,*args,**kwargs):
        result=super().get_pos_mask(*args,**kwargs)
        self.raw_alignment=result[1].detach().clone()
        return result


def view_predictions(raw,batch,size,criterion):
    """Differentiable decoded outputs; detached unmodified stock TAL matching."""
    raw=criterion.parse_output(raw)
    logits=raw['scores'].permute(0,2,1).float().contiguous()
    distributions=raw['boxes'].permute(0,2,1).float().contiguous()
    anchors,strides=make_anchors(raw['feats'],criterion.stride,.5)
    anchors=anchors.float(); strides=strides.float()
    distances=distributions.view(*distributions.shape[:2],4,criterion.reg_max).softmax(-1)
    distances=distances.matmul(criterion.proj.float())
    boxes=dist2bbox(distances,anchors,xywh=False)*strides
    probabilities=logits.sigmoid()
    with torch.no_grad():
        targets=torch.cat([batch['batch_idx'].view(-1,1),batch['cls'].view(-1,1),batch['bboxes']],1).float()
        targets=criterion.preprocess(targets,len(logits),torch.full((4,),size,device=logits.device,dtype=torch.float32))
        labels,gt=targets.split((1,4),2); valid=gt.sum(-1,keepdim=True)>0
        assigner=RecordingAssigner(topk=10,num_classes=criterion.nc,alpha=.5,beta=6.,stride=criterion.stride.tolist())
        result=assigner(probabilities.detach(),boxes.detach(),anchors*strides,labels,gt,valid)
        fg,indices=result[3:]
        alignment=getattr(assigner,'raw_alignment',logits.new_zeros(len(logits),gt.shape[1],logits.shape[1]))
    return dict(probabilities=probabilities,boxes=boxes/size,fg=fg,indices=indices,alignment=alignment,labels=labels.squeeze(-1).long(),valid=valid.squeeze(-1))


def top_three(view):
    """Stable descending rank; equal scores retain ascending anchor order."""
    p=view['probabilities']; b,m,n=view['alignment'].shape
    if not m:
        return p.new_zeros((b,0,p.shape[-1])),p.new_zeros((b,0,4)),torch.zeros((b,0),dtype=torch.bool,device=p.device),torch.zeros((b,0),dtype=torch.bool,device=p.device)
    with torch.no_grad():
        assigned=(view['indices'][:,None,:]==torch.arange(m,device=p.device)[None,:,None])&view['fg'][:,None,:]
        ranked=view['alignment'].masked_fill(~assigned,-1)
        ids=torch.argsort(ranked,dim=-1,descending=True,stable=True)[...,:min(3,n)]
        weights=view['alignment'].gather(-1,ids)*assigned.gather(-1,ids)
        mass=weights.sum(-1)
        weights=weights/torch.where(mass>0,mass,torch.ones_like(mass))[...,None]
        has_positive=assigned.any(-1)
    batch_ids=torch.arange(b,device=p.device)[:,None,None]
    return ((p[batch_ids,ids]*weights[...,None]).sum(-2),
            (view['boxes'][batch_ids,ids]*weights[...,None]).sum(-2),mass>0,has_positive)


def agreement(teacher_p,teacher_b,student_p,student_b):
    p=teacher_p.detach().float().clamp(1e-6,1-1e-6)
    q=student_p.float().clamp(1e-6,1-1e-6)
    kl=(p*(p/q).log()+(1-p)*((1-p)/(1-q)).log()).mean(-1)
    loc=(teacher_b.detach().float()-student_b.float()).abs().mean(-1)
    return kl+loc,kl,loc


def consistency(student_raw,teacher_raw,batch,criterion,focused):
    with torch.autocast(device_type=batch['img'].device.type,enabled=False):
        student=view_predictions(student_raw,batch,320,criterion)
        with torch.no_grad(): teacher=view_predictions(teacher_raw,batch,640,criterion)
        selected,stats=geometry_selection(batch,len(batch['img']),student['labels'].shape[1],focused)
        sp,sb,sv,sh=top_three(student); tp,tb,tv,th=top_three(teacher)
        usable=selected&sv&tv
        losses,kl,loc=agreement(tp,tb,sp,sb)
        zero=student['probabilities'].sum()*0+student['boxes'].sum()*0
        count=usable.sum()
        loss=(losses*usable).sum()/count.clamp_min(1)+zero
        labels=student['labels']
        stats.update(usable=int(count),skip_no_positive=int((selected&(~sh|~th)).sum()),
                     skip_zero_weight=int((selected&sh&th&(~sv|~tv)).sum()),
                     selected_by_class=torch.bincount(labels[selected],minlength=4).tolist(),
                     usable_by_class=torch.bincount(labels[usable],minlength=4).tolist(),
                     kl=float(((kl*usable).sum()/count.clamp_min(1)).detach()),
                     box_l1=float(((loc*usable).sum()/count.clamp_min(1)).detach()),aux=float(loss.detach()))
        return loss,stats


class BContext:
    def __init__(self,trainer,arm):
        self.owner=weakref.ref(trainer); self.arm=arm; self.batch_index=0; self.last={}
    def compute(self,model,batch):
        trainer=self.owner(); teacher=trainer.ema.ema
        assert not teacher.training and all(not p.requires_grad for p in teacher.parameters())
        updates_before=trainer.ema.updates
        half=F.interpolate(batch['img'],size=(320,320),mode='bilinear',align_corners=False,antialias=True)
        half_raw=model(half)
        with torch.no_grad(): teacher_raw=teacher(batch['img'])
        aux,stats=consistency(half_raw,teacher_raw,batch,model.criterion,self.arm=='small_thin')
        weight=ramp(trainer.epoch,self.batch_index,len(trainer.train_loader))
        stats.update(epoch=trainer.epoch+1,batch=self.batch_index,weight=weight,teacher_updates_before=updates_before)
        self.batch_index+=1; self.last=stats
        return aux*weight


class BDetectionModel(DetectionModel):
    def loss(self,batch,preds=None):
        loss,items=super().loss(batch,preds)
        context=getattr(self,'_b_context',None)
        if self.training and context is not None:
            extra=context.compute(self,batch)*batch['img'].shape[0]
            # Stock returns a 3-component vector which the trainer sums. Add once.
            loss=loss.clone(); loss[1]=loss[1]+extra
        return loss,items


class BTrainer(DetectionTrainer):
    """Stock training orchestration, optimizer and EMA; only model loss is extended."""
    def __init__(self,*args,**kwargs):
        self.b_config=json.loads(Path('b-config.json').read_text())
        super().__init__(*args,**kwargs)
        self.add_callback('on_train_start',self.b_start)
        self.add_callback('on_train_epoch_start',self.b_epoch)
        self.add_callback('on_train_batch_start',self.b_batch_start)
        self.add_callback('on_train_batch_end',self.b_batch)
        self.add_callback('on_fit_epoch_end',self.b_epoch_end)
    def get_model(self,cfg=None,weights=None,verbose=True):
        if self.b_config['arm']=='baseline': return super().get_model(cfg,weights,verbose)
        model=self.set_model_names_for_load(BDetectionModel(cfg,nc=self.data['nc'],ch=self.data['channels'],verbose=verbose))
        if weights: model.load(weights)
        return model
    def b_start(self,t):
        self.b_rows=[]; self.b_epoch_times=[]; self.b_context=None
        if self.b_config['arm']!='baseline':
            self.b_context=BContext(self,self.b_config['arm'])
            object.__setattr__(self.model,'_b_context',self.b_context)
        self.b_ever_batch_size=self.batch_size
        groups=[dict(lr=g['lr'],initial_lr=g.get('initial_lr'),weight_decay=g.get('weight_decay'),betas=g.get('betas'),momentum=g.get('momentum'),parameters=len(g['params'])) for g in self.optimizer.param_groups]
        Path('results').mkdir(exist_ok=True)
        Path('results/optimizer-effective.json').write_text(json.dumps(dict(type=type(self.optimizer).__name__,groups=groups,warmup_bias_lr=self.args.warmup_bias_lr),indent=2))
        Path('results/resume-observed.json').write_text(json.dumps(dict(start_epoch=self.start_epoch,optimizer_state_entries=len(self.optimizer.state),teacher_updates=self.ema.updates,initial_ramp=ramp(self.start_epoch,0,len(self.train_loader)))))
    def b_epoch(self,t):
        self._oom_retries=3  # refuse stock silent per-arm auto batch reduction
        self.b_epoch_start=time.perf_counter()
        self.b_batch_times=[]
        if self.b_context: self.b_context.batch_index=0
    def b_batch_start(self,t):
        if self.b_config['smoke'] and torch.cuda.is_available(): torch.cuda.synchronize()
        self.b_batch_started=time.perf_counter()
    def b_batch(self,t):
        assert self.batch_size==self.b_ever_batch_size,'Per-arm batch size changed'
        if self.b_config['smoke'] and torch.cuda.is_available(): torch.cuda.synchronize()
        self.b_batch_times.append(time.perf_counter()-self.b_batch_started)
        if self.b_context:
            row=self.b_context.last.copy(); row['teacher_updates_after']=self.ema.updates
            assert row['teacher_updates_after']-row['teacher_updates_before'] in [0,1]
            row['supervised_items']={k:float(v) for k,v in self.loss_items.items()}
            row['total_batch_loss']=float(self.loss.detach())
            self.b_rows.append(row)
            with open('results/aux-batches.jsonl','a') as f: f.write(json.dumps(row)+'\n')
    def b_epoch_end(self,t):
        # Native final_eval emits a separate callback at epoch=epochs for best-checkpoint metrics.
        if self.epoch>=self.epochs: return
        rows=[r for r in self.b_rows if r['epoch']==self.epoch+1]
        record=dict(epoch=self.epoch+1,seconds=time.perf_counter()-self.b_epoch_start,
                    allocated=torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0,
                    reserved=torch.cuda.max_memory_reserved() if torch.cuda.is_available() else 0,
                    batches=len(rows),teacher_updates=self.ema.updates)
        if len(self.b_batch_times)>2:
            record['steady_batch_median_seconds']=statistics.median(self.b_batch_times[2:])
        if rows:
            for key in ['total','visible','target','selected','usable','skip_no_positive','skip_zero_weight']:
                record[key]=sum(r[key] for r in rows)
            for key in ['aux','kl','box_l1','weight']:
                record[key+'_mean']=sum(r[key] for r in rows)/len(rows)
            record['empty_selection_batches']=sum(r['selected']==0 for r in rows)
            for key in ['selected_by_class','usable_by_class']:
                record[key]=[sum(r[key][c] for r in rows) for c in range(4)]
        self.b_epoch_times.append(record)
        Path('results/timing.json').write_text(json.dumps(self.b_epoch_times,indent=2))
