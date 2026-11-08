# Measured B prototype resources

Full training uses one Tesla T4 per private job. Times below include training and export, exclude queueing. Peaks are cumulative allocator measurements for each training job.

| Arm | Hours | Peak allocated GiB | Peak reserved GiB | Usable/selected augmented GT |
|---|---:|---:|---:|---:|
| baseline | 1.591 | 3.741 | 5.021 | 0/0 |
| generic | 2.393 | 4.866 | 6.229 | 471037/472441 |
| small_thin | 2.453 | 4.866 | 6.229 | 74244/74951 |

baseline effective optimizer: `{"type": "AdamW", "groups": [{"lr": 0.00125, "initial_lr": 0.00125, "weight_decay": 0.0005, "betas": [0.9, 0.999], "momentum": null, "parameters": 88}, {"lr": 0.00125, "initial_lr": 0.00125, "weight_decay": 0.0, "betas": [0.9, 0.999], "momentum": null, "parameters": 81}, {"lr": 0.00125, "initial_lr": 0.00125, "weight_decay": 0.0, "betas": [0.9, 0.999], "momentum": null, "parameters": 87}], "warmup_bias_lr": 0.0}`.

baseline convergence diagnostic: best recorded source-selection mAP50:95=0.15964; first CSV maximum at epoch48; improvement in best score over epochs41-50 versus epochs1-40=0.00226. Training stopped at the fixed50-epoch prototype budget; convergence is not established.

generic: no-positive skips=1375; zero-weight skips=29; usable fraction=0.99703; empty-selection batches=0; usable class counts [D00,D10,D20,D40]=[135425, 23898, 132860, 178854].
Unweighted epoch means of auxiliary loss=0.030775, KL=0.016650, normalized-box L1=0.014125. Per-epoch/per-batch telemetry remains in artifacts.

generic effective optimizer: `{"type": "AdamW", "groups": [{"lr": 0.00125, "initial_lr": 0.00125, "weight_decay": 0.0005, "betas": [0.9, 0.999], "momentum": null, "parameters": 88}, {"lr": 0.00125, "initial_lr": 0.00125, "weight_decay": 0.0, "betas": [0.9, 0.999], "momentum": null, "parameters": 81}, {"lr": 0.00125, "initial_lr": 0.00125, "weight_decay": 0.0, "betas": [0.9, 0.999], "momentum": null, "parameters": 87}], "warmup_bias_lr": 0.0}`.

generic convergence diagnostic: best recorded source-selection mAP50:95=0.15155; first CSV maximum at epoch50; improvement in best score over epochs41-50 versus epochs1-40=0.00324. Training stopped at the fixed50-epoch prototype budget; convergence is not established.

small_thin: no-positive skips=698; zero-weight skips=9; usable fraction=0.99057; empty-selection batches=4613; usable class counts [D00,D10,D20,D40]=[17251, 5855, 1890, 49248].
Unweighted epoch means of auxiliary loss=0.019859, KL=0.009579, normalized-box L1=0.010279. Per-epoch/per-batch telemetry remains in artifacts.

small_thin effective optimizer: `{"type": "AdamW", "groups": [{"lr": 0.00125, "initial_lr": 0.00125, "weight_decay": 0.0005, "betas": [0.9, 0.999], "momentum": null, "parameters": 88}, {"lr": 0.00125, "initial_lr": 0.00125, "weight_decay": 0.0, "betas": [0.9, 0.999], "momentum": null, "parameters": 81}, {"lr": 0.00125, "initial_lr": 0.00125, "weight_decay": 0.0, "betas": [0.9, 0.999], "momentum": null, "parameters": 87}], "warmup_bias_lr": 0.0}`.

small_thin convergence diagnostic: best recorded source-selection mAP50:95=0.15346; first CSV maximum at epoch50; improvement in best score over epochs41-50 versus epochs1-40=0.00377. Training stopped at the fixed50-epoch prototype budget; convergence is not established.

select: 0.045 hours including preparation; peak allocated=0.548GiB, reserved=0.932GiB; workspace before cleanup=1.025GiB.

evaluate: 0.149 hours including preparation; peak allocated=0.540GiB, reserved=0.910GiB; workspace before cleanup=1.095GiB.

Measured full training/export plus selection/evaluation/preparation: 6.631 GPU-session hours. Smoke unit tests, smoke recovery and notebook installation/startup are additional. Original smoke gate estimate9.256h included20% contingency and1h for scoring. Failed smokev1 is a separate implementation overhead recorded in the main log.

Small/thin augmented-instance counts can increase through mosaic. Evaluation support uses original-image geometry and is not comparable to repeated training-instance counts.

Full telemetry validation: finite auxiliary/supervised losses, batch-scaled total-loss reconstruction, exact ramp, complete batch coverage, skip/class-count reconciliation and EMA-update continuity passed. Generic and B per-batch augmented geometry counts identical: True. This count check does not establish pixel-level view equality. Details: `{"generic": {"batches": 25850, "ema_updates": 6828, "counts": {"total": 476690, "visible": 472441, "target": 74951, "selected": 472441, "usable": 471037, "skip_no_positive": 1375, "skip_zero_weight": 29}}, "small_thin": {"batches": 25850, "ema_updates": 6828, "counts": {"total": 476690, "visible": 472441, "target": 74951, "selected": 74951, "usable": 74244, "skip_no_positive": 698, "skip_zero_weight": 9}}}`.

Original-image640 geometry populations (unique annotations; class orderD00,D10,D20,D40): `{"train": {"images": 8264, "class_order": ["D00", "D10", "D20", "D40"], "counts_by_class": {"all": [2007, 345, 1673, 2691], "small": [36, 3, 0, 349], "thin": [5, 5, 0, 23], "small_or_thin": [36, 7, 0, 349], "B_eligible": [36, 7, 0, 349]}}, "selection": {"images": 1034, "class_order": ["D00", "D10", "D20", "D40"], "counts_by_class": {"all": [222, 70, 212, 298], "small": [6, 1, 0, 36], "thin": [1, 1, 0, 3], "small_or_thin": [6, 1, 0, 36], "B_eligible": [6, 1, 0, 36]}}, "source_audit": {"images": 1033, "class_order": ["D00", "D10", "D20", "D40"], "counts_by_class": {"all": [288, 52, 231, 358], "small": [7, 0, 0, 63], "thin": [0, 0, 0, 4], "small_or_thin": [7, 0, 0, 63], "B_eligible": [7, 0, 0, 63]}}, "unseen": {"images": 4805, "class_order": ["D00", "D10", "D20", "D40"], "counts_by_class": {"all": [6750, 3295, 834, 135], "small": [290, 86, 2, 83], "thin": [45, 127, 0, 19], "small_or_thin": [293, 150, 2, 83], "B_eligible": [293, 150, 2, 83]}}}`. B_eligible is the small/thin union with short side>=8px. These original supports differ from the repeated augmented training counts above; mosaic can move originally larger objects into the focused mask.

Execution fault: duplicate local controllers submitted source selection twice. Version1 added 0.042 measured T4-session hours; version2 was retained. Their frozen configurations match exactly. Each detector was trained once. A tested OS-held file lock now prevents duplicate executors. Including this measured redundant stage: 6.672 hours, plus smoke/install/startup overhead.

Account-level quota cross-check: used GPU quota increased by 6.855 hours between saved before/after snapshots; this is distinct from per-job process profiling. Final account usage=8:38:21.470000 of30h; reserved=0:00:00; paid scaling enabled=False. Queue time is reported separately in the main log.