# B prototype comparison

**One-seed development outcome: no improvement under this configuration.** This is a point-estimate screen, not evidence across seeds/countries. Japan was untouched.

All arms: fresh identical COCO initialization, YOLO11s640, seed42,50epochs, pinned Ultralytics8.4.192. Checkpoints and confidence thresholds were selected using source data and frozen together before evaluation.

| Arm | Country | mAP50 | mAP50:95 | Recall | Small/thin recall | Precision | FP/image |
|---|---|---:|---:|---:|---:|---:|---:|
| baseline | India | 0.3558 | 0.1471 | 0.2675 | 0.2258 | 0.7893 | 0.0680 |
| baseline | Czech | 0.2333 | 0.0840 | 0.1302 | 0.0000 | 0.5957 | 0.0671 |
| baseline | United_States | 0.1646 | 0.0630 | 0.1786 | 0.0492 | 0.5893 | 0.2853 |
| generic | India | 0.3341 | 0.1388 | 0.2073 | 0.1774 | 0.7668 | 0.0600 |
| generic | Czech | 0.2105 | 0.0771 | 0.1209 | 0.0000 | 0.6341 | 0.0530 |
| generic | United_States | 0.1300 | 0.0477 | 0.0907 | 0.0170 | 0.5761 | 0.1530 |
| small_thin | India | 0.3226 | 0.1334 | 0.2367 | 0.2258 | 0.7613 | 0.0707 |
| small_thin | Czech | 0.2489 | 0.0888 | 0.1674 | 0.0000 | 0.6545 | 0.0671 |
| small_thin | United_States | 0.1599 | 0.0615 | 0.1751 | 0.0227 | 0.5513 | 0.3267 |

## Primary comparison

US B minus generic small/thin recall: 0.0057. Recall condition passes: True; FP/image guard passes: False.
Paired image/group bootstrap95% intervals for B minus generic (one training seed): `{"overall_recall_difference": [0.07856072342015474, 0.09013378182947585], "target_recall_difference": [-0.0037599314922466846, 0.015815019762845845], "fp_per_image_difference": [0.15806386320158852, 0.19005146236955733]}`.

US B minus fresh baseline small/thin recall: -0.0265; FP/image difference: 0.0414.
US overall detection changes (B minus comparator): mAP50:95 +0.0138 versus generic and -0.0015 versus baseline; overall recall +0.0844 versus generic and -0.0035 versus baseline.
At the shared baseline threshold, US small/thin recall is B=0.0189, generic=0.0170, baseline=0.0492.


The compact JSON includes all per-country comparisons, per-class support, and results at the common baseline threshold. Full per-image metrics and predictions remain in local ignored artifacts.

## Common confidence threshold

All arms below use the fresh baseline threshold, exposing changes caused by confidence selection.

| Arm | Country | Overall recall | Small/thin recall | FP/image |
|---|---|---:|---:|---:|
| baseline | India | 0.2675 | 0.2258 | 0.0680 |
| baseline | Czech | 0.1302 | 0.0000 | 0.0671 |
| baseline | United_States | 0.1786 | 0.0492 | 0.2853 |
| generic | India | 0.2073 | 0.1774 | 0.0600 |
| generic | Czech | 0.1209 | 0.0000 | 0.0530 |
| generic | United_States | 0.0907 | 0.0170 | 0.1530 |
| small_thin | India | 0.2297 | 0.2258 | 0.0667 |
| small_thin | Czech | 0.1442 | 0.0000 | 0.0601 |
| small_thin | United_States | 0.1642 | 0.0189 | 0.2922 |

## Class support and missed damage

