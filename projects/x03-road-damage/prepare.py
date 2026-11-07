"""CPU-only original RDD2022 preparation; no Japan access."""
import collections
import hashlib
import io
import json
import random
import shutil
import tarfile
import time
import urllib.request
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

COUNTRIES = {'India': 7706, 'Czech': 2829, 'United_States': 4805}
CLASSES = ['D00', 'D10', 'D20', 'D40']
BASE = 'https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/'

class RemoteArchive(io.RawIOBase):
    """Read only requested ZIP ranges from the official Figshare archive."""
    def __init__(self):
        import requests
        self.session=requests.Session()
        response=self.session.get('https://ndownloader.figshare.com/files/38030910?x03='+str(time.time_ns()),headers={'Range':'bytes=0-127'},timeout=60)
        response.raise_for_status(); assert response.status_code==206
        self.url=response.url; self.size=int(response.headers['Content-Range'].split('/')[-1]); self.pos=0
    def seekable(self): return True
    def readable(self): return True
    def tell(self): return self.pos
    def seek(self,offset,whence=0):
        self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.size+offset
        return self.pos
    def read(self,n=-1):
        if n<0: n=self.size-self.pos
        n=min(n,self.size-self.pos)
        if not n: return b''
        # Figshare signatures expire after ten seconds: obtain a fresh redirect per request.
        r=self.session.get('https://ndownloader.figshare.com/files/38030910?x03='+str(time.time_ns()),headers={'Range':f'bytes={self.pos}-{self.pos+n-1}'},timeout=120)
        r.raise_for_status()
        if r.status_code!=206 or len(r.content)!=n: raise ValueError('Range server did not return requested bytes')
        self.pos+=n; return r.content

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''): h.update(b)
    return h.hexdigest()

def convert_box(coords, width, height):
    # VOC inclusive 1-based corners -> continuous 0-based image-edge coordinates.
    a, b, c, d = coords
    a, b, c, d = max(0, a-1), max(0, b-1), min(width, c), min(height, d)
    if c <= a or d <= b: raise ValueError('degenerate box')
    return [(a+c)/2/width, (b+d)/2/height, (c-a)/width, (d-b)/height]

def dhash(im):
    a = np.asarray(im.convert('L').resize((9, 8)), dtype=np.int16)
    return int(''.join(map(str, (a[:, 1:] > a[:, :-1]).astype(int).ravel())), 2)

