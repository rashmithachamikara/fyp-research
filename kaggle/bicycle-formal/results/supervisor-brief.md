# Bicycle JPEG pilot - supervisor brief

**Recommendation - hold mitigation project.** The extra bicycle miss-rate increase from correlating JPEG quality with bicycle presence was **+0.066 percentage points**, with a 95% paired source-bootstrap interval of **-0.148 to +0.300**. Its upper bound is below the prespecified 3-point decision margin under this training recipe.

The frozen Grounding DINO-T scoring adapter was trained on 3,400 images, calibrated on 800, and evaluated once on 2,000 held-out sources containing 2,024 annotated bicycles. Head A used a 90/10 association between bicycle presence and Q95/Q90. Head B used 50/50 within each class. Both saw identical sources and total quality frequencies. Three paired seeds, four epochs, and the shared validation-selected threshold 0.35 were frozen before test extraction.

| Model | Matched misses | Reversed misses | Original-JPEG misses | False alarms per negative, matched / reversed |
|---|---:|---:|---:|---:|
| untouched | 43.53% | 45.16% | 43.43% | 0.037 / 0.032 |
| A | 4.69% | 4.91% | 4.59% | 10.852 / 10.177 |
| B | 4.50% | 4.64% | 4.51% | 11.259 / 10.212 |

A and B values average three seeds. The seed-specific extra miss increases were +0.346, -0.148, and 0.000 points. Intervals use 20,000 paired source resamples, conditional on these three trained seeds.

**Interpretation limitation.** Both adapted heads generated approximately 10-11 false alarms per bicycle-free image at the shared threshold, versus approximately 0.03 for the untouched detector. Their lower miss rates therefore came with substantial deterioration in false alarms. The result supports holding the mitigation project under this recipe. It provides a limited test of shortcut reliance in a poorly calibrated operating regime. A revised training or calibration study would require a new protocol and fresh evaluation sources.

The cue remained readable on validation data. Probe accuracies were 75.5% for backbone features, 70.6% for pooled decoder features, and 61.6% for matched bicycle queries. Feature readability and cue reliance answer different questions.

**Resources and audit.** Extraction used 129.3 T4 minutes and 7.02 GB of saved feature shards. CPU probes and training took 4.3 minutes, and final evaluation took 1.8 minutes, excluding platform startup. Model weights, images, heads and caches remain on Kaggle. The companion figure reports absolute errors and the primary interval; `error_types.csv` reports every model/seed's new-miss categories. The manifest and head hashes are retained in the run outputs.

[Train/validation extraction](https://www.kaggle.com/code/rashmithachamikara/bicycle-formal-trainval) | [Probes and training](https://www.kaggle.com/code/rashmithachamikara/bicycle-formal-training) | [Test extraction](https://www.kaggle.com/code/rashmithachamikara/bicycle-formal-test) | [Frozen evaluation](https://www.kaggle.com/code/rashmithachamikara/bicycle-formal-evaluation)
