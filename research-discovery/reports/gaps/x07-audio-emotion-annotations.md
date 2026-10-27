[← Research candidates](../research-candidates.md)

# Audio emotion confidence with modality-matched annotations

**ID:** X07 · **Area:** Audio / multi-annotator learning · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

The same acted utterance receives different audio-only and audiovisual emotion judgments. Supervising an audio-only model with a pooled or audiovisual target can therefore train it toward information absent from its input. Generic annotator disagreement and cross-corpus uncertainty are already studied.

**Potential stakeholders:** Speech-model developers and researchers evaluating listener-judgment probabilities.

## 2. Research gap and question

**Tentative gap:** Investigate modality-matched probability targets and controlled transfer of information from paired annotation views, evaluated against existing audio-only votes on unseen actors. This is a listener-judgment modelling problem, not inference of a speaker's true mental state.

**Research question:** Can modality-aware soft-target learning reduce an audio-only classifier's overconfidence relative to held-out audio-only ratings without requiring new annotations?

**Hypothesis and rival explanation:** Modality-matched targets plus a constrained cross-view regulariser will improve audio-only vote fidelity. Rival explanation: any apparent gain comes from speaker or sentence leakage, or ordinary soft-label training.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Are You Sure?, Interspeech 2024](https://arxiv.org/html/2407.01143v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2407.01143) | SER uncertainty under disagreement, unknown inputs and corruption. | Uncertainty-aware SER is occupied; isolate annotation-view mismatch on identical clips. | Full text; Sections 2–4 (X07-L1) |
| [More Similar than Dissimilar, ASRU 2025](https://arxiv.org/html/2509.12295v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2509.12295) | Annotator modelling and cross-corpus personalisation. | Avoid an enrolment or new-rater-data dependency; compare population-level audio-only targets. | Full text located; method and abstract inspected; Methods and experimental setup (X07-L2) |
| [Minority Views Matter, 2024](https://doi.org/10.1109/TAFFC.2024.3411290) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FTAFFC.2024.3411290) | Evaluation using subjective annotations and inclusive aggregation. | An annotation-view-specific objective needs differentiation from existing aggregation rules. | Scholarly abstract only; FastTrack X07-D1 neighbour (X07-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2407.01143,10.48550%2FarXiv.2509.12295,10.1109%2FTAFFC.2024.3411290). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Use generic frozen audio embeddings with a learned small head. Compare audio-only targets, actor-intended labels and audiovisual targets on exactly the same partitions. Train a view-aware regulariser and a calibration method without feeding faces or actor IDs at inference.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [CREMA-D author repository](https://github.com/CheyneyComputerScience/CREMA-D): 7,442 clips, 91 actors, six intended emotions and twelve sentences. |
| Actually checked | README, storage instructions and licence inspected. A bounded 16 KB prefix of finishedResponses.csv verified queryType, clipName and response fields; raw individual responses were not saved in reports. |
| Targets | Filter queryType=1 for audio-only judgments, using the author mapping. Do not mistake the actor's filename label or a pooled tabulation for an audio-only vote distribution. |
| Access and licence | Author release uses ODbL 1.0 with Database Contents License for individual contents. Git LFS is required for media; a normal ZIP can contain pointer files. Full clone documented around 7.55 GB; audio-only size unmeasured. |
| Resources, estimated | Frozen features and small heads: 8 GB RAM, 10–20 GB disk; optional modest GPU for extraction/fine-tuning. Validate media access and known damaged files before training. |
| Fallback / prototype | Restrict to verified actors and recordings, preserving actor holdouts; local audio-only vote-probability display. No claims about clinical, workplace or hidden emotional states. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: target model | Does input-matched supervision improve audio-only vote fidelity? H: Matching the target view improves audio-only vote fidelity. | Train a count-aware audio-only probabilistic head. | Intended-label and ordinary soft-target heads; remove count model. | Vote distribution error on held-out actors. |
| B: cross-view learning | Can other annotation views help without transferring unavailable visual cues? H: Constrained transfer helps where naive audiovisual supervision harms. | Train a constrained cross-view consistency/transfer term. | Audio-only baseline and naive pooled targets; remove constraint. | Benefit/harm versus audio–visual disagreement. |
| C: calibration | Can actor-held-out calibration improve reliability without collapsing disagreement? H: Regularised calibration improves confidence without erasing disagreement. | Fit regularised probability calibration from source actors. | Temperature scaling and no calibration; remove regularisation. | Probability fidelity and selective risk by agreement. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Brier score against existing audio-only vote proportions; use per-clip count-aware uncertainty and distribution distance as secondary outcomes.
- **Split:** Actor-disjoint train/validation/test; additional sentence-held-out diagnostic. All views and encodings of a clip stay together; actor IDs are grouping variables, never input features.
- **Baselines and code:** MFCC/openSMILE-style features with logistic regression; frozen wav2vec2/audio embeddings plus MLP; soft-label/dropout and the 2024 uncertainty methods. [SpeechBrain](https://github.com/speechbrain/speechbrain) is an implementation route, not proof of a matching pretrained split.
- **Ablations:** Target view, count model, constrained view transfer and calibration independently; identical encoder/features and rater counts.
- **Uncertainty and errors:** Actor-cluster bootstrap, rater resampling where assignments permit and training seeds; errors by sentence, intended class and cross-view disagreement.
- **Useful result without winning:** Demonstrate when intended labels or audiovisual votes give deceptively confident scores for an audio-only model.
- **Interpretation limit:** A codec/noise transformation has no new human ratings here; do not claim its perceived-emotion uncertainty is ground-truthed by clean-audio votes. No new participant study is assumed.

## 8. Score and next decision

**Provisional score: 74.9/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 3/5; the required rating is 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Low-medium: annotation-view mismatch is testable, but closest annotator and aggregation methods may cover the proposed modelling idea. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: paired rating views and grouping schema are documented and a response prefix was inspected; LFS waveform loading remains pending. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: frozen embeddings and small heads are bounded; correct target reconstruction and subjective-label analysis need care. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: count-aware training, constrained cross-view transfer and calibration are empirical contributions. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: actor/sentence grouping and matched annotation views directly test the claim; finite rater counts limit precision. |
| Three-member structure | 12 | 4 | 9.6 | Medium: target modelling, cross-view objective and calibration have separate comparisons within one predictor. |
| Real-world significance | 9 | 3 | 5.4 | Medium-low: a concrete supervision error matters for SER research, but acted recordings limit natural-conversation relevance. |
| Compute/storage | 5 | 4 | 4.0 | Medium: author storage estimate fits and heads are small; audio decoding and feature cost unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium-high: local audio and probability inspection is bounded. |
| **Normalised total / 100** | **98** |  | **74.9** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Pass | Section 5 records an original public release or author-documented loading route, existing labels and the access-check limit. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Unknown | Modality-specific novelty beyond recent annotator modelling and aggregation remains to be established. |
| 7. Beyond application assembly | Pass | Section 6 investigates learned interventions with baseline comparisons and ablations, rather than application assembly. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Pass | The bounded core and fallback in Section 5 are plausible within the team window; training costs remain estimates. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Pass | Section 5 records source terms and a bounded offline use; no deployment or high-stakes benefit is assumed. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** A feasible annotation-learning lead, with limited ecological validity and unresolved novelty.

**Next decision point:** Reconstruct audio-only vote counts for a verified media subset and compare intended-label, audiovisual and audio-only supervision with one fixed encoder. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