| Arm | Country | Class | Matched/all GT | Matched/small-thin GT |
|---|---|---|---:|---:|
| baseline | India | D00 | 25/170 | 0/4 |
| baseline | India | D10 | 0/3 | 0/0 |
| baseline | India | D20 | 92/210 | 0/0 |
| baseline | India | D40 | 74/331 | 14/58 |
| baseline | Czech | D00 | 26/118 | 0/3 |
| baseline | Czech | D10 | 0/49 | 0/0 |
| baseline | Czech | D20 | 2/21 | 0/0 |
| baseline | Czech | D40 | 0/27 | 0/5 |
| baseline | United_States | D00 | 1937/6750 | 25/293 |
| baseline | United_States | D10 | 0/3295 | 0/150 |
| baseline | United_States | D20 | 27/834 | 0/2 |
| baseline | United_States | D40 | 3/135 | 1/83 |
| generic | India | D00 | 13/170 | 0/4 |
| generic | India | D10 | 0/3 | 0/0 |
| generic | India | D20 | 80/210 | 0/0 |
| generic | India | D40 | 55/331 | 11/58 |
| generic | Czech | D00 | 25/118 | 0/3 |
| generic | Czech | D10 | 0/49 | 0/0 |
| generic | Czech | D20 | 1/21 | 0/0 |
| generic | Czech | D40 | 0/27 | 0/5 |
| generic | United_States | D00 | 970/6750 | 8/293 |
| generic | United_States | D10 | 2/3295 | 0/150 |
| generic | United_States | D20 | 23/834 | 0/2 |
| generic | United_States | D40 | 4/135 | 1/83 |
| small_thin | India | D00 | 15/170 | 0/4 |
| small_thin | India | D10 | 0/3 | 0/0 |
| small_thin | India | D20 | 92/210 | 0/0 |
| small_thin | India | D40 | 62/331 | 14/58 |
| small_thin | Czech | D00 | 32/118 | 0/3 |
| small_thin | Czech | D10 | 2/49 | 0/0 |
| small_thin | Czech | D20 | 2/21 | 0/0 |
| small_thin | Czech | D40 | 0/27 | 0/5 |
| small_thin | United_States | D00 | 1883/6750 | 11/293 |
| small_thin | United_States | D10 | 1/3295 | 0/150 |
| small_thin | United_States | D20 | 43/834 | 0/2 |
| small_thin | United_States | D40 | 2/135 | 1/83 |

| Arm | Country | Missed objects/image | Damage images with a miss |
|---|---|---:|---:|
| baseline | India | 0.6973 | 0.7718 |
| baseline | Czech | 0.6608 | 0.8629 |
| baseline | United_States | 1.8828 | 0.8986 |
| generic | India | 0.7547 | 0.7988 |
| generic | Czech | 0.6678 | 0.8790 |
| generic | United_States | 2.0843 | 0.9521 |
| small_thin | India | 0.7267 | 0.7628 |
| small_thin | Czech | 0.6325 | 0.8710 |
| small_thin | United_States | 1.8907 | 0.9043 |

US B versus generic matched-GT transitions: `{"all": {"missed_by_both": 8937, "gained": 1078, "retained": 851, "lost": 148}, "small_or_thin": {"missed_by_both": 514, "retained": 7, "gained": 5, "lost": 2}, "byclass": {"0": {"missed_by_both": 4728, "gained": 1052, "retained": 831, "lost": 139}, "1": {"missed_by_both": 3292, "lost": 2, "gained": 1}, "2": {"missed_by_both": 786, "gained": 25, "retained": 18, "lost": 5}, "3": {"missed_by_both": 131, "lost": 2, "retained": 2}}, "fp_images": {"higher": 913, "equal": 3644, "lower": 248}}`. Gained/lost refer to the same ground-truth objects at IoU>=0.50 and each arm's source-selected threshold.

## Resources and interpretation

- baseline: 1.59 hours; peak reserved5.02GiB; threshold0.3872.
- generic: 2.39 hours; peak reserved6.23GiB; threshold0.3872.
  Augmented GT instances selected472441; usable471037. These are repeated/augmented training instances, not unique original annotations.
- small_thin: 2.45 hours; peak reserved6.23GiB; threshold0.3721.
  Augmented GT instances selected74951; usable74244. These are repeated/augmented training instances, not unique original annotations.

Execution overhead: source selection was submitted twice by duplicate local controllers; the redundant job used 0.042 measured T4-session hours and produced an identical frozen configuration. All detector training arms ran once. A process lock fixed the duplication.

Total measured full-training/export time: 6.44GPU-session hours. Smoke, selection and evaluation are additional. Queue time is not GPU training time.

All54 hash-selected example overlays are included in evaluation artifacts: green=matched GT, red=missed GT, cyan=predictions at the arm-specific source-selected threshold. They are deterministic examples, not a representative error-rate estimate.

Loss and teacher/BN policies match between generic and focused arms; their selection mask differs. The supervised baseline uses fewer passes, so baseline comparisons are equal training exposure, not equal compute. Without count-matched random consistency, geometry-specific causation is unresolved.

Small/thin source annotations are dominated by potholes. Box geometry is not physical crack width. US outcomes are development evidence; do not tune on these results and then present the same US set as confirmation. One lambda/ramp and one seed cannot disprove consistency methods generally. Confidence intervals represent paired image/group sampling, not training-seed/country variation. Stronger baseline recipes, count-matched/random and resolution controls, additional seeds and countries belong to the main study.
