[← Research candidates](../research-candidates.md)

# Activity transitions under unfamiliar sensor sampling patterns

**ID:** X09 · **Area:** Time series / sensor classification · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Sampling patterns can become predictive shortcuts, while sparse or irregular observations obscure brief activity transitions. Recent PRISM and SIGHT papers document sampling-shift and temporal-adaptation limitations. Generic sampling-rate robustness and adversarial augmentation already exist.

**Potential stakeholders:** Wearable activity-recognition developers; no clinical use is established.

## 2. Research gap and question

**Tentative gap:** Study constrained learned sampling augmentation together with transition-sensitive temporal learning, tested under coupled observation and signal shifts. PRISM explicitly leaves learned plausible sampling generators and coupled feature shifts open; this does not prove that a particular generator is novel.

**Research question:** Can a source-trained, constrained sampling curriculum preserve postural-transition recognition under unseen dropout/rate patterns better than fixed sampling augmentation?

**Hypothesis and rival explanation:** A budget-constrained adversarial sampling policy will improve transition recall without exploiting class-dependent missingness shortcuts. Rival explanation: fixed downsampling augmentation or a larger receptive field suffices.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Domain Generalization under Sampling Pattern Shifts, 2026](https://arxiv.org/html/2609.33279v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2609.33279) | HAR-C and PRISM; sampling shortcuts and robust source training. | Appendix A leaves learned sampling generators and coupled sampling/feature shifts open. | Full text; benchmark, method and limitations; Sections 2–4; Appendix A (X09-L1) |
| [Temporal Structure Matters for Efficient Test-Time Adaptation, 2026](https://arxiv.org/html/2605.04617v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2605.04617) | SIGHT temporal refinement for cross-subject activity streams. | Sparse sampling and abrupt changes are stated limitations; distinguish source-only learning from target adaptation. | Full text; method and limitations; Sections 4–5; Appendix limitations (X09-L2) |
| [HAR Robust to Different Sampling Rates, 2021](https://arxiv.org/html/2101.00812v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FJSEN.2020.3038281) | Adversarial learning and downsampling augmentation. | Do not claim sampling-rate augmentation or adversarial invariance is new. | Full text located; abstract/method inspected; Method and sampling-rate experiments (X09-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2609.33279,10.48550%2FarXiv.2605.04617,10.1109%2FJSEN.2020.3038281). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Train a small time-aware temporal model and a constrained mask/rate curriculum on source subjects. Add a transition-sensitive objective and source-only calibration. Keep mask families class-balanced and hold out sampling patterns. The regular original data does not provide measured real dropout mechanisms; generated masks are controlled tests.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [UCI HAPT / postural transitions](https://archive.ics.uci.edu/dataset/341/smartphone+based+recognition+of+human+activities+and+postural+transitions). |
| Verified source details | Thirty subjects, 50 Hz acceleration/gyroscope raw streams, six activities and six postural transitions. RawData/labels.txt supplies experiment, user, activity and start/end sample indices. |
| Access and licence | Official direct ZIP route listed as 75.9 MB; CC BY 4.0. File list and loading documentation inspected; raw archive not downloaded. |
| Evaluation version | Use raw sequences and transition labels, not only pre-windowed 561-feature records. Partition subjects and whole recordings before resampling/windowing. |
| Resources, estimated | CPU-first small CNN/GRU/TCN, 4–8 GB RAM and under 5 GB working disk; optional modest GPU. Original-to-generated size expansion must be capped. |
| Fallback / prototype | Fixed augmentation plus a learned small policy on fewer mask families; local activity replay. No continuous wearable deployment or medical claims. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: observation policy | Can a learned constrained sampling policy beat fixed masks? H: A learned constrained curriculum outperforms fixed mask mixtures. | Train a mask/rate curriculum under fixed observation budgets. | Uniform and predefined masks; remove learned policy. | Generalisation to unseen mask families. |
| B: transitions | Can transition-sensitive training retain brief state changes? H: Transition-specific training reduces missed brief state changes. | Train a temporal boundary/transition objective. | Ordinary classification; match receptive field and resolution. | Transition F1 and delayed-change errors. |
| C: confidence | Can source-only uncertainty fitting identify sampling failures? H: Time-gap-aware confidence identifies sampling failures. | Learn a time-gap-aware calibrator/rejector. | Global calibration and no rejector; remove gap features. | Selective risk by transition and sampling condition. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Subject-macro transition F1, with transition definitions/tolerances frozen from training and validation; include ordinary-activity macro-F1.
- **Split:** Subject-disjoint raw recordings; hold out sampling-pattern families. Keep overlapping windows and all resampled versions of a recording together; no target-subject labels for tuning.
- **Baselines and code:** Handcrafted features/SVM, DeepConvLSTM or small TCN, fixed sampling augmentation, PRISM and SIGHT as modern references. [ViTST code](https://github.com/Leezekun/ViTST) provides an additional irregular-series baseline; exact PRISM anonymous-code access remains unverified.
- **Ablations:** Learned policy, transition loss and calibration; also compare sampling-only, feature-only and coupled shifts at matched observed samples.
- **Uncertainty and errors:** Subject-cluster bootstrap, repeated training/mask seeds; errors by transition, remaining sampling density, burst length and channel loss.
- **Useful result without winning:** Show when dropout augmentation creates label shortcuts or when apparent robustness hides missed transitions.
- **Interpretation limit:** The waist-mounted laboratory protocol does not establish cross-device, clinical or real dropout-process generalisation. Do not invent physical energy savings from dropped samples.

## 8. Score and next decision

**Provisional score: 77.8/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 3/5; the required rating is 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Medium-low: explicit recent limitations support the question, but older adversarial sampling methods require sharper differentiation. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: original raw streams, subject IDs, transition indices, direct route and licence are documented. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: small temporal models and a capped generator are feasible; adversarial optimisation could be unstable. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: learned observation policy, temporal objective and uncertainty fitting provide substantive experiments. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: raw-sequence grouping and held-out masks address shortcuts; synthetic sampling limits external validity. |
| Three-member structure | 12 | 4 | 9.6 | Medium: policy, transition objective and calibration are distinct interventions on one classifier. |
| Real-world significance | 9 | 4 | 7.2 | Medium: observation loss affects activity systems, but this dataset does not validate real wearable benefits. |
| Compute/storage | 5 | 5 | 5.0 | Medium-high: small public data and compact temporal models support CPU development; runtime unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium-high: a historical activity/sampling replay is bounded. |
| **Normalised total / 100** | **98** |  | **77.8** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Pass | Section 5 records an original public release or author-documented loading route, existing labels and the access-check limit. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Unknown | Novelty beyond PRISM and established adversarial sampling-rate methods remains unverified. |
| 7. Beyond application assembly | Pass | Section 6 investigates learned interventions with baseline comparisons and ablations, rather than application assembly. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Pass | The bounded core and fallback in Section 5 are plausible within the team window; training costs remain estimates. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Pass | Section 5 records source terms and a bounded offline use; no deployment or high-stakes benefit is assumed. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** A strong low-resource sensor-learning direction for further checking; source-only scope must remain explicit.

**Next decision point:** Reproduce fixed-rate/mask augmentation on raw subject-disjoint HAPT, then establish a transition failure before designing a learned policy. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
