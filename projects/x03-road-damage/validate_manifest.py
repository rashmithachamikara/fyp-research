"""Independent local checks of the frozen preparation manifest, without images."""
import collections
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def validate():
    p=next((ROOT/'artifacts/prepare').rglob('manifest.json'))
    rows=json.loads(p.read_text()); assert len({r['id'] for r in rows})==len(rows)
    groups={}; stats={}
    for r in rows:
        assert r['country'] in ['India','Czech','United_States']
        assert r['width']>0 and r['height']>0
        if r['split']!='excluded_overlap':
            if r['group'] in groups: assert groups[r['group']]==r['split']
            groups[r['group']]=r['split']
        key=r['country']+'/'+r['split']
        s=stats.setdefault(key,dict(images=0,negative_images=0,classes=[0]*4,small_or_thin=0,small_or_thin_classes=[0]*4,B_eligible=0))
        s['images']+=1; s['negative_images']+=not bool(r['boxes'])
        for cls,x,y,w,h in r['boxes']:
            assert cls in range(4) and 0<=x<=1 and 0<=y<=1 and 0<w<=1 and 0<h<=1
            assert x-w/2>=-1e-6 and y-h/2>=-1e-6 and x+w/2<=1+1e-6 and y+h/2<=1+1e-6
            s['classes'][cls]+=1
            sw=w*r['width']*640/max(r['width'],r['height']); sh=h*r['height']*640/max(r['width'],r['height'])
            target=sw*sh<1024 or min(sw,sh)<16
            s['small_or_thin']+=target; s['B_eligible']+=target and min(sw,sh)>=8
            s['small_or_thin_classes'][cls]+=int(target)
    result=dict(status='passed',manifest_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),records=len(rows),groups=len(groups),statistics=stats)
    (ROOT/'runs/manifest-validation.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))

if __name__=='__main__': validate()
