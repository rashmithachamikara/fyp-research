"""Verify B artifacts, compute paired intervals, and write bounded pilot conclusions."""
import collections
import csv
import gzip
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import yaml

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent))
from metrics import match,masks,xyxy
ARMS=['baseline','generic','small_thin']; COUNTRIES=['India','Czech','United_States']

def read(stage,name):
    candidates=[p for p in (ROOT/'artifacts'/stage).rglob(name) if p.parent.name=='results']
    assert len(candidates)==1,(stage,name,candidates)
    return candidates[0],json.loads(candidates[0].read_text())

def compact(value):
    if isinstance(value,dict): return {k:compact(v) for k,v in value.items() if k!='per_image'}
    if isinstance(value,list): return [compact(v) for v in value]
    return value

def paired(a,b):
    # Shared image/group resampling, not independent resampling of method outputs.
    assert [r['id'] for r in a]==[r['id'] for r in b]
    groups=collections.defaultdict(lambda:np.zeros((2,6),dtype=float))
    for left,right in zip(a,b):
        for j,r in enumerate([left,right]):
            groups[r['group']][j]+=[r['tp'],r['tp']+r['fn'],r['target_tp'],r['target_gt'],r['fp'],1]
    data=np.stack(list(groups.values())); rng=np.random.default_rng(42); values=[]
    for _ in range(1000):
        sums=data[rng.integers(0,len(data),len(data))].sum(0)
        def stats(s): return np.array([s[0]/s[1] if s[1] else np.nan,s[2]/s[3] if s[3] else np.nan,s[4]/s[5]])
        values.append(stats(sums[0])-stats(sums[1]))
    return {k:np.nanpercentile(np.array(values)[:,i],[2.5,97.5]).tolist() for i,k in enumerate(['overall_recall_difference','target_recall_difference','fp_per_image_difference'])}


def detection_changes(records,predictions,thresholds):
    changes={name:{'all':collections.Counter(),'small_or_thin':collections.Counter(),'byclass':{str(c):collections.Counter() for c in range(4)},'fp_images':collections.Counter()}
             for name in ['B_vs_generic','B_vs_baseline','generic_vs_baseline']}
    for r in records:
        gt=xyxy(r['boxes'],r['width'],r['height']); target=masks(gt,r['width'],r['height'])['small_or_thin']; hits={}; fps={}
        for arm in ARMS:
            pp=np.asarray(predictions[arm][r['id']],float).reshape(-1,6)
            pairs,false,_=match(gt,pp,thresholds[arm]); hits[arm]={j for _,j in pairs}; fps[arm]=len(false)
        for name,a,b in [('B_vs_generic','small_thin','generic'),('B_vs_baseline','small_thin','baseline'),('generic_vs_baseline','generic','baseline')]:
            result=changes[name]
            for j,box in enumerate(gt):
                state=('retained' if j in hits[b] else 'gained') if j in hits[a] else ('lost' if j in hits[b] else 'missed_by_both')
                result['all'][state]+=1; result['byclass'][str(int(box[0]))][state]+=1
                if target[j]: result['small_or_thin'][state]+=1
            result['fp_images']['higher' if fps[a]>fps[b] else 'lower' if fps[a]<fps[b] else 'equal']+=1
    return changes


