import copy
import unittest
import torch
from ultralytics.cfg import get_cfg
from ultralytics.nn.tasks import DetectionModel
from b_core import agreement,geometry_selection,top_three,ramp,BDetectionModel,consistency,BTrainer

torch.set_num_threads(2)

class CoreTests(unittest.TestCase):
    def test_identical_zero_and_independent_sigmoids(self):
        p=torch.tensor([[[.9,.8,.1,.3]]])  # does not sum to one
        b=torch.tensor([[[.1,.2,.3,.4]]])
        loss,_,_=agreement(p,b,p.clone(),b.clone())
        self.assertTrue(torch.allclose(loss,torch.zeros_like(loss),atol=1e-7))
    def test_teacher_detached_student_has_gradients(self):
        p=torch.tensor([[[.8,.7,.2,.1]]],requires_grad=True)
        q=torch.tensor([[[.3,.4,.5,.6]]],requires_grad=True)
        b=torch.tensor([[[.1,.2,.3,.4]]],requires_grad=True)
        s=torch.tensor([[[.2,.1,.4,.5]]],requires_grad=True)
        agreement(p,b,q,s)[0].sum().backward()
        self.assertIsNone(p.grad); self.assertIsNone(b.grad)
        self.assertGreater(float(q.grad.abs().sum()),0); self.assertGreater(float(s.grad.abs().sum()),0)
    def test_box_normalization(self):
        full=torch.tensor([[[64.,128.,256.,320.]]]); half=full/2
        p=torch.full((1,1,4),.5)
        self.assertEqual(float(agreement(p,full/640,p,half/320)[0]),0.)
    def test_geometry_boundaries_and_union(self):
        batch={'batch_idx':torch.tensor([0,0,0,0]),'bboxes':torch.tensor([[.5,.5,16/640,64/640],[.5,.5,32/640,32/640],[.5,.5,8/640,10/640],[.5,.5,7/640,10/640]])}
        selected,stats=geometry_selection(batch,1,4,True)
        self.assertEqual(selected.tolist(),[[False,False,True,False]])
        self.assertEqual(stats['target'],1)
        generic,_=geometry_selection(batch,1,4,False)
        self.assertEqual(generic.tolist(),[[True,True,True,False]])
    def test_top_three_ties_and_fewer_candidates(self):
        view=dict(probabilities=torch.tensor([[[.1],[.2],[.3],[.9]]],requires_grad=True),boxes=torch.zeros(1,4,4),
                  fg=torch.ones(1,4,dtype=torch.bool),indices=torch.zeros(1,4,dtype=torch.long),alignment=torch.ones(1,1,4))
        p,b,valid,positive=top_three(view)
        self.assertAlmostEqual(float(p.detach()),.2,places=6)
        p.sum().backward(); self.assertEqual(float(view['probabilities'].grad[0,3,0]),0.)
        view['fg'][:]=False
        p,b,valid,positive=top_three(view)
        self.assertFalse(bool(valid.any())); self.assertFalse(bool(positive.any()))
        self.assertTrue(torch.isfinite(p).all())
    def test_ramp_resume(self):
        self.assertEqual(ramp(0,0,10),0); self.assertEqual(ramp(1,0,10),.2)
        self.assertEqual(ramp(5,0,10),1)
    def test_final_validation_is_not_an_extra_training_epoch(self):
        trainer=object.__new__(BTrainer); trainer.epoch=2; trainer.epochs=2; trainer.b_epoch_times=[]
        trainer.b_epoch_end(trainer)
        self.assertEqual(trainer.b_epoch_times,[])
    def test_stock_loss_and_grad_parity_without_context(self):
        torch.manual_seed(42)
        stock=DetectionModel('yolo11s.yaml',nc=4,verbose=False)
        stock.args=get_cfg(overrides=dict(task='detect',imgsz=640))
        wrapped=copy.deepcopy(stock); wrapped.__class__=BDetectionModel
        stock.train(); wrapped.train()
        batch=dict(img=torch.rand(2,3,64,64),batch_idx=torch.tensor([0.,1.]),cls=torch.tensor([[0.],[3.]]),bboxes=torch.tensor([[.5,.5,.3,.3],[.4,.4,.2,.2]]))
        a,ai=stock.loss(batch); b,bi=wrapped.loss(batch)
        self.assertTrue(torch.equal(a,b))
        a.sum().backward(); b.sum().backward()
        for p,q in zip(stock.parameters(),wrapped.parameters()):
            if p.grad is not None: self.assertTrue(torch.equal(p.grad,q.grad))
    def test_tal_decode_consistency_gradients_and_empty_batch(self):
        model=DetectionModel('yolo11s.yaml',nc=4,verbose=False); model.args=get_cfg()
        criterion=model.init_criterion()
        def raw(size,teacher):
            shapes=[size//8,size//16,size//32]; n=sum(s*s for s in shapes)
            d=torch.full((1,4,16,n),-15.)
            if teacher: d[:,:,1,:]=15.
            else: d[:,:,:2,:]=0.
            scores=torch.full((1,4,n),-.8 if teacher else -.4); scores[:,0]=1.4 if teacher else .4
            return dict(boxes=d.reshape(1,64,n).requires_grad_(),scores=scores.requires_grad_(),feats=[torch.zeros(1,1,s,s) for s in shapes])
        batch=dict(img=torch.zeros(1,3,640,640),batch_idx=torch.tensor([0.]),cls=torch.tensor([[0.]]),bboxes=torch.tensor([[100/640,100/640,16/640,16/640]]))
        student=raw(320,False); teacher=raw(640,True)
        loss,stats=consistency(student,teacher,batch,criterion,True)
        self.assertEqual(stats['usable'],1); self.assertGreater(float(loss.detach()),0)
        loss.backward()
        self.assertIsNone(teacher['scores'].grad); self.assertIsNone(teacher['boxes'].grad)
        self.assertGreater(float(student['scores'].grad.abs().sum()),0)
        self.assertGreater(float(student['boxes'].grad.abs().sum()),0)
        batch.update(batch_idx=torch.zeros(0),cls=torch.zeros(0,1),bboxes=torch.zeros(0,4))
        loss,stats=consistency(raw(320,False),raw(640,True),batch,criterion,True)
        self.assertEqual(stats['usable'],0); self.assertEqual(float(loss.detach()),0)
        loss.backward()
    def test_auxiliary_is_added_once_not_three_times(self):
        model=BDetectionModel('yolo11s.yaml',nc=4,verbose=False); model.args=get_cfg()
        model.train()
        batch=dict(img=torch.rand(2,3,64,64),batch_idx=torch.tensor([0.,1.]),cls=torch.tensor([[0.],[3.]]),bboxes=torch.tensor([[.5,.5,.3,.3],[.4,.4,.2,.2]]))
        base,_=model.loss(batch)
        class FakeContext:
            def compute(self,m,b): return b['img'].sum()*0+2
        object.__setattr__(model,'_b_context',FakeContext())
        extended,_=model.loss(batch)
        self.assertAlmostEqual(float((extended.sum()-base.sum()).detach()),4.,places=5)

if __name__=='__main__': unittest.main()
