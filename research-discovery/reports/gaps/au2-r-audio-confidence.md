[← Research candidates](../research-candidates.md)

# Reliable confidence in compact audio classifiers

**ID:** AU2-R · **Area:** Audio / uncertainty / efficient ML · **Status:** Refine novelty

**Evidence reviewed:** 27 October 2026

## 1. Problem

An audio classifier can recognise scenes such as a bus, airport or park on one microphone, then make confident mistakes on another. Compressing the model may further change how well confidence reflects correctness.

The intended users are developers of context-aware audio tools. The project would evaluate benchmark reliability; it would not establish field safety or microcontroller performance.

## 2. Research gap and question

**Established:** device-robust audio classification, prediction calibration and quantisation already exist.

**Gap to investigate:** whether a training objective that preserves confidence ordering can improve selective prediction on unseen microphones after compression, under a fixed model budget.

**Research question:** Can confidence-preserving training and compression reduce error among accepted predictions on unseen recording devices without materially reducing scene-classification accuracy?

**Novelty status:** plausible, but insufficiently differentiated. Combining temperature scaling with a compact classifier is not the proposed contribution.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [DCASE 2025 task paper](https://arxiv.org/html/2505.01747v1) | Compact, data-efficient, device-aware classification | Confidence ordering and selective risk under matched budgets | Full text |
| [Quantisation and calibration report, 2021](https://dcase.community/documents/challenge2021/technical_reports/DCASE2021_Byttebier_85_t1.pdf) | Small models, quantisation and score calibration | Reliability on held-out microphones, rather than calibration plus quantisation alone | Full text |
| [Reject-option report, 2019](https://dcase.community/documents/challenge2019/technical_reports/DCASE2019_Lehner_103.pdf) | Unknown scene-class rejection | Unknown microphones for the same known scene classes | Full text |
| [Heated-up softmax and spectrum correction, 2020](https://research.samsung.com/research-papers/Acoustic-Scene-Classification-for-Mismatched-Recording-Devices-Using-Heated-Up-Softmax-and-Spectrum-Correction) | Confidence calibration for microphone mismatch | A stronger contribution than changing the temperature | Authors' abstract |
| [Confidence-aware distillation report, 2025](https://dcase.community/documents/challenge2025/technical_reports/DCASE2023_HAN_96_t1.pdf) | Confidence-weighted teachers and a compact student | Isolate reliability changes from accuracy and teacher-quality changes | Full text |

These comparisons support the question; they do not establish originality.

The confidence-aware distillation report changes several factors between systems. Its results do not isolate a causal effect of confidence weighting.

## 4. Proposed approach

Use a compact scene classifier as the shared baseline. Investigate confidence-consistency training, a small calibration model and confidence-preserving quantisation.

The research contribution would be the objectives and controlled experiments. A clip-classification application would demonstrate the findings.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary data | [TAU Urban Acoustic Scenes 2022 Mobile](https://zenodo.org/records/6337421) |
| Verified access | Documentation, licence, metadata and official split files downloaded |
| Available splits | 34,900 training clips in the 25% list; 29,680 test clips |
| Leakage check | No overlapping filenames or location identifiers between those lists |
| Licence | Custom experimental, non-commercial terms; preserve notices and attribution |
| Compute | Small CNN; CPU development and optional modest-GPU training |
| Fallback | Official 5% list: 6,980 training clips |
| Unverified | Audio decoding, training time, peak RAM and quantised-kernel support |

Budget approximately 50–100 GB for bounded audio/features/outputs; this is an estimate. Several TAU editions reuse recordings and are not independent datasets. Simulated microphones limit claims about arbitrary real hardware.

The inspected metadata contains 230,350 clips, ten scene classes and nine device IDs. Training uses A, B, C and S1–S3; testing also includes S4–S6. These are available-list counts before internal holdouts. The archive listing is approximately 27.5 GB; waveforms were not downloaded or decoded. Proprietary device impulse responses are unavailable and must not be a dependency.

The [official loader](https://github.com/CPJKU/dcase2025_task1_baseline/blob/main/dataset/dcase25.py) identifies the split files. The downloaded [licence](../../metadata/source-checks/TAU-LICENSE.txt) does not establish permission for commercial services or unrestricted redistribution.

**Prototype:** a local clip classifier showing scene, confidence and accept/abstain behaviour. Workstation measurements would not establish microcontroller speed or energy savings.

## 6. Three-member contributions

| Member | Research question | Method investigation | Assessable result |
|---|---|---|---|
| A: learning | Does device-balanced confidence-consistency training improve transfer? | Confidence agreement across paired training recordings | Compare pairing, balancing and ordinary classification losses |
| B: uncertainty | Does partially shared calibration transfer better with scarce labels? | Regularised confidence head with shared/device-specific parameters | Compare pooling strategies, calibration and selective error |
| C: compression | Can quantisation preserve confidence ranking? | Confidence-consistency objective during quantisation-aware training | Compare floating point, ordinary quantisation and confidence-aware quantisation |

All three contributions address the same reliability problem and may share data, models and the experimental pipeline. Each member needs attributable method development and experimental evidence; separate projects or papers are not required.

## 7. Evaluation

- **Primary metric:** worst unseen-device area under the risk–coverage curve; lower is better.
- **Secondary metrics:** macro accuracy, NLL, Brier score, calibration error and risk at fixed coverage.
- **Baselines:** MFCC plus logistic regression/SVM; compact DCASE classifier; ordinary calibration and quantisation.
- **Split:** preserve the official final test. Create location/capture-disjoint training, selection and calibration subsets internally.
- **Ablations:** pairing, device balancing, calibration sharing and quantisation consistency.
- **Uncertainty:** five headline seeds and confidence intervals grouped by original location/capture.
- **Useful negative result:** identify where accuracy, confidence and compression disagree.

The compact neural system targets 128,000 parameter bytes and 30 million model MACs per one-second input, including calibration components. These are design targets, not measured results.

The official baseline reports 61,148 parameters and 29.42 million MACs; these are published figures. Report feature extraction, runtime memory and total stored models separately. Large frozen encoders count toward the full inference system; they cannot be hidden outside the compact-model budget.

Match training data, augmentation, seeds and model budgets across comparisons. Withhold validation locations/captures across all devices and subsegments; use source-device holdouts to simulate unseen-device validation. Never tune calibration on S4–S6 test labels. Start with three development seeds and use five for headline results.

## 8. Score and next decision

**Overall: 77.3/100.** The required novelty rating is 4/5; this candidate has 3/5 and does not qualify.

### Weighted rubric

Scoring updated: **28 October 2026**. The nine weights total **98**; weighted points below are out of 98 and the total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---:|---:|---:|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Medium-low: precise question, but novelty beyond existing calibration, distillation and quantisation is not yet strong |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | High: source licence and metadata inspected; simulated devices and reused recordings limit external validity |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: small core, but audio learning and runtime need a pilot |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: training objectives, uncertainty fitting and QAT |
| Evaluation/reproducibility | 12 | 5 | 12.0 | Medium-high for design: explicit grouping, metrics and controls; experiments not run |
| Three-member structure | 12 | 4 | 9.6 | Medium: assessable contributions to one shared problem; individual experiment boundaries still need refinement |
| Real-world significance | 9 | 3 | 5.4 | Medium: concrete device mismatch, but no validated end-user impact |
| Compute/storage | 5 | 4 | 4.0 | Medium: bounded small-model design; no measured training cost |
| Prototype | 3 | 4 | 2.4 | Medium-high: local clip analysis fits backend skills |
| **Normalised total / 100** | **98** | | **77.3** | **Does not qualify: novelty is below the required 4/5** |

### Mandatory gates

Pass means a bounded design is supported by current evidence; it is not a completed experimental result. Unknown gates prevent qualification, even when a provisional comparison score is provided.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | official device-mismatch task |
| 2. ML essential | Pass | classifier/confidence learning |
| 3. Train/adapt models | Pass | small CNN, calibration and QAT |
| 4. Existing data accessible | Pass | official archives, licence and split metadata inspected |
| 5. No unavailable human evaluation | Pass | existing scene labels |
| 6. Precise research gap | Pass | bounded reliability question with explicit neighbours; novelty strength assessed separately |
| 7. Beyond application assembly | Pass | objective/calibration/compression experiments |
| 8. Objective evaluation | Pass | device/location splits and risk metrics |
| 9. 6–8 month feasibility | Pass | compact bounded core; timing pilot pending |
| 10. Three connected contributions | Pass | learning, calibration and compression questions |
| 11. No specialised/continuous high-end compute | Pass | small classifier; large teachers optional |
| 12. Manageable responsible use | Pass | documented research licence, local prototype, no person identification |
| 13. Useful negative findings | Pass | reliability/accuracy/compression trade-offs |

**Decision:** discuss and refine; do not commit yet.

**Next decision point:** strengthen the methodological distinction, then reproduce the baseline on the 5% list. Measure wall time and peak RAM and compare floating-point/quantised confidence on a location-disjoint validation set. If the effect is negligible, revise the premise before expanding experiments.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Evidence ledger](../../metadata/evidence-ledger.csv).
