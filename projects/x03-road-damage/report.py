"""Summarise completed local Kaggle artifacts without manufacturing results."""
import json
import csv
import statistics
from verify_results import verify
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def report():
    verify()
    summary_path=next((ROOT/'artifacts/evaluate').rglob('summary.json'))
    training_path=next((ROOT/'artifacts/train').rglob('training-complete.json'))
    env_path=next((ROOT/'artifacts/train').rglob('environment.json'))
    summary=json.loads(summary_path.read_text()); train=json.loads(training_path.read_text()); env=json.loads(env_path.read_text())
    threshold=json.loads(next((ROOT/'artifacts/evaluate').rglob('threshold.json')).read_text())
    assignment=json.loads(next((ROOT/'artifacts/evaluate').rglob('A-assignment.json')).read_text())
    audit=json.loads((ROOT/'runs/audit.json').read_text())
    inventory=json.loads((ROOT/'runs/manifest-validation.json').read_text())
    train_images=sum(v.get('train',0) for v in audit['counts'].values())
    training_small=sum(v['small_or_thin'] for k,v in inventory['statistics'].items() if k.endswith('/train'))
    audit_small=sum(v['small_or_thin'] for k,v in inventory['statistics'].items() if k.endswith('/source_audit'))
    pothole_small=sum(v['small_or_thin_classes'][3] for k,v in inventory['statistics'].items() if k.endswith('/train'))
    hours=train['seconds']/3600
    timing=json.loads(next((ROOT/'artifacts/train').rglob('timing.json')).read_text())
    epochs={}
    for row in timing['epochs']: epochs.setdefault(row['epoch'],row)
    steady=[r['seconds'] for e,r in epochs.items() if e>3]
    peak_alloc=max(r['allocated'] for r in timing['epochs'])/1024**3
    peak_reserved=max(r['reserved'] for r in timing['epochs'])/1024**3
    scaled_core=lambda multiplier:1.3*((44+28*1.7+15)*hours*multiplier+10)
    csv_path=next((ROOT/'artifacts/train').rglob('results.csv'))
    with open(csv_path,newline='') as f: history=[{k.strip():v for k,v in r.items()} for r in csv.DictReader(f)]
    metric='metrics/mAP50-95(B)'
    ap_history=[float(r[metric]) for r in history if metric in r]
    late_gain=max(ap_history[-10:])-max(ap_history[:-10]) if len(ap_history)>10 else None
    lines=['# Kaggle baseline pilot results','',
           'These are one-seed development results. The US is a simulated unseen development country; Japan was not accessed.', '',
           f"GPU: {env['gpu']}; VRAM {env['vram_bytes']/1024**3:.1f} GiB. Model: {train['model']}; batch {train['batch']}; 50 epochs; seed 42; Ultralytics 8.4.192.",
           f'Measured training wall time (including validation/checkpoint work): {hours:.2f} hours. Setup, preparation and evaluation are additional.', '',
           f'Peak PyTorch allocated/reserved GPU memory: {peak_alloc:.2f}/{peak_reserved:.2f} GiB. Median epoch wall time after the first three epochs: {statistics.median(steady):.1f} seconds (includes validation/checkpoint work). These measurements belong to this T4 configuration; they are not RTX4050 benchmarks.', '',
           f"Operating confidence threshold: {threshold['value']:.4f}, selected only on source-selection data using {threshold['rule']}. AP/precision/recall below use 0–1 units; FP/image is a count rate.", '',
           'An operational miss means no same-class prediction above that threshold matches the label at IoU>=0.5. This includes low-confidence detections, wrong classes and insufficient localisation, not only complete absence of a visible box.', '',
           f"Effective split counts: `{json.dumps(audit['counts'])}`. Quarantined records: {len(audit['quarantine'])}; see runs/audit.json for reasons and overlap exclusions. Out-of-scope classes are ignored within otherwise retained images.", '',
           f'The inventory found {training_small} small/thin training labels and {audit_small} source-audit labels under the frozen definitions. Of the training subgroup, {pothole_small} are potholes: aggregate small/thin performance does not establish small-crack performance. US has no empty-label images, whereas source splits contain many. Class/prevalence differences confound raw country gaps; sparse geometry results require caution. Inventory and class composition are recorded in runs/manifest-validation.json.', '',
           '| Country / role | mAP50 | mAP50:95 | Recall | Small/thin recall | Precision | FP/image |',
           '|---|---:|---:|---:|---:|---:|---:|']
    def num(v): return 'undefined' if v is None else f'{v:.4f}'
    for c in ['India','Czech','United_States']:
        m=summary[c]
        vals=[m['AP']['map50'],m['AP']['map50_95'],m['geometry']['all']['recall'],m['geometry']['small_or_thin']['recall'],m['precision'],m['fp_per_image']]
        lines.append('| '+c+' | '+' | '.join(num(x) for x in vals)+' |')
    gap=summary['source_macro_AP']['map50_95']-summary['United_States']['AP']['map50_95']
    lines+=['',f'Source-macro minus US mAP50:95: {gap*100:.2f} percentage points. This is descriptive; it does not identify a causal country effect.', '',
            '## Diagnostics and next decisions','',
            '- A: inspect A-assignment.json for geometry-specific zero-positive rates and supervision mass. These do not demonstrate the proposed replacement improves anything.',
            '- B: compare scale320 and 640 subgroup recall, including the B_eligible population. Scale sensitivity supports investigation, not intervention efficacy.',
            '- C: the table below measures target availability and the raw weak map. A learned head is still required to test whether features add information.', '',
            'A assignment summaries: `'+json.dumps(assignment['summary'])+'`.', '',
            '| Country | Missed-centre positive cells | Positive images | Cell prevalence | Raw weak-map AP | Collisions |',
            '|---|---:|---:|---:|---:|---:|']
    for c in ['India','Czech','United_States']:
        m=summary[c]['C']; lines.append(f"| {c} | {m['positive_cells']} | {m['positive_images']} | {num(m['prevalence'])} | {num(m['weak_map_average_precision'])} | {m['collisions']} |")
    lines+=['', 'Small/thin share of all operational misses: '+', '.join(f"{c}: {num(summary[c]['small_or_thin_share_of_misses'])}" for c in ['India','Czech','United_States'])+'. This describes concentration of errors at the chosen operating point; it does not establish their cause.']
    lines+=['','## Resource projection and limitations','',
            f'Source-selection best-mAP improvement in the last ten epochs versus all preceding epochs: {num(late_gain)}. Continued improvement can make the fixed-budget baseline inconclusive; this is a diagnostic, not a convergence proof.',
            f'Illustrative core-grid projection: 44 ordinary +28 extra-view runs; assumed B multiplier1.7; development15 ordinary equivalents; C10 hours; contingency30%. At this pilot data size this gives {scaled_core(1):.0f} hours. Scaling to the original-count average final-fold training size gives about {scaled_core(13569.15/train_images):.0f} hours, with an image-count range of about {scaled_core(10738/train_images):.0f}–{scaled_core(16112/train_images):.0f} hours. These are assumptions: B is unbenchmarked, final audit counts differ and convergence may require more epochs.',
            f'This pilot fits {train_images} images. Original-count final folds would fit about 10,738–16,112 images at a 70% source split, before auditing. Linear image-count scaling alone would multiply the measured ordinary-run time by {10738/train_images:.2f}–{16112/train_images:.2f}; this is an assumption, not a throughput measurement.',
            '', 'No deployment adequacy threshold was supplied. A high or low metric alone does not establish that all three interventions are necessary. Review learning curves, sparse subgroup support, annotation completeness and visual examples before choosing research directions.',
            '', 'Example overlays are saved under artifacts/evaluate/results/: green ground-truth boxes were matched, red ground-truth boxes were missed, and cyan boxes are detector predictions above the frozen operating threshold. Examples use a fixed hash sample, so they do not estimate the frequency of individual error types.',
            '', 'Caution: one seed; one unseen development country; imperfect sequence metadata; conservative duplicate grouping; fixed 50-epoch budget. Bootstrap intervals describe image/group sampling, not country or training-seed uncertainty. Raw-map AP uses a stepwise tie-aware definition. Models and predictions are retained in ignored local artifacts; concise summary JSON is retained under runs.', '']
    (ROOT/'pilot-report.md').write_text('\n'.join(lines),encoding='utf-8')
    (ROOT/'runs/summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')

if __name__=='__main__': report()
