# Kaggle baseline pilot results

These are one-seed development results. The US is a simulated unseen development country; Japan was not accessed.

GPU: Tesla T4; VRAM 14.6 GiB. Model: yolo11s.pt; batch 16; 50 epochs; seed 42; Ultralytics 8.4.192.
Measured training wall time (including validation/checkpoint work): 1.53 hours. Setup, preparation and evaluation are additional.

Peak PyTorch allocated/reserved GPU memory: 3.74/5.02 GiB. Median epoch wall time after the first three epochs: 109.1 seconds (includes validation/checkpoint work). These measurements belong to this T4 configuration; they are not RTX4050 benchmarks.

Operating confidence threshold: 0.3872, selected only on source-selection data using precision>=0.70, maximum recall, ties higher threshold. AP/precision/recall below use 0–1 units; FP/image is a count rate.

An operational miss means no same-class prediction above that threshold matches the label at IoU>=0.5. This includes low-confidence detections, wrong classes and insufficient localisation, not only complete absence of a visible box.

Effective split counts: `{"India": {"source_audit": 750, "selection": 751, "train": 6001, "excluded_overlap": 203}, "Czech": {"selection": 283, "train": 2263, "source_audit": 283}, "United_States": {"unseen": 4805}}`. Quarantined records: 1; see runs/audit.json for reasons and overlap exclusions. Out-of-scope classes are ignored within otherwise retained images.

The inventory found 392 small/thin training labels and 70 source-audit labels under the frozen definitions. Of the training subgroup, 349 are potholes: aggregate small/thin performance does not establish small-crack performance. US has no empty-label images, whereas source splits contain many. Class/prevalence differences confound raw country gaps; sparse geometry results require caution. Inventory and class composition are recorded in runs/manifest-validation.json.

| Country / role | mAP50 | mAP50:95 | Recall | Small/thin recall | Precision | FP/image |
|---|---:|---:|---:|---:|---:|---:|
| India | 0.3558 | 0.1471 | 0.2675 | 0.2258 | 0.7893 | 0.0680 |
| Czech | 0.2333 | 0.0840 | 0.1302 | 0.0000 | 0.5957 | 0.0671 |
| United_States | 0.1646 | 0.0630 | 0.1786 | 0.0474 | 0.5893 | 0.2853 |

Source-macro minus US mAP50:95: 5.25 percentage points. This is descriptive; it does not identify a causal country effect.

## Diagnostics and next decisions

- A: inspect A-assignment.json for geometry-specific zero-positive rates and supervision mass. These do not demonstrate the proposed replacement improves anything.
- B: compare scale320 and 640 subgroup recall, including the B_eligible population. Scale sensitivity supports investigation, not intervention efficacy.
- C: the table below measures target availability and the raw weak map. A learned head is still required to test whether features add information.

A assignment summaries: `{"all": {"boxes": 188, "zero_positive_fraction": 0.0, "mean_positives": 10.0, "mean_score_mass": 4.483171466183155}, "small_or_thin": {"boxes": 3, "zero_positive_fraction": 0.0, "mean_positives": 10.0, "mean_score_mass": 3.1373070081075034}, "other": {"boxes": 185, "zero_positive_fraction": 0.0, "mean_positives": 10.0, "mean_score_mass": 4.50499629523303}}`.

| Country | Missed-centre positive cells | Positive images | Cell prevalence | Raw weak-map AP | Collisions |
|---|---:|---:|---:|---:|---:|
| India | 48 | 35 | 0.0000 | 0.0145 | 0 |
| Czech | 9 | 9 | 0.0000 | 0.0062 | 0 |
| United_States | 523 | 464 | 0.0001 | 0.0014 | 0 |

Small/thin share of all operational misses: India: 0.0918, Czech: 0.0481, United_States: 0.0578. This describes concentration of errors at the chosen operating point; it does not establish their cause.

## Resource projection and limitations

Source-selection best-mAP improvement in the last ten epochs versus all preceding epochs: 0.0023. Continued improvement can make the fixed-budget baseline inconclusive; this is a diagnostic, not a convergence proof.
Illustrative core-grid projection: 44 ordinary +28 extra-view runs; assumed B multiplier1.7; development15 ordinary equivalents; C10 hours; contingency30%. At this pilot data size this gives 225 hours. Scaling to the original-count average final-fold training size gives about 361 hours, with an image-count range of about 288–426 hours. These are assumptions: B is unbenchmarked, final audit counts differ and convergence may require more epochs.
This pilot fits 8264 images. Original-count final folds would fit about 10,738–16,112 images at a 70% source split, before auditing. Linear image-count scaling alone would multiply the measured ordinary-run time by 1.30–1.95; this is an assumption, not a throughput measurement.

No deployment adequacy threshold was supplied. A high or low metric alone does not establish that all three interventions are necessary. Review learning curves, sparse subgroup support, annotation completeness and visual examples before choosing research directions.

Example overlays are saved under artifacts/evaluate/results/: green ground-truth boxes were matched, red ground-truth boxes were missed, and cyan boxes are detector predictions above the frozen operating threshold. Examples use a fixed hash sample, so they do not estimate the frequency of individual error types.

Caution: one seed; one unseen development country; imperfect sequence metadata; conservative duplicate grouping; fixed 50-epoch budget. Bootstrap intervals describe image/group sampling, not country or training-seed uncertainty. Raw-map AP uses a stepwise tie-aware definition. Models and predictions are retained in ignored local artifacts; concise summary JSON is retained under runs.
