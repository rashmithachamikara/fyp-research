from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from threadpoolctl import threadpool_limits

started=time.perf_counter()
_,ground=annotations()
records={}
for rec in shard_records('trainval'):
    records[rec['source_id'],rec['quality']]=prepare(rec,ground)
assert set(records)=={(i,q) for s in ('train','validation') for i in PARTS[s] for q in (90,95)}

probe_report={}
for kind in ('backbone','decoder','matched'):
    datasets={}
    for split in ('train','validation'):
        x,y,groups=[],[],[]
        for i in PARTS[split]:
            pair=[records[i,q] for q in (95,90)]
            if kind=='matched':
                overlap=[r['iou'] for r in pair]
                for gi in range(len(ground[i])):
                    if all(o[:,gi].max()>=.5 for o in overlap):
                        for label,r in enumerate(pair):
                            x.append(r['queries'][r['iou'][:,gi].argmax()].float().numpy())
                            y.append(label)
                            groups.append(i)
            else:
                for label,r in enumerate(pair):
                    q=r['queries'].float()
                    value=r['backbone'] if kind=='backbone' else torch.cat([q.mean(0),q.std(0,unbiased=False)])
                    x.append(value.numpy()); y.append(label); groups.append(i)
        datasets[split]=(np.stack(x),np.array(y),np.array(groups))
    with threadpool_limits(limits=2):
        p=make_pipeline(StandardScaler(),LogisticRegression(C=1,solver='liblinear',max_iter=2000,random_state=0))
        p.fit(*datasets['train'][:2])
        x,y,groups=datasets['validation']
        correct=(p.predict(x)==y)
    ids=np.unique(groups)
    totals=np.array([correct[groups==i].sum() for i in ids])
    counts=np.array([(groups==i).sum() for i in ids])
    rng=np.random.default_rng(451)
    boot=[]
    for _ in range(20000):
        idx=rng.integers(len(ids),size=len(ids))
        boot.append(totals[idx].sum()/counts[idx].sum())
    probe_report[kind]=dict(accuracy=float(correct.mean()),ci95=np.quantile(boot,[.025,.975]).tolist(),
                            train_views=len(datasets['train'][1]),validation_views=len(y),validation_sources=len(ids))
    print('probe',kind,probe_report[kind],flush=True)
write_json('probe_report.json',probe_report)

calibration=[]
for t in np.arange(5,81,5)/100:
    totals=np.sum([matching(records[i,q]['iou'],predict(records[i,q]),t)[:3] for i in PARTS['validation'] for q in (95,90)],axis=0)
    tp,fp,fn=map(int,totals)
    calibration.append(dict(threshold=float(t),f1=2*tp/max(1,2*tp+fp+fn)))
threshold=max(calibration,key=lambda r:r['f1'])['threshold']
write_csv('formal_validation_thresholds.csv',calibration)

assignments=[]
losses=[]
hashes={}
for seed in (11,23,37):
    for name in ('A','B'):
        torch.manual_seed(seed)
        head=head_new()
        assignment={}
        rng=random.Random(seed)
        for flag in (False,True):
            ids=sorted(i for i in PARTS['train'] if bool(len(ground[i]))==flag)
            rng.shuffle(ids)
            n95=(1530 if flag else 170) if name=='A' else 850
            assignment.update({i:(95 if j<n95 else 90) for j,i in enumerate(ids)})
        assert sum(q==95 for q in assignment.values())==1700
        assignments.extend(dict(model=name,seed=seed,source_id=i,quality=q) for i,q in sorted(assignment.items()))
        optimizer=torch.optim.AdamW(head.parameters(),lr=1e-4,weight_decay=.01)
        order=random.Random(seed+771)
        for epoch in range(4):
            ids=sorted(assignment); order.shuffle(ids)
            total=0
            for begin in range(0,len(ids),6):
                batch=[records[i,assignment[i]] for i in ids[begin:begin+6]]
                queries=torch.stack([r['queries'].float() for r in batch])
                text=torch.stack([r['text'] for r in batch])
                base=torch.stack([r['logits'] for r in batch])
                labels=torch.stack([r['labels'] for r in batch])
                scores=base+torch.einsum('bqd,bd->bq',head(queries),text)
                bg=nn.functional.softplus(scores[labels==0]).mean()
                fg=scores[labels==1]
                loss=(bg+nn.functional.softplus(-fg).mean())/2 if fg.numel() else bg
                assert torch.isfinite(loss)
                optimizer.zero_grad(); loss.backward(); optimizer.step()
                total+=loss.item()
            losses.append(dict(model=name,seed=seed,epoch=epoch+1,loss=total/len(range(0,len(ids),6))))
            print(name,seed,'epoch',epoch+1,'loss',losses[-1]['loss'],flush=True)
        target=OUT/f'head-{name}-{seed}.pt'
        torch.save(head.state_dict(),target)
        hashes[target.name]=hashlib.sha256(target.read_bytes()).hexdigest()
write_csv('assignments.csv',assignments)
write_csv('training_losses.csv',losses)
write_json('frozen_training.json',dict(version=1,manifest_sha256=DIGEST,threshold=threshold,heads=hashes,
           evaluation_code_sha256=EVAL_HASH,total_seconds=time.perf_counter()-started))
