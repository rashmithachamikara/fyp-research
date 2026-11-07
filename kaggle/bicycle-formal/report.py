import json
import shutil
from pathlib import Path

mount=Path('/kaggle/input')
out=Path('/kaggle/working')
def find(name):
    return next(mount.rglob(name))
def read(name):
    return json.loads(find(name).read_text())
r=read('formal_result.json')
m=read('absolute_metrics.json')
p=read('probe_report.json')
a,b=read('trainval_extraction.json'),read('test_extraction.json')
training=read('frozen_training.json')
minutes=(a['extraction_seconds']+b['extraction_seconds'])/60
storage=sum(s['bytes'] for stage in (a,b) for s in stage['shards'])/1e9
lines=[]
for name in ('untouched','A','B'):
    matched=next(x for x in m if x['model']==name and x['condition']=='matched')
    reversed=next(x for x in m if x['model']==name and x['condition']=='reversed')
    original=next(x for x in m if x['model']==name and x['condition']=='original')
    lines.append(f"| {name} | {matched['miss_rate_percent']:.2f}% | {reversed['miss_rate_percent']:.2f}% | {original['miss_rate_percent']:.2f}% | {matched['false_alarms_per_negative']:.3f} / {reversed['false_alarms_per_negative']:.3f} |")
brief=f'''# Bicycle JPEG pilot - supervisor brief

**Recommendation - {r['decision'].lower()}.** The extra bicycle miss-rate increase from correlating JPEG quality with bicycle presence was **{r['mean_delta_pp']:+.3f} percentage points**, with a 95% paired source-bootstrap interval of **{r['delta_ci95'][0]:+.3f} to {r['delta_ci95'][1]:+.3f}**. Its upper bound is below the prespecified 3-point decision margin under this training recipe.

The frozen Grounding DINO-T scoring adapter was trained on 3,400 images, calibrated on 800, and evaluated once on 2,000 held-out sources containing {r['test_bicycle_instances']:,} annotated bicycles. Head A used a 90/10 association between bicycle presence and Q95/Q90. Head B used 50/50 within each class. Both saw identical sources and total quality frequencies. Three paired seeds, four epochs, and the shared validation-selected threshold {r['threshold']} were frozen before test extraction.

| Model | Matched misses | Reversed misses | Original-JPEG misses | False alarms per negative, matched / reversed |
|---|---:|---:|---:|---:|
{chr(10).join(lines)}

A and B values average three seeds. The seed-specific extra miss increases were +0.346, -0.148, and 0.000 points. Intervals use 20,000 paired source resamples, conditional on these three trained seeds.

**Interpretation limitation.** Both adapted heads generated approximately 10-11 false alarms per bicycle-free image at the shared threshold, versus approximately 0.03 for the untouched detector. Their lower miss rates therefore came with substantial deterioration in false alarms. The result supports holding the mitigation project under this recipe. It provides a limited test of shortcut reliance in a poorly calibrated operating regime. A revised training or calibration study would require a new protocol and fresh evaluation sources.

The cue remained readable on validation data. Probe accuracies were {100*p['backbone']['accuracy']:.1f}% for backbone features, {100*p['decoder']['accuracy']:.1f}% for pooled decoder features, and {100*p['matched']['accuracy']:.1f}% for matched bicycle queries. Feature readability and cue reliance answer different questions.

**Resources and audit.** Extraction used {minutes:.1f} T4 minutes and {storage:.2f} GB of saved feature shards. CPU probes and training took {training['total_seconds']/60:.1f} minutes, and final evaluation took {r['evaluation_seconds']/60:.1f} minutes, excluding platform startup. Model weights, images, heads and caches remain on Kaggle. The companion figure reports absolute errors and the primary interval; `error_types.csv` reports every model/seed's new-miss categories. The manifest and head hashes are retained in the run outputs.

[Train/validation extraction](https://www.kaggle.com/code/rashmithachamikara/bicycle-formal-trainval) | [Probes and training](https://www.kaggle.com/code/rashmithachamikara/bicycle-formal-training) | [Test extraction](https://www.kaggle.com/code/rashmithachamikara/bicycle-formal-test) | [Frozen evaluation](https://www.kaggle.com/code/rashmithachamikara/bicycle-formal-evaluation)
'''
(out/'supervisor-brief.md').write_text(brief)
for name in ('formal_results.png','formal_results.svg','error_types.csv'):
    shutil.copyfile(find(name),out/name)
print(brief)
