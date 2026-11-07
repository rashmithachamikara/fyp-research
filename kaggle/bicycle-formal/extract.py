import subprocess
import sys
from PIL import Image

started = time.perf_counter()
subprocess.run([sys.executable,'-m','pip','install','-q','transformers==4.57.1'],check=True)
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection
assert torch.cuda.is_available()
device = 'cuda:0'
spec = dict(version=1,manifest_sha256=DIGEST,checkpoint=REVISION,prompt='bicycle.',qualities=[95,90],
            subsampling=2,optimize=False,head=[256,32,256],seeds=[11,23,37],epochs=4,batch=6,
            adamw_lr=.0001,adamw_weight_decay=.01,margin_pp=3,bootstrap_draws=20000,
            threshold_grid=[n/100 for n in range(5,81,5)],threshold_tie='lower',
            training_loss='mean background softplus plus mean matched-positive softplus, divided by 2; background only if no positives',
            probes='pooled final backbone mean/std, decoder mean/std, matched query; StandardScaler and LogisticRegression C=1 liblinear',
            matching='score-ordered greedy, IoU>=0.5, one-to-one, no NMS',evaluation_code_sha256=EVAL_HASH)
if STAGE == 'test':
    lock = json.loads(locate('frozen_training.json').read_text())
    assert lock['manifest_sha256'] == DIGEST and lock['evaluation_code_sha256'] == EVAL_HASH
write_json('run_spec.json',spec)
root, ground = annotations()
processor = AutoProcessor.from_pretrained('IDEA-Research/grounding-dino-tiny',revision=REVISION,use_fast=False)
model = AutoModelForZeroShotObjectDetection.from_pretrained('IDEA-Research/grounding-dino-tiny',revision=REVISION).to(device).eval()
model.requires_grad_(False)
backbone = {}
def capture(module, args, result):
    fm = result[-1][0].detach().float()
    backbone['pooled'] = torch.cat([fm.mean((-2,-1)),fm.std((-2,-1),unbiased=False)],dim=-1)[0].cpu()
hook = model.model.backbone.conv_encoder.register_forward_hook(capture)

def view(rgb, quality):
    if quality:
        buffer = io.BytesIO()
        rgb.save(buffer,format='JPEG',quality=quality,subsampling=2,optimize=False)
        buffer.seek(0)
        with Image.open(buffer) as image:
            rgb = image.convert('RGB')
    inputs = processor(images=rgb,text='bicycle.',return_tensors='pt').to(device)
    with torch.inference_mode():
        pred = model(**inputs)
        queries = pred.intermediate_hidden_states[0,-1]
        word = processor.tokenizer.convert_ids_to_tokens(inputs.input_ids[0].tolist()).index('bicycle')
        text = pred.encoder_last_hidden_state_text[0,word]
        logits = pred.logits[0,:,word]
        torch.testing.assert_close(queries@text,logits,atol=.001,rtol=.0001)
        return dict(queries=queries.half().cpu(),text=text.float().cpu(),logits=logits.float().cpu(),
                    boxes=pred.pred_boxes[0].float().cpu(),backbone=backbone['pooled'])

# Replay cached development records before formal extraction.
devpath = locate('development_manifest.json')
devrows = json.loads(devpath.read_text())[:2]
for row in devrows:
    with Image.open(root/'val2017'/row['filename']) as f:
        r = view(f.convert('RGB'),95)
    old = torch.load(devpath.parent/'features'/f"{row['image_id']}_95.pt",weights_only=True)
    torch.testing.assert_close(r['boxes'],old['boxes_cxcywh'])
    assert torch.equal(head_new()(r['queries'].float()),torch.zeros_like(r['queries'].float()))
ids = sorted(PARTS['test'] if STAGE=='test' else PARTS['train']+PARTS['validation'])
qualities = (95,90,0) if STAGE=='test' else (95,90)
indexes=[]
extraction_start=time.perf_counter()
for begin in range(0,len(ids),250):
    target=OUT/f'{STAGE}-shard-{begin//250:03d}.pt'
    previous=list(MOUNT.rglob(target.name))
    if previous:
        records=torch.load(previous[0],weights_only=True)
    else:
        records=[]
        for i in ids[begin:begin+250]:
            with Image.open(root/'train2017'/f'{i:012d}.jpg') as f:
                rgb=f.convert('RGB')
            for quality in qualities:
                rec=view(rgb,quality)
                rec.update(source_id=i,quality=quality)
                records.append(rec)
    assert {(r['source_id'],r['quality']) for r in records} == {(i,q) for i in ids[begin:begin+250] for q in qualities}
    for r in records:
        assert all(torch.isfinite(r[k]).all() for k in ('queries','text','logits','boxes','backbone'))
    if not previous:
        torch.save(records,target)
    actual=previous[0] if previous else target
    indexes.append(dict(file=target.name,bytes=actual.stat().st_size,views=len(records)))
    write_json(f'{STAGE}_extraction.json',dict(gpu=torch.cuda.get_device_name(0),elapsed_seconds=time.perf_counter()-extraction_start,shards=indexes))
    print(STAGE,begin+len(records)//len(qualities),'/',len(ids),flush=True)
write_json(f'{STAGE}_extraction.json',dict(gpu=torch.cuda.get_device_name(0),total_seconds=time.perf_counter()-started,
           extraction_seconds=time.perf_counter()-extraction_start,shards=indexes,peak_gpu_bytes=torch.cuda.max_memory_allocated()))
