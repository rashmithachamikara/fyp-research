import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

started=time.perf_counter()
lock=json.loads(locate('frozen_training.json').read_text())
assert lock['manifest_sha256']==DIGEST and lock['evaluation_code_sha256']==EVAL_HASH
threshold=lock['threshold']
heads={'untouched':None}
for name,digest in lock['heads'].items():
    p=locate(name)
    assert hashlib.sha256(p.read_bytes()).hexdigest()==digest
    h=head_new(); h.load_state_dict(torch.load(p,weights_only=True)); h.eval()
    heads[name.removesuffix('.pt').removeprefix('head-')]=h
_,ground=annotations()
rows=[]; error_rows=[]; observed=set()
for rec in shard_records('test'):
    i,q=rec['source_id'],rec['quality']
    assert (i,q) not in observed and i in PARTS['test']
    observed.add((i,q))
    rec=prepare(rec,ground)
    condition='original' if q==0 else ('matched' if q==(95 if len(ground[i]) else 90) else 'reversed')
    for name,h in heads.items():
        scores=predict(rec,h)
        tp,fp,fn,missed=matching(rec['iou'],scores,threshold)
        rows.append(dict(model=name,source_id=i,condition=condition,bicycles=len(ground[i]),tp=tp,fp=fp,fn=fn))
        for gi in range(len(ground[i])):
            covered=rec['iou'][:,gi]>=.5
            survives=covered & (scores>=threshold)
            error_rows.append(dict(model=name,source_id=i,annotation_index=gi,condition=condition,
                                   missed=int(missed[gi]),coverage=int(covered.any()),survives=int(survives.any())))
assert observed=={(i,q) for i in PARTS['test'] for q in (95,90,0)}
write_csv('test_per_source.csv',rows)
write_csv('test_per_instance.csv',error_rows)
lookup={(r['model'],r['source_id'],r['condition']):r for r in rows}
positive=[i for i in PARTS['test'] if len(ground[i])]
negative=[i for i in PARTS['test'] if not len(ground[i])]
gt=np.array([len(ground[i]) for i in positive])
miss={}
fa={}
for name in heads:
    for c in ('matched','reversed','original'):
        miss[name,c]=np.array([lookup[name,i,c]['fn'] for i in positive])
        fa[name,c]=np.array([lookup[name,i,c]['fp'] for i in negative])
differences=np.stack([miss[f'A-{s}','reversed']-miss[f'A-{s}','matched']-miss[f'B-{s}','reversed']+miss[f'B-{s}','matched'] for s in (11,23,37)])
seed_delta=100*differences.sum(1)/gt.sum()
rng=np.random.default_rng(5182027)
bootstrap=[]
metrics={}
for group,names in [('untouched',['untouched']),('A',[f'A-{s}' for s in (11,23,37)]),('B',[f'B-{s}' for s in (11,23,37)])]:
    for c in ('matched','reversed','original'):
        metrics[group,c]=dict(miss=np.mean([miss[n,c] for n in names],axis=0),fa=np.mean([fa[n,c] for n in names],axis=0),boot_miss=[],boot_fa=[])
for _ in range(20000):
    ip=rng.integers(len(positive),size=len(positive)); ine=rng.integers(len(negative),size=len(negative))
    denom=gt[ip].sum()
    bootstrap.append(100*differences[:,ip].sum(1).mean()/denom)
    for values in metrics.values():
        values['boot_miss'].append(100*values['miss'][ip].sum()/denom)
        values['boot_fa'].append(values['fa'][ine].mean())
low,high=np.quantile(bootstrap,[.025,.975])
decision='Proceed to mitigation' if low>=3 and (seed_delta>0).all() else ('Hold mitigation project' if high<3 else 'Inconclusive')
summary=[]
for (name,c),v in metrics.items():
    summary.append(dict(model=name,condition=c,miss_rate_percent=100*v['miss'].sum()/gt.sum(),
                        miss_ci95=np.quantile(v['boot_miss'],[.025,.975]).tolist(),
                        false_alarms_per_negative=float(v['fa'].mean()),fa_ci95=np.quantile(v['boot_fa'],[.025,.975]).tolist()))
write_json('absolute_metrics.json',summary)
instance={(r['model'],r['source_id'],r['annotation_index'],r['condition']):r for r in error_rows}
types=defaultdict(int)
for r in error_rows:
    if r['condition']=='reversed' and r['missed'] and not instance[r['model'],r['source_id'],r['annotation_index'],'matched']['missed']:
        kind='no candidate coverage' if not r['coverage'] else ('score below threshold' if not r['survives'] else 'candidate assigned to another bicycle')
        types[r['model'],kind]+=1
errors=[dict(model=n,error_type=t,count=types[n,t]) for n in heads for t in ('no candidate coverage','score below threshold','candidate assigned to another bicycle')]
write_csv('error_types.csv',errors)
report=dict(decision=decision,mean_delta_pp=float(seed_delta.mean()),delta_ci95=[float(low),float(high)],
            delta_pp_by_seed=dict(zip(('11','23','37'),seed_delta.tolist())),threshold=threshold,
            test_sources=2000,test_bicycle_instances=int(gt.sum()),manifest_sha256=DIGEST,evaluation_seconds=time.perf_counter()-started)
write_json('formal_result.json',report)
fig,axes=plt.subplots(1,3,figsize=(12,4),layout='constrained')
colors={'matched':'#246b9e','reversed':'#d27032','original':'#777777'}
for j,(field,interval,ylabel) in enumerate([('miss_rate_percent','miss_ci95','Missed bicycles (%)'),('false_alarms_per_negative','fa_ci95','False alarms per negative image')]):
    for k,c in enumerate(('matched','reversed','original')):
        vals=[next(r for r in summary if r['model']==n and r['condition']==c) for n in ('untouched','A','B')]
        y=np.array([r[field] for r in vals]); ci=np.array([r[interval] for r in vals]).T
        axes[j].errorbar(np.arange(3)+(k-1)*.2,y,yerr=np.maximum(0,np.array([y-ci[0],ci[1]-y])),fmt='o',label=c,color=colors[c],capsize=3)
    axes[j].set_xticks(range(3),['Untouched','A','B']);axes[j].set_ylabel(ylabel)
axes[0].legend(fontsize=8)
axes[2].errorbar([0],[seed_delta.mean()],yerr=[[max(0,seed_delta.mean()-low)],[max(0,high-seed_delta.mean())]],fmt='o',capsize=4)
axes[2].scatter([.15]*3,seed_delta,s=15,label='Seeds')
axes[2].axhline(3,color='#d27032',linestyle='--',label='3-point margin');axes[2].axhline(0,color='grey',linewidth=.6)
axes[2].set_xticks([0],['Extra miss-rate increase']);axes[2].set_ylabel('Percentage points');axes[2].legend(fontsize=8)
fig.savefig(OUT/'formal_results.png',dpi=160)
fig.savefig(OUT/'formal_results.svg')
print(json.dumps(report,indent=2))
