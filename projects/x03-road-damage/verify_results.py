"""Independent local artifact-integrity and data-role checks before reporting."""
import hashlib
import gzip
import csv
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def read_artifact(stage,name):
    candidates=[p for p in (ROOT/'artifacts'/stage).rglob(name) if p.parent.name=='results']
    if not candidates:
        compressed=[p for p in (ROOT/'artifacts'/stage).rglob(name+'.gz') if p.parent.name=='results']
        if len(compressed)==1:
            target=compressed[0].with_suffix('')
            with gzip.open(compressed[0],'rt',encoding='utf-8') as src: target.write_text(src.read(),encoding='utf-8')
            candidates=[target]
    assert len(candidates)==1,(stage,name,candidates)
    return candidates[0],json.loads(candidates[0].read_text())

def verify():
    manifest=next((ROOT/'artifacts/prepare').rglob('manifest.json'))
    rows=json.loads(manifest.read_text())
    expected_hash=json.loads((ROOT/'runs/manifest-validation.json').read_text())['manifest_sha256']
    assert hashlib.sha256(manifest.read_bytes()).hexdigest()==expected_hash,'Preparation manifest changed'
    _,training=read_artifact('train','training-complete.json')
    smoke=json.loads((ROOT/'runs/smoke.json').read_text())
    assert training['status']=='complete' and training['epochs']==50
    assert training['model']==smoke['model'] and training['batch']==smoke['batch']
    history_path=next(p for p in (ROOT/'artifacts/train').rglob('results.csv') if p.parent.name=='results')
    with open(history_path,newline='') as f: history=[{k.strip():v for k,v in r.items()} for r in csv.DictReader(f)]
    assert len(history)==50 and int(float(history[-1]['epoch']))==50,'Actual training history did not complete 50 epochs'
    path,hashes=read_artifact('train','checkpoint-sha256.json')
    verified={}
    for name,digest in hashes.items():
        checkpoint=path.parent/name
        assert checkpoint.stat().st_size>1000000,name
        actual=hashlib.sha256(checkpoint.read_bytes()).hexdigest()
        assert actual==digest,(name,actual,digest)
        verified[name]=actual
    _,threshold=read_artifact('evaluate','threshold.json')
    selection={r['id'] for r in rows if r['split']=='selection'}
    assert set(threshold['selection_ids'])==selection,'Threshold used wrong split'
    assert 0<=threshold['value']<=1
    _,selection_predictions=read_artifact('evaluate','predictions-source-selection-640.json')
    assert set(selection_predictions)==selection
    _,summary=read_artifact('evaluate','summary.json')
    inventory=json.loads((ROOT/'runs/manifest-validation.json').read_text())['statistics']
    coverage={}
    for country in ['India','Czech','United_States']:
        expected={r['id'] for r in rows if r['country']==country and r['split'] in ['source_audit','unseen']}
        assert summary[country]['images']==len(expected)
        role='unseen' if country=='United_States' else 'source_audit'
        assert summary[country]['geometry']['small_or_thin']['gt']==inventory[country+'/'+role]['small_or_thin'],'Geometry count differs from frozen inventory'
        for size in [640,320]:
            _,predictions=read_artifact('evaluate',f'predictions-{country}-{size}.json')
            assert set(predictions)==expected,(country,size,'prediction coverage mismatch')
            for boxes in predictions.values():
                for box in boxes:
                    assert len(box)==6 and all(math.isfinite(x) for x in box)
                    assert 0<=box[4]<=1 and box[5] in range(4)
        for name in ['map50','map50_95']:
            assert math.isfinite(summary[country]['AP'][name]) and 0<=summary[country]['AP'][name]<=1
        coverage[country]=len(expected)
    _,assignment=read_artifact('evaluate','A-assignment.json')
    assert assignment['images']==256 and assignment['records'],'Assignment diagnostic is incomplete'
    result=dict(status='passed',manifest_sha256=expected_hash,checkpoint_sha256=verified,
                source_selection_images=len(selection),evaluation_images=coverage,
                checks=['frozen manifest','completed model/configuration','downloaded checkpoint hashes',
                        'source-only threshold roles','complete prediction coverage at both scales',
                        'finite class/confidence/AP outputs','nonempty assignment diagnostic'])
    (ROOT/'runs/artifact-verification.json').write_text(json.dumps(result,indent=2))
    return result

if __name__=='__main__': print(json.dumps(verify(),indent=2))
