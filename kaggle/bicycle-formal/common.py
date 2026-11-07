import csv
import gc
import hashlib
import io
import json
import os
import random
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
from torch import nn
from torchvision.ops import box_convert, box_iou

OUT = Path('/kaggle/working')
MOUNT = Path('/kaggle/input')
DIGEST = 'dfbf35a66d13e0b57447cb91b7f0e9dbc96879240ebe2a3d929f05b6bee851df'
REVISION = 'a2bb814dd30d776dcf7e30523b00659f4f141c71'
torch.set_num_threads(2)

def locate(name):
    return next(MOUNT.rglob(name))

def write_json(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2))

def write_csv(name, rows):
    with (OUT / name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

manifest_file = locate('formal_split.csv')
assert hashlib.sha256(manifest_file.read_bytes()).hexdigest() == DIGEST
with manifest_file.open() as f:
    MANIFEST = list(csv.DictReader(f))
PARTS = {s: sorted(int(r['source_id']) for r in MANIFEST if r['split'] == s) for s in ('train','validation','test')}
assert [len(PARTS[s]) for s in PARTS] == [3400,800,2000]
assert len({int(r['source_id']) for r in MANIFEST}) == 6200

def annotations():
    path = locate('instances_train2017.json')
    with path.open() as f:
        data = json.load(f)
    needed = {int(r['source_id']) for r in MANIFEST}
    sizes = {r['id']: (r['width'],r['height']) for r in data['images'] if r['id'] in needed}
    category = next(r['id'] for r in data['categories'] if r['name']=='bicycle')
    ground = defaultdict(list)
    for a in data['annotations']:
        if a['category_id'] == category and a['image_id'] in needed:
            assert not a['iscrowd']
            ground[a['image_id']].append(a['bbox'])
    result = {}
    for i in needed:
        w,h = sizes[i]
        b = torch.tensor(ground[i],dtype=torch.float32).reshape(-1,4)
        result[i] = box_convert(b / torch.tensor([w,h,w,h]),'xywh','xyxy')
    return path.parent.parent, result

def matching(overlap, scores, threshold):
    available = np.ones(overlap.shape[1],dtype=bool)
    kept = np.flatnonzero(scores >= threshold)
    order = kept[np.argsort(-scores[kept],kind='stable')]
    for qi in order:
        options = np.flatnonzero(available & (overlap[qi] >= .5))
        if len(options):
            available[options[np.argmax(overlap[qi,options])]] = False
    tp = int((~available).sum())
    return tp, len(kept)-tp, int(available.sum()), available

def checks():
    assert matching(np.zeros((2,0)),np.array([.9,.8]),.5)[:3] == (0,2,0)
    assert matching(np.array([[.8],[.9]]),np.array([.9,.8]),.5)[:3] == (1,1,0)
    assert matching(np.array([[.8,.6],[.2,.9]]),np.array([.9,.8]),.5)[:3] == (2,0,0)
    assert matching(np.array([[.8]]),np.array([.4]),.5)[:3] == (0,0,1)
    torch.manual_seed(11)
    h = head_new()
    q = torch.randn(4,256)
    assert torch.equal(h(q),torch.zeros_like(q))

def head_new():
    h = nn.Sequential(nn.Linear(256,32),nn.ReLU(),nn.Linear(32,256))
    nn.init.zeros_(h[-1].weight)
    nn.init.zeros_(h[-1].bias)
    return h

def shard_records(stage):
    paths = sorted(MOUNT.rglob(stage+'-shard-*.pt'))
    for p in paths:
        yield from torch.load(p,map_location='cpu',weights_only=True)

def prepare(rec, ground):
    i = rec['source_id']
    iou = box_iou(box_convert(rec['boxes'],'cxcywh','xyxy'),ground[i])
    labels = torch.zeros(len(iou))
    pairs = torch.nonzero(iou>=.5)
    uq, ug = set(),set()
    if len(pairs):
        labels[pairs[:,0]] = -1
        for k in torch.argsort(iou[pairs[:,0],pairs[:,1]],descending=True,stable=True).tolist():
            qi,gi = pairs[k].tolist()
            if qi not in uq and gi not in ug:
                uq.add(qi)
                ug.add(gi)
                labels[qi] = 1
    rec['iou'] = iou.numpy()
    rec['labels'] = labels
    return rec

def predict(rec, head=None):
    if head is None:
        return rec['logits'].sigmoid().numpy()
    with torch.no_grad():
        return (rec['logits'] + head(rec['queries'].float()) @ rec['text']).sigmoid().numpy()

checks()
