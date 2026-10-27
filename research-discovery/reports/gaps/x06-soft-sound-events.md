[← Research candidates](../research-candidates.md)

# Recovering short, low-consensus sound events from soft labels

**ID:** X06 · **Area:** Audio / sound-event detection · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Low-consensus sounds can disappear when soft labels are thresholded, and temporal smoothing can suppress short events. Existing MAESTRO work already demonstrates benefits from soft labels and rare-event detection; those benefits are not a new contribution.

**Potential stakeholders:** Acoustic-monitoring researchers and sound-event model developers.

## 2. Research gap and question

**Tentative gap:** Investigate duration-aware training and pooling for low-consensus event segments, with explicit handling of classes not annotated in a scene. The release only resolves one-second segments, so it cannot validate sub-second onset precision.

**Research question:** Can duration-aware soft-target learning improve one-to-three-second event detection without trading away probability fidelity or increasing false alarms on annotated negative segments?

**Hypothesis and rival explanation:** A duration-aware objective will reduce short-event suppression beyond ordinary soft BCE at matched backbone size. Rival explanation: apparent gains are just lower thresholds, altered smoothing or treating unannotated classes as negatives.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Training SED with Soft Labels, ICASSP 2023](https://arxiv.org/html/2302.14572v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2302.14572) | Soft/hard targets, CRNN training and previously missed low-consensus classes. | Soft labels and recovery of rare sounds are already demonstrated; isolate duration and annotation-availability effects. | Full text; label construction and training; Sections 2–4 (X06-L1) |
| [Sound Event Detection with Soft Labels: A New Perspective on Evaluation, 2024](https://www.eurasip.org/Proceedings/Eusipco/Eusipco2024/pdfs/0000066.pdf) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.23919%2FEUSIPCO63174.2024.10715239) | Soft precision/recall/F-score and threshold-related evaluation differences. | Use soft metrics alongside hard decisions; do not present threshold optimisation as a learned contribution. | Full PDF; Sections I–IV (X06-L2) |
| [Interactive Dual-Conformer with Scene-Inspired Mask, 2023](https://arxiv.org/abs/2311.14068) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2311.14068) | A strong soft-SED architecture and scene masking. | Compare compact duration-aware learning rather than claiming a scene mask is novel. | Abstract only; HTML not retrieved; Abstract (X06-L3) |
| [DCASE 2024 Task 4, 2024](https://arxiv.org/abs/2406.08056) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2406.08056) | Heterogeneous training data and potentially missing sound labels. | Missing-label handling itself is occupied; the narrow interaction with duration requires differentiation. | Scholarly abstract and official task documentation; Abstract; DCASE task description (X06-L4) |

[Import these 4 literature records](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2302.14572,10.23919%2FEUSIPCO63174.2024.10715239,10.48550%2FarXiv.2311.14068,10.48550%2FarXiv.2406.08056). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Train a compact CRNN on the available soft annotations. Investigate a duration-sensitive loss, temporal pooling that preserves short activity and a validation-only decision rule. Use only documented eligible class/scene labels; never turn an unavailable annotation into a negative.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [MAESTRO Real](https://zenodo.org/records/7244360) and [DCASE 2023 Task 4B](https://dcase.community/challenge2023/task-sound-event-detection-with-soft-labels). |
| Actually checked | Official API, licence, README and 877,169-byte annotation ZIP inspected. The archive has 49 development annotation files, 17 label names and one-second segments; waveforms were not decoded. |
| Data-quality limitation | README duration/class listing does not fully match inspected annotations. One soft value lies outside [0,1] beyond roundoff; locate it and predeclare exclusion/clipping sensitivity before training. |
| Access and licence | Development audio listed as 2,614,126,654 bytes; custom experimental/non-commercial licence. The separate evaluation release must supply labels before it can be used locally; otherwise use grouped development folds. |
| Resources, estimated | CPU feature preparation plus occasional modest GPU; 8–16 GB RAM and 8–20 GB disk. A frozen audio-embedding head is the fallback; no runtime measured. |
| Prototype | Local sound timeline at one-second resolution. No claim to detect physical hazards or give precise event onsets. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: soft objective | Does duration-aware weighting retain low-consensus activity? H: Duration-aware learning preserves low-consensus short activity. | Train a duration-sensitive soft-target loss. | Ordinary soft BCE/MSE; remove duration term. | Soft probability error and recall by duration. |
| B: pooling | Can pooling preserve brief events without excessive alarms? H: Learned pooling improves brief-event recall at matched false positives. | Learn a compact multi-resolution temporal pooling module. | Fixed mean/median pooling; matched receptive field. | Short-event recall versus false-positive segments. |
| C: decisions | Can validation-only calibration improve useful operating points? H: Conditional calibration improves operating points without test tuning. | Train a class/duration-aware decision calibrator. | Fixed/global/class thresholds; remove duration conditioning. | Decision trade-offs without test-threshold tuning. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Macro soft Brier score on eligible one-second class/segments; predeclare short-event recall as the key secondary outcome rather than inventing sub-second ground truth.
- **Split:** Group all segments from an original recording and location/capture together. Use development folds for fitting/selection; no evaluation-waveform adaptation.
- **Baselines and code:** Published CRNN hard-BCE, soft-BCE and soft-MSE models; compact CRNN with [DCASE evaluation tools](https://github.com/fgnt/sed_scores_eval); Dual-Conformer is a stronger reference whose exact training/checkpoints remain unverified.
- **Ablations:** Duration loss, pooling and calibration; fixed time resolution, data, class eligibility and smoothing. Report missing-label masks separately from negative labels.
- **Uncertainty and errors:** Recording-cluster bootstrap and repeated seeds; analyse event duration, polyphony, soft-consensus level and class. Report interval instability for rare classes.
- **Useful result without winning:** Show whether short-event gains are just threshold/smoothing changes or whether probability fidelity worsens while hard F1 improves.
- **Interpretation limit:** Annotation-derived duration is one-second resolution. Soft values represent aggregated opinions, not physical event probabilities.

## 8. Score and next decision

**Provisional score: 71.8/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 3/5; the required rating is 4/5. 2 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Low-medium: soft labels, rare-event gains and missing-label methods already exist; the duration-specific addition is not established. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium: original annotation payload and permitted research use checked; documentation mismatch, one invalid value and tiny independent recording count weaken suitability. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: one compact CRNN and bounded audio release fit the timeline; audio learning and label-quality handling remain. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: objective, pooling and decision-learning experiments go beyond an audio-player application. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: soft metrics, one-second limits and recording grouping prevent obvious overclaims; some baseline implementation details remain unverified. |
| Three-member structure | 12 | 4 | 9.6 | Medium: three investigations share one event model and each has a direct comparator. |
| Real-world significance | 9 | 3 | 5.4 | Medium: event-monitoring failures are concrete; this benchmark cannot establish hazard detection benefits. |
| Compute/storage | 5 | 4 | 4.0 | Medium: few-GB audio and a compact backbone fit modest resources; timing and memory unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium-high: a local one-second timeline is straightforward. |
| **Normalised total / 100** | **98** |  | **71.8** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Pass | Section 5 records an original public release or author-documented loading route, existing labels and the access-check limit. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Unknown | Distinctiveness of duration-aware learning beyond existing soft-SED and masking methods is unresolved. |
| 7. Beyond application assembly | Unknown | Need to show that the learning contribution exceeds routine class/duration reweighting. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Pass | The bounded core and fallback in Section 5 are plausible within the team window; training costs remain estimates. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Pass | Section 5 records source terms and a bounded offline use; no deployment or high-stakes benefit is assumed. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** Keep as an audio reserve; data quality and methodological differentiation need attention.

**Next decision point:** Resolve the out-of-range annotation value and documented class eligibility, reproduce soft-BCE/MSE, then test whether short-event suppression persists at matched thresholds. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