def prepare(root=Path('/kaggle/working')):
    root = Path(root); raw = root/'raw'; out = root/'prepared'; out.mkdir(exist_ok=True)
    (out/'images').mkdir(exist_ok=True); (out/'labels').mkdir(exist_ok=True)
    records, errors, provenance = [], [], []
    # Original S3 country URLs now return 403. Official Figshare distributes a ZIP of country ZIPs.
    remote=RemoteArchive(); outer=zipfile.ZipFile(remote)
    print('Official archive members:',outer.namelist(),flush=True)
    for country, expected in COUNTRIES.items():
        z = root/f'RDD2022_{country}.zip'
        member=next(n for n in outer.namelist() if Path(n).name==country+'.zip')
        url = 'https://figshare.com/articles/dataset/21431547 ; file 38030910 ; member '+member
        print('Range-download', url, flush=True)
        with outer.open(member) as src, open(z,'wb') as dst:
            shutil.copyfileobj(src,dst,length=8*1024*1024)
        provenance.append({'country': country, 'url': url, 'bytes': z.stat().st_size, 'sha256': sha(z)})
        with zipfile.ZipFile(z) as f:
            # Extract only labelled training material; never challenge test data.
            for member in f.infolist():
                p = Path(member.filename)
                if '..' in p.parts or p.is_absolute(): raise ValueError('unsafe archive')
                if 'train' in [x.lower() for x in p.parts] and p.suffix.lower() in ['.jpg', '.jpeg', '.xml']:
                    f.extract(member, raw/country)
        xmls = {p.stem: p for p in (raw/country).rglob('*.xml')}
        images = sorted((raw/country).rglob('*.jpg'))
        if len(images) != expected: raise ValueError(f'{country}: {len(images)} images, expected {expected}')
        for image in images:
            try:
                if image.stem not in xmls: raise ValueError('missing XML is not a negative')
                xml = xmls[image.stem]; tree = ET.parse(xml).getroot()
                with Image.open(image) as im:
                    im.load(); w, h = im.size; ph = dhash(im)
                    pixels = hashlib.sha256(im.convert('RGB').tobytes()).hexdigest()
                if (int(tree.findtext('size/width')), int(tree.findtext('size/height'))) != (w, h):
                    raise ValueError('XML/image dimensions disagree')
                boxes = []; ignored = []
                for obj in tree.findall('object'):
                    name = obj.findtext('name')
                    if name not in CLASSES: ignored.append(name); continue
                    coords = [float(obj.findtext('bndbox/'+k)) for k in ['xmin','ymin','xmax','ymax']]
                    if not np.isfinite(coords).all(): raise ValueError('nonfinite coordinates')
                    boxes.append([CLASSES.index(name), *convert_box(coords, w, h)])
                # Other real damage classes are outside this four-class task; retain images.
                # A malformed spelling resembling a target class is quarantined for audit.
                if any(n not in ['D01','D11','D43','D44','D50'] for n in ignored):
                    raise ValueError('unrecognised class spelling: '+str(ignored))
                dest = out/'images'/image.name; shutil.copy2(image, dest)
                (out/'labels'/f'{image.stem}.txt').write_text('\n'.join(' '.join(map(str,b)) for b in boxes))
                records.append(dict(id=image.stem, country=country, width=w, height=h, boxes=boxes,
                                    sha256=sha(image), xml_sha256=sha(xml), pixels=pixels, dhash=ph,
                                    ignored_classes=ignored,
                                    source_image=str(image.relative_to(raw)), source_xml=str(xml.relative_to(raw))))
            except Exception as e: errors.append({'image': image.name, 'error': str(e)})
        z.unlink()
    # Connected components: exact decoded duplicates and conservative dHash candidates <=3 bits.
    # Candidate grouping is conservative leakage prevention, not proof of semantic duplication.
    parent = list(range(len(records)))
    def find(i):
        while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
        return i
    def union(i,j): parent[find(i)] = find(j)
    buckets = collections.defaultdict(list); pixels_seen = {}; pairs = []
    for i,r in enumerate(records):
        if r['pixels'] in pixels_seen: union(i,pixels_seen[r['pixels']])
        pixels_seen[r['pixels']] = i
        candidates = set()
        for chunk in range(4): candidates.update(buckets[(chunk,(r['dhash']>>(16*chunk))&65535)])
        for j in candidates:
            if (r['dhash'] ^ records[j]['dhash']).bit_count() <= 3:
                union(i,j); pairs.append([records[j]['id'],r['id']])
        for chunk in range(4): buckets[(chunk,(r['dhash']>>(16*chunk))&65535)].append(i)
    groups = collections.defaultdict(list)
    for i,r in enumerate(records): groups[find(i)].append(r)
    for members in groups.values():
        gid = min(r['id'] for r in members)
        for r in members: r['group'] = gid
        if any(r['country']=='United_States' for r in members):
            for r in members: r['split'] = 'unseen' if r['country']=='United_States' else 'excluded_overlap'
    rng = random.Random(42)
    source_groups = [m for m in groups.values() if 'split' not in m[0]]
    rng.shuffle(source_groups)
    totals = collections.Counter(r['country'] for m in source_groups for r in m)
    assigned = collections.defaultdict(collections.Counter)
    for members in sorted(source_groups, key=len, reverse=True):
        counts = collections.Counter(r['country'] for r in members)
        split = max(['train','selection','source_audit'], key=lambda s:
            sum(counts[c]*({'train':.8,'selection':.1,'source_audit':.1}[s]*totals[c]-assigned[c][s]) /
                max(1,{'train':.8,'selection':.1,'source_audit':.1}[s]*totals[c]) for c in counts))
        for r in members: r['split'] = split; assigned[r['country']][split] += 1
    for split in ['train','selection','source_audit','unseen']:
        ids = [r['id'] for r in records if r['split']==split]
        (out/f'{split}.txt').write_text('\n'.join('/kaggle/working/prepared/images/'+i+'.jpg' for i in ids))
    (out/'manifest.json').write_text(json.dumps(records))
    audit = dict(counts={c:dict(collections.Counter(r['split'] for r in records if r['country']==c)) for c in COUNTRIES},
                 quarantine=errors, near_duplicate_pairs=pairs, provenance=provenance,
                 sequence_limitation='No verified route/sequence metadata; filename adjacency is not assumed to identify sequences.',
                 coordinate_convention='VOC inclusive 1-based corners; xmin/ymin minus one, bounds clipped to image edges',
                 duplicate_policy='Group all dHash<=3 candidates conservatively; exclude sources sharing a group with US. No manual duplicate certification.')
    (out/'audit.json').write_text(json.dumps(audit,indent=2))
    for c in COUNTRIES:
        subset = [r for r in records if r['country']==c][:8]
        canvas = Image.new('RGB',(640,160*len(subset)),'white')
        for k,r in enumerate(subset):
            im = Image.open(out/'images'/f"{r['id']}.jpg").convert('RGB'); draw=ImageDraw.Draw(im)
            for cls,x,y,w,h in r['boxes']:
                draw.rectangle([(x-w/2)*im.width,(y-h/2)*im.height,(x+w/2)*im.width,(y+h/2)*im.height],outline='red',width=3)
            im.thumbnail((640,150)); canvas.paste(im,(0,k*160))
        canvas.save(out/f'conversion_{c}.jpg')
    # All splits must remain group-disjoint, except excluded overlap records.
    seen={}
    for r in records:
        if r['split']=='excluded_overlap': continue
        if r['group'] in seen: assert seen[r['group']]==r['split']
        seen[r['group']]=r['split']
    with tarfile.open(root/'prepared.tar.gz','w:gz') as f: f.add(out,arcname='prepared')
    print(json.dumps({k:v for k,v in audit.items() if k not in ['near_duplicate_pairs','quarantine']},indent=2),flush=True)
    # Preserve original XML for reproducibility; avoid saving duplicate raw images in output.
    with tarfile.open(root/'original_xml.tar.gz','w:gz') as f:
        for p in raw.rglob('*.xml'): f.add(p,arcname=str(p.relative_to(raw)))
    shutil.rmtree(raw)
    shutil.rmtree(out/'images'); shutil.rmtree(out/'labels')

if __name__=='__main__': prepare()
