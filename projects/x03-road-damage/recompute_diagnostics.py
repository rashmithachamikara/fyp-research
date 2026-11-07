"""Repair numerical geometry ties using frozen predictions; no model execution/tuning."""
import ast
import collections
import copy
import datetime
import json
from pathlib import Path

import numpy as np
from metrics import xyxy,match,masks,operating,bootstrap,grid_cell,average_precision_binary
from verify_results import read_artifact

ROOT=Path(__file__).resolve().parent

def recompute():
    path,original=read_artifact('evaluate','summary.json')
    backup=path.with_name('summary-kaggle-original.json')
    if not backup.exists(): backup.write_text(path.read_text(),encoding='utf-8')
    original=json.loads(backup.read_text()); summary=copy.deepcopy(original)
    rows=json.loads(next((ROOT/'artifacts/prepare').rglob('manifest.json')).read_text())
    _,threshold=read_artifact('evaluate','threshold.json'); threshold=threshold['value']
    # Reuse the exact pure C metric implementation from the executed notebook source.
    tree=ast.parse((ROOT/'pilot.py').read_text(encoding='utf-8'))
    function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='c_diagnostics')
    scope=dict(np=np,xyxy=xyxy,match=match,masks=masks,grid_cell=grid_cell,average_precision_binary=average_precision_binary)
    exec(compile(ast.Module(body=[function],type_ignores=[]),'frozen-c-metric','exec'),scope)
    changes={}
    for country in ['India','Czech','United_States']:
        subset=[r for r in rows if r['country']==country and r['split'] in ['source_audit','unseen']]
        _,preds=read_artifact('evaluate',f'predictions-{country}-640.json')
        _,half=read_artifact('evaluate',f'predictions-{country}-320.json')
        op=operating(subset,preds,threshold)
        op['bootstrap95']=bootstrap(subset,op['per_image']); op['C']=scope['c_diagnostics'](subset,preds,threshold)
        positive=[r for r in subset if r['boxes']]; negative=[r for r in subset if not r['boxes']]
        op['positive_images_operating']=operating(positive,preds,threshold) if positive else None
        op['negative_images_operating']=operating(negative,preds,threshold) if negative else None
        op['scale320']=operating(subset,half,threshold)
        transitions={k:collections.Counter() for k in ['all','small_or_thin','B_eligible']}
        byclass={str(c):dict(gt=0,tp=0,fp=0,small_or_thin_gt=0,small_or_thin_tp=0) for c in range(4)}
        for r in subset:
            gt=xyxy(r['boxes'],r['width'],r['height']); mm=masks(gt,r['width'],r['height'])
            pp=np.asarray(preds[r['id']],float).reshape(-1,6); hp=np.asarray(half[r['id']],float).reshape(-1,6)
            pairs,fp,_=match(gt,pp,threshold); hits=[{j for _,j in pairs},{j for _,j in match(gt,hp,threshold)[0]}]
            for k,counts in transitions.items():
                for j in np.flatnonzero(mm[k]):
                    counts['both' if j in hits[0] and j in hits[1] else '640_only' if j in hits[0] else '320_only' if j in hits[1] else 'neither']+=1
            for cls in range(4):
                c=byclass[str(cls)]; c['gt']+=int((gt[:,0]==cls).sum()); c['tp']+=sum(gt[j,0]==cls for _,j in pairs)
                c['fp']+=sum(pp[i,5]==cls for i in fp)
                c['small_or_thin_gt']+=int(((gt[:,0]==cls)&mm['small_or_thin']).sum())
                c['small_or_thin_tp']+=sum(gt[j,0]==cls and mm['small_or_thin'][j] for _,j in pairs)
        for cls,c in byclass.items():
            c={k:int(v) for k,v in c.items()}; byclass[cls]=c
            c.update(precision=c['tp']/(c['tp']+c['fp']) if c['tp']+c['fp'] else None,
                     recall=c['tp']/c['gt'] if c['gt'] else None,sparse=c['gt']<30,
                     small_or_thin_recall=c['small_or_thin_tp']/c['small_or_thin_gt'] if c['small_or_thin_gt'] else None,
                     small_or_thin_sparse=c['small_or_thin_gt']<30)
        op['byclass']=byclass; op['B_scale_transitions']={k:dict(v) for k,v in transitions.items()}
        op['AP']=original[country]['AP']
        for k in ['precision','fp_per_image','misses_per_image']:
            assert op[k]==original[country][k],(country,k,'Unexpected non-geometry change')
        assert op['geometry']['all']==original[country]['geometry']['all']
        changes[country]=dict(old_target_gt=original[country]['geometry']['small_or_thin']['gt'],new_target_gt=op['geometry']['small_or_thin']['gt'],new_C=op['C'])
        summary[country]=op
    summary['metric_revision']=dict(reason='Strict size cutoffs: round transformed side lengths to 6 decimal pixels to eliminate cancellation at exact boundaries',
        applied=datetime.datetime.now().astimezone().isoformat(),model_predictions_threshold_and_AP_unchanged=True,original_file=backup.name)
    path.write_text(json.dumps(summary,indent=2),encoding='utf-8')
    (ROOT/'runs/geometry-correction.json').write_text(json.dumps(changes,indent=2),encoding='utf-8')
    print(json.dumps(changes,indent=2))

if __name__=='__main__': recompute()