def verify_telemetry(arm,batch):
    path=next((ROOT/'artifacts'/arm.replace('_','-')).rglob('aux-batches.jsonl.gz'))
    batches=(8264+batch-1)//batch; epochs=collections.Counter(); previous=0
    counters=collections.Counter(); populations=[]
    with gzip.open(path,'rt') as f:
        for line in f:
            r=json.loads(line); epoch=r['epoch']; index=r['batch']
            assert index==epochs[epoch] and 1<=epoch<=50 and index<batches
            epochs[epoch]+=1
            assert r['teacher_updates_before']==previous
            assert r['teacher_updates_after']-previous in [0,1]
            previous=r['teacher_updates_after']
            assert abs(r['weight']-min(1.,((epoch-1)+index/batches)/5))<1e-8
            assert 0<=r['usable']<=r['selected']<=r['visible']<=r['total']
            assert r['selected']==(r['visible'] if arm=='generic' else r['target'])
            assert r['usable']+r['skip_no_positive']+r['skip_zero_weight']==r['selected']
            assert sum(r['selected_by_class'])==r['selected'] and sum(r['usable_by_class'])==r['usable']
            assert np.isfinite([r['aux'],r['kl'],r['box_l1'],r['total_batch_loss'],*r['supervised_items'].values()]).all()
            assert abs(r['aux']-r['kl']-r['box_l1'])<1e-5
            actual_batch=min(batch,8264-index*batch)
            expected=sum(r['supervised_items'].values())+r['weight']*r['aux']
            assert abs(r['total_batch_loss']/actual_batch-expected)<1e-4*max(1,abs(expected))
            for key in ['total','visible','target','selected','usable','skip_no_positive','skip_zero_weight']: counters[key]+=r[key]
            populations.append((r['total'],r['visible'],r['target']))
    assert set(epochs)==set(range(1,51)) and set(epochs.values())=={batches}
    return dict(batches=sum(epochs.values()),ema_updates=previous,counts=dict(counters)),populations

