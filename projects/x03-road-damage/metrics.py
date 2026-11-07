"""Explicit operational matching/geometry; AP is computed by the pinned YOLO validator."""
import numpy as np

def grid_cell(x,y,width,height):
    gain=640/max(width,height)
    # Ultralytics LetterBox rounds resized dimensions then splits integer padding.
    left=round((640-round(width*gain))/2-.1)
    top=round((640-round(height*gain))/2-.1)
    return min(39,max(0,int((y*gain+top)/16))),min(39,max(0,int((x*gain+left)/16)))

def xyxy(boxes, width, height):
    out=[]
    for c,x,y,w,h in boxes:
        out.append([c,(x-w/2)*width,(y-h/2)*height,(x+w/2)*width,(y+h/2)*height])
    return np.asarray(out,dtype=float).reshape(-1,5)

def iou(a,b):
    lo=np.maximum(a[:2],b[:,:2]); hi=np.minimum(a[2:],b[:,2:])
    inter=np.maximum(0,hi-lo).prod(1)
    area=np.maximum(0,a[2:]-a[:2]).prod()
    return inter/(area+np.maximum(0,b[:,2:]-b[:,:2]).prod(1)-inter+1e-12)

def match(gt,pred,threshold,overlap=.5):
    # GT: class,x1,y1,x2,y2; prediction: x1,y1,x2,y2,confidence,class.
    used=set(); pairs=[]; fp=[]
    for i in sorted(range(len(pred)),key=lambda i:-pred[i,4]):
        if pred[i,4]<threshold: continue
        eligible=[j for j in range(len(gt)) if j not in used and gt[j,0]==pred[i,5]]
        if eligible:
            overlaps=iou(pred[i,:4],gt[eligible,1:]); j=int(np.argmax(overlaps))
            if overlaps[j]>=overlap:
                used.add(eligible[j]); pairs.append((i,eligible[j])); continue
        fp.append(i)
    return pairs,fp,[j for j in range(len(gt)) if j not in used]

def masks(gt,width,height):
    sides=(gt[:,3:5]-gt[:,1:3])*640/max(width,height)
    small=sides.prod(1)<32**2; thin=sides.min(1)<16
    return dict(all=np.ones(len(gt),dtype=bool),small=small,thin=thin,small_or_thin=small|thin,
                B_eligible=(small|thin)&(sides.min(1)>=8))

def operating(records,predictions,threshold):
    totals={k:dict(tp=0,gt=0) for k in ['all','small','thin','small_or_thin','B_eligible']}
    fps=0; damage_images=0; images_with_miss=0; per_image=[]
    for r in records:
        gt=xyxy(r['boxes'],r['width'],r['height']); pred=np.asarray(predictions[r['id']],float).reshape(-1,6)
        pairs,fp,miss=match(gt,pred,threshold); mm=masks(gt,r['width'],r['height']); hit={j for _,j in pairs}
        for k,m in mm.items():
            totals[k]['gt']+=int(m.sum()); totals[k]['tp']+=sum(bool(m[j]) for j in hit)
        fps+=len(fp); damage_images+=bool(len(gt)); images_with_miss+=bool(miss)
        per_image.append(dict(id=r['id'],group=r['group'],tp=len(pairs),fp=len(fp),fn=len(miss),
                              target_gt=int(mm['small_or_thin'].sum()),target_tp=sum(bool(mm['small_or_thin'][j]) for j in hit)))
    for v in totals.values(): v['recall']=v['tp']/v['gt'] if v['gt'] else None; v['sparse']=v['gt']<30
    tp=totals['all']['tp']; fn=totals['all']['gt']-tp
    return dict(threshold=threshold,geometry=totals,precision=tp/(tp+fps) if tp+fps else 0,
                fp_per_image=fps/max(1,len(records)),misses_per_image=fn/max(1,len(records)),
                damage_images_with_miss_fraction=images_with_miss/damage_images if damage_images else None,
                images=len(records),per_image=per_image)

def select_threshold(records,predictions):
    # Fixed reproducible grid; predictions below .001 are not retained.
    rows=[]
    for t in np.linspace(.001,.999,200):
        m=operating(records,predictions,float(t)); p=m['precision']; rec=m['geometry']['all']['recall'] or 0
        rows.append((float(t),p,rec,2*p*rec/(p+rec) if p+rec else 0))
    eligible=[r for r in rows if r[1]>=.7]
    chosen=max(eligible,key=lambda r:(r[2],r[0])) if eligible else max(rows,key=lambda r:(r[3],r[0]))
    return chosen[0],dict(rule='precision>=0.70, maximum recall, ties higher threshold' if eligible else 'best F1 fallback',grid=rows)

def average_precision_binary(labels,scores):
    labels=np.asarray(labels,bool); scores=np.asarray(scores,float)
    if not labels.any(): return None
    # Tie-aware stepwise average precision (same definition as sklearn average_precision_score).
    order=np.argsort(-scores,kind='stable'); y=labels[order]; s=scores[order]
    ends=np.r_[np.where(np.diff(s)!=0)[0],len(s)-1]
    tp=np.cumsum(y)[ends]; recall=tp/y.sum(); precision=tp/(ends+1)
    return float(np.sum(np.diff(np.r_[0,recall])*precision))

def bootstrap(records,per_image,n=1000):
    groups={}
    for x in per_image: groups.setdefault(x['group'],[]).append(x)
    values=list(groups.values()); rng=np.random.default_rng(42); rows=[]
    for _ in range(n):
        sample=[x for i in rng.integers(0,len(values),len(values)) for x in values[i]]
        tp=sum(x['tp'] for x in sample); fp=sum(x['fp'] for x in sample); fn=sum(x['fn'] for x in sample)
        tg=sum(x['target_gt'] for x in sample); tt=sum(x['target_tp'] for x in sample)
        rows.append([tp/max(1,tp+fn),tp/max(1,tp+fp),fp/len(sample),tt/tg if tg else np.nan])
    return {k:np.nanpercentile(np.asarray(rows)[:,i],[2.5,97.5]).tolist() for i,k in enumerate(['recall','precision','fp_per_image','small_or_thin_recall'])}