def report():
    _,summary=read('evaluate','b-summary.json'); _,finished=read('evaluate','evaluation-complete.json')
    frozen=finished['frozen']; cfg=finished['experiment']; records={}; verified={}; histories={}; recipes={}; optimizers={}
    _,source_frozen=read('select','frozen-models.json'); assert frozen==source_frozen
    manifest_path=next((ROOT.parent/'artifacts/prepare').rglob('manifest.json'))
    assert hashlib.sha256(manifest_path.read_bytes()).hexdigest()==cfg['manifest_sha256']
    manifest=json.loads(manifest_path.read_text())
    assert set(frozen['selection_ids'])=={r['id'] for r in manifest if r['split']=='selection'}
    original_populations={}
    for split in ['train','selection','source_audit','unseen']:
        records_for_split=[r for r in manifest if r['split']==split]
        counts={name:[0]*4 for name in ['all','small','thin','small_or_thin','B_eligible']}
        for r in records_for_split:
            gt=xyxy(r['boxes'],r['width'],r['height']); geometry=masks(gt,r['width'],r['height'])
            for name,mask in geometry.items():
                for cls in range(4): counts[name][cls]+=int(((gt[:,0]==cls)&mask).sum())
        original_populations[split]=dict(images=len(records_for_split),class_order=['D00','D10','D20','D40'],counts_by_class=counts)
    for arm in ARMS:
        stage=arm.replace('_','-'); record_path,record=read(stage,f'{arm}-record.json'); records[arm]=record
        assert record['epochs']==50 and record['seed']==42 and record['status']=='complete'
        assert record['coco_sha256']==cfg['coco_sha256'] and record['manifest_sha256']==cfg['manifest_sha256']
        digest=hashlib.sha256((record_path.parent/f'{arm}-best.pt').read_bytes()).hexdigest()
        assert digest==record['best_sha256']==frozen['arms'][arm]['checkpoint_sha256']
        history=next((ROOT/'artifacts'/stage).rglob(f'{arm}-history.csv'))
        with open(history,newline='') as f: rows=list(csv.DictReader(f))
        assert len(rows)==50 and int(float(rows[-1]['epoch']))==50
        histories[arm]=rows
        recipe=yaml.safe_load((record_path.parent/f'{arm}-args.yaml').read_text())
        recipes[arm]={k:v for k,v in recipe.items() if k not in ['name','save_dir']}
        _,optimizers[arm]=read(stage,'optimizer-effective.json')
        verified[arm]=digest
        with gzip.open(next((ROOT/'artifacts/select').rglob(f'predictions-selection-{arm}.json.gz')),'rt') as f: source_predictions=json.load(f)
        assert set(source_predictions)==set(frozen['selection_ids'])
        for country in COUNTRIES:
            preds=next((ROOT/'artifacts/evaluate').rglob(f'predictions-{arm}-{country}.json.gz'))
            with gzip.open(preds,'rt') as f: predictions=json.load(f)
            expected={r['id'] for r in manifest if r['country']==country and r['split'] in ['source_audit','unseen']}
            assert set(predictions)==expected=={r['id'] for r in summary[arm][country]['per_image']}
            assert summary[arm][country]['images']=={'India':750,'Czech':283,'United_States':4805}[country]
            assert summary[arm][country]['geometry']['small_or_thin']['gt']=={'India':62,'Czech':8,'United_States':528}[country]
            metric=summary[arm][country]; classes=list(metric['byclass'].values())
            assert sum(r['gt'] for r in classes)==metric['geometry']['all']['gt']
            assert sum(r['tp'] for r in classes)==metric['geometry']['all']['tp']
            assert sum(r['target_gt'] for r in classes)==metric['geometry']['small_or_thin']['gt']
            assert sum(r['target_tp'] for r in classes)==metric['geometry']['small_or_thin']['tp']
            assert abs(sum(r['fp'] for r in classes)/metric['images']-metric['fp_per_image'])<1e-10
    expected_overlays={f'example-{arm}-{r["id"]}.jpg' for arm in ARMS for country in COUNTRIES
                       for r in sorted([r for r in manifest if r['country']==country and r['split'] in ['source_audit','unseen']],key=lambda r:hashlib.sha256(r['id'].encode()).hexdigest())[:6]}
    assert {p.name for p in (ROOT/'artifacts/evaluate').rglob('example-*.jpg')}==expected_overlays
    assert len({r['batch'] for r in records.values()})==1
    assert all(recipes[a]==recipes['baseline'] and optimizers[a]==optimizers['baseline'] for a in ARMS)
    telemetry={}; populations={}
    for arm in ARMS[1:]: telemetry[arm],populations[arm]=verify_telemetry(arm,records[arm]['batch'])
    same_augmented_population=populations['generic']==populations['small_thin']
    for arm in ARMS:
        _,timing=read(arm.replace('_','-'),'timing.json')
        assert len(timing)==50 and [r['epoch'] for r in timing]==list(range(1,51))
        if arm!='baseline': assert timing[-1]['teacher_updates']==telemetry[arm]['ema_updates']
        parity_path,parity=read('select',f'export-parity-{arm}.json')
        assert len(parity)==3 and all(r['id'] in frozen['selection_ids'] and np.isfinite(r['max_absolute_difference']) for r in parity)
    pairs={}; transitions={}
    for country in COUNTRIES:
        pairs[country]={name:paired(summary[a][country]['per_image'],summary[b][country]['per_image']) for name,a,b in [('B_vs_generic','small_thin','generic'),('B_vs_baseline','small_thin','baseline'),('generic_vs_baseline','generic','baseline')]}
        predictions={}
        for arm in ARMS:
            with gzip.open(next((ROOT/'artifacts/evaluate').rglob(f'predictions-{arm}-{country}.json.gz')),'rt') as f: predictions[arm]=json.load(f)
        transitions[country]=detection_changes([r for r in manifest if r['country']==country and r['split'] in ['source_audit','unseen']],predictions,{a:frozen['arms'][a]['threshold'] for a in ARMS})
    generic=summary['generic']['United_States']; b=summary['small_thin']['United_States']
    recall_win=b['geometry']['small_or_thin']['recall']>generic['geometry']['small_or_thin']['recall']
    fp_ok=b['fp_per_image']<=1.1*generic['fp_per_image'] if generic['fp_per_image'] else b['fp_per_image']==0
    outcome='promising' if recall_win and fp_ok else 'no improvement under this configuration'
    lines=['# B prototype comparison','',f'**One-seed development outcome: {outcome}.** This is a point-estimate screen, not evidence across seeds/countries. Japan was untouched.','',
           'All arms: fresh identical COCO initialization, YOLO11s640, seed42,50epochs, pinned Ultralytics8.4.192. Checkpoints and confidence thresholds were selected using source data and frozen together before evaluation.', '',
           '| Arm | Country | mAP50 | mAP50:95 | Recall | Small/thin recall | Precision | FP/image |',
           '|---|---|---:|---:|---:|---:|---:|---:|']
    for arm in ARMS:
        for country in COUNTRIES:
            m=summary[arm][country]
            lines.append(f"| {arm} | {country} | {m['AP']['map50']:.4f} | {m['AP']['map50_95']:.4f} | {m['geometry']['all']['recall']:.4f} | {m['geometry']['small_or_thin']['recall']:.4f} | {m['precision']:.4f} | {m['fp_per_image']:.4f} |")
    lines+=['','## Primary comparison','',f'US B minus generic small/thin recall: {b["geometry"]["small_or_thin"]["recall"]-generic["geometry"]["small_or_thin"]["recall"]:.4f}. Recall condition passes: {recall_win}; FP/image guard passes: {fp_ok}.',
            'Paired image/group bootstrap95% intervals for B minus generic (one training seed): `'+json.dumps(pairs['United_States']['B_vs_generic'])+'`.',
            '', 'The compact JSON includes all per-country comparisons, per-class support, and results at the common baseline threshold. Full per-image metrics and predictions remain in local ignored artifacts.', '',
            '## Common confidence threshold','',
            'All arms below use the fresh baseline threshold, exposing changes caused by confidence selection.', '',
            '| Arm | Country | Overall recall | Small/thin recall | FP/image |','|---|---|---:|---:|---:|']
    base=summary['baseline']['United_States']
    primary_position=lines.index('## Primary comparison')+4
    lines[primary_position:primary_position]=['',f'US B minus fresh baseline small/thin recall: {b["geometry"]["small_or_thin"]["recall"]-base["geometry"]["small_or_thin"]["recall"]:.4f}; FP/image difference: {b["fp_per_image"]-base["fp_per_image"]:.4f}.',
        f'US overall detection changes (B minus comparator): mAP50:95 {b["AP"]["map50_95"]-generic["AP"]["map50_95"]:+.4f} versus generic and {b["AP"]["map50_95"]-base["AP"]["map50_95"]:+.4f} versus baseline; overall recall {b["geometry"]["all"]["recall"]-generic["geometry"]["all"]["recall"]:+.4f} versus generic and {b["geometry"]["all"]["recall"]-base["geometry"]["all"]["recall"]:+.4f} versus baseline.',
        f'At the shared baseline threshold, US small/thin recall is B={b["common_threshold"]["geometry"]["small_or_thin"]["recall"]:.4f}, generic={generic["common_threshold"]["geometry"]["small_or_thin"]["recall"]:.4f}, baseline={base["common_threshold"]["geometry"]["small_or_thin"]["recall"]:.4f}.','']
    for arm in ARMS:
        for country in COUNTRIES:
            m=summary[arm][country]['common_threshold']
            lines.append(f"| {arm} | {country} | {m['geometry']['all']['recall']:.4f} | {m['geometry']['small_or_thin']['recall']:.4f} | {m['fp_per_image']:.4f} |")
    lines+=['','## Class support and missed damage','',
            '| Arm | Country | Class | Matched/all GT | Matched/small-thin GT |','|---|---|---|---:|---:|']
    for arm in ARMS:
        for country in COUNTRIES:
            for cls,m in summary[arm][country]['byclass'].items():
                lines.append(f"| {arm} | {country} | {['D00','D10','D20','D40'][int(cls)]} | {m['tp']}/{m['gt']} | {m['target_tp']}/{m['target_gt']} |")
    lines+=['','| Arm | Country | Missed objects/image | Damage images with a miss |','|---|---|---:|---:|']
    for arm in ARMS:
        for country in COUNTRIES:
            m=summary[arm][country]
            lines.append(f"| {arm} | {country} | {m['misses_per_image']:.4f} | {m['damage_images_with_miss_fraction']:.4f} |")
    lines+=['', 'US B versus generic matched-GT transitions: `'+json.dumps(transitions['United_States']['B_vs_generic'])+'`. Gained/lost refer to the same ground-truth objects at IoU>=0.50 and each arm\'s source-selected threshold.', '',
            '## Resources and interpretation','']
    total=0
    resource_lines=['# Measured B prototype resources','', 'Full training uses one Tesla T4 per private job. Times below include training and export, exclude queueing. Peaks are cumulative allocator measurements for each training job.','',
                    '| Arm | Hours | Peak allocated GiB | Peak reserved GiB | Usable/selected augmented GT |','|---|---:|---:|---:|---:|']
    for arm in ARMS:
        _,timing=read(arm.replace('_','-'),'timing.json'); seconds=records[arm]['seconds']; total+=seconds
        peak=max(r['reserved'] for r in timing)/1024**3
        allocated=max(r['allocated'] for r in timing)/1024**3; used=selected=0
        lines.append(f'- {arm}: {seconds/3600:.2f} hours; peak reserved{peak:.2f}GiB; threshold{frozen["arms"][arm]["threshold"]:.4f}.')
        if arm!='baseline':
            unique={}
            for r in timing: unique.setdefault(r['epoch'],r)
            used=sum(r.get('usable',0) for r in unique.values()); selected=sum(r.get('selected',0) for r in unique.values())
            lines.append(f'  Augmented GT instances selected{selected}; usable{used}. These are repeated/augmented training instances, not unique original annotations.')
            no_positive=sum(r.get('skip_no_positive',0) for r in unique.values()); no_weight=sum(r.get('skip_zero_weight',0) for r in unique.values())
            class_counts=[sum(r.get('usable_by_class',[0]*4)[i] for r in unique.values()) for i in range(4)]
            resource_lines+=['',f'{arm}: no-positive skips={no_positive}; zero-weight skips={no_weight}; usable fraction={used/selected if selected else 0:.5f}; empty-selection batches={sum(r.get("empty_selection_batches",0) for r in unique.values())}; usable class counts [D00,D10,D20,D40]={class_counts}.',
                             f'Unweighted epoch means of auxiliary loss={np.mean([r["aux_mean"] for r in unique.values()]):.6f}, KL={np.mean([r["kl_mean"] for r in unique.values()]):.6f}, normalized-box L1={np.mean([r["box_l1_mean"] for r in unique.values()]):.6f}. Per-epoch/per-batch telemetry remains in artifacts.']
            if used==0: outcome='inconclusive/implementation-limited'
        resource_lines.insert(6+ARMS.index(arm),f'| {arm} | {seconds/3600:.3f} | {allocated:.3f} | {peak:.3f} | {used}/{selected} |')
        _,optimizer=read(arm.replace('_','-'),'optimizer-effective.json')
        resource_lines+=['',f'{arm} effective optimizer: `'+json.dumps(optimizer)+'`.']
        source_ap=[float(r['metrics/mAP50-95(B)']) for r in histories[arm]]
        resource_lines+=['',f'{arm} convergence diagnostic: best recorded source-selection mAP50:95={max(source_ap):.5f}; first CSV maximum at epoch{source_ap.index(max(source_ap))+1}; improvement in best score over epochs41-50 versus epochs1-40={max(source_ap)-max(source_ap[:40]):.5f}. Training stopped at the fixed50-epoch prototype budget; convergence is not established.']
    stage_seconds=0
    for stage in ['select','evaluate']:
        _,resource=read(stage,'stage-resources.json'); stage_seconds+=resource['seconds_including_preparation']
        resource_lines+=['',f'{stage}: {resource["seconds_including_preparation"]/3600:.3f} hours including preparation; peak allocated={resource["allocated"]/1024**3:.3f}GiB, reserved={resource["reserved"]/1024**3:.3f}GiB; workspace before cleanup={resource["working_bytes_before_cleanup"]/1024**3:.3f}GiB.']
    resource_lines+=['',f'Measured full training/export plus selection/evaluation/preparation: {(total+stage_seconds)/3600:.3f} GPU-session hours. Smoke unit tests, smoke recovery and notebook installation/startup are additional. Original smoke gate estimate9.256h included20% contingency and1h for scoring. Failed smokev1 is a separate implementation overhead recorded in the main log.','',
                     'Small/thin augmented-instance counts can increase through mosaic. Evaluation support uses original-image geometry and is not comparable to repeated training-instance counts.', '',
                     f'Full telemetry validation: finite auxiliary/supervised losses, batch-scaled total-loss reconstruction, exact ramp, complete batch coverage, skip/class-count reconciliation and EMA-update continuity passed. Generic and B per-batch augmented geometry counts identical: {same_augmented_population}. This count check does not establish pixel-level view equality. Details: `'+json.dumps(telemetry)+'`.']
    resource_lines+=['','Original-image640 geometry populations (unique annotations; class orderD00,D10,D20,D40): `'+json.dumps(original_populations)+'`. B_eligible is the small/thin union with short side>=8px. These original supports differ from the repeated augmented training counts above; mosaic can move originally larger objects into the focused mask.']
    overhead_path=ROOT/'runs/duplicate-selection-overhead.json'
    if overhead_path.exists():
        overhead=json.loads(overhead_path.read_text())['seconds_including_preparation']/3600
        resource_lines+=['',f'Execution fault: duplicate local controllers submitted source selection twice. Version1 added {overhead:.3f} measured T4-session hours; version2 was retained. Their frozen configurations match exactly. Each detector was trained once. A tested OS-held file lock now prevents duplicate executors. Including this measured redundant stage: {(total+stage_seconds)/3600+overhead:.3f} hours, plus smoke/install/startup overhead.']
        lines+=['',f'Execution overhead: source selection was submitted twice by duplicate local controllers; the redundant job used {overhead:.3f} measured T4-session hours and produced an identical frozen configuration. All detector training arms ran once. A process lock fixed the duplication.']
    before_path=ROOT/'runs/quota-before.json'; after_path=ROOT/'runs/quota-after.json'
    if before_path.exists() and after_path.exists():
        before=json.loads(before_path.read_text()); after=json.loads(after_path.read_text())
        def used_seconds(value):
            h,m,s=value.split(':'); return float(h)*3600+float(m)*60+float(s)
        quota_delta=(used_seconds(after['_time_used'])-used_seconds(before['_time_used']))/3600
        resource_lines+=['',f'Account-level quota cross-check: used GPU quota increased by {quota_delta:.3f} hours between saved before/after snapshots; this is distinct from per-job process profiling. Final account usage={after["_time_used"]} of30h; reserved={after["_time_reserved"]}; paid scaling enabled={after["_is_pay_to_scale_enabled"]}. Queue time is reported separately in the main log.']
    lines+=['',f'Total measured full-training/export time: {total/3600:.2f}GPU-session hours. Smoke, selection and evaluation are additional. Queue time is not GPU training time.',
            '', 'All54 hash-selected example overlays are included in evaluation artifacts: green=matched GT, red=missed GT, cyan=predictions at the arm-specific source-selected threshold. They are deterministic examples, not a representative error-rate estimate.',
            '', 'Loss and teacher/BN policies match between generic and focused arms; their selection mask differs. The supervised baseline uses fewer passes, so baseline comparisons are equal training exposure, not equal compute. Without count-matched random consistency, geometry-specific causation is unresolved.',
            '', 'Small/thin source annotations are dominated by potholes. Box geometry is not physical crack width. US outcomes are development evidence; do not tune on these results and then present the same US set as confirmation. One lambda/ramp and one seed cannot disprove consistency methods generally. Confidence intervals represent paired image/group sampling, not training-seed/country variation. Stronger baseline recipes, count-matched/random and resolution controls, additional seeds and countries belong to the main study.', '']
    if outcome=='inconclusive/implementation-limited': lines[2]='**Outcome: inconclusive/implementation-limited (no usable consistency signal).**'
    (ROOT/'report.md').write_text('\n'.join(lines),encoding='utf-8')
    (ROOT/'resource-report.md').write_text('\n'.join(resource_lines),encoding='utf-8')
    (ROOT/'runs/summary.json').write_text(json.dumps(compact(summary),indent=2))
    (ROOT/'runs/paired-intervals.json').write_text(json.dumps(pairs,indent=2))
    (ROOT/'runs/paired-detection-changes.json').write_text(json.dumps(transitions,indent=2))
    (ROOT/'runs/geometry-populations.json').write_text(json.dumps(original_populations,indent=2))
    (ROOT/'runs/verification.json').write_text(json.dumps(dict(status='passed',checkpoints=verified,counts_verified=True,shared_batch=True,identical_resolved_recipe=True,source_only_selection=True,telemetry=telemetry,same_augmented_geometry_counts=same_augmented_population,outcome=outcome),indent=2))

if __name__=='__main__': report()
