[← Research candidates](../research-candidates.md)

# Land-cover confidence when optical quality and sensor availability change

**ID:** X02 · **Area:** Computer vision / remote sensing · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Optical cloud contamination can make a fused radar–optical classifier over-rely on the poorer input. A 2026 reliability-aware fusion paper already studies this, including a spatial holdout; neither reliability gating nor geographic testing is a new gap.

**Potential stakeholders:** Land-cover analysts and Earth-observation model developers.

## 2. Research gap and question

**Tentative gap:** The narrower candidate is availability-conditioned uncertainty calibration under combinations of missing modalities and quality changes not used for calibration. Whether this adds enough beyond current fusion and incomplete-multimodal learning is unresolved.

**Research question:** Can availability-conditioned calibration preserve useful land-cover confidence at a fixed review budget when both input availability and corruption type change on held-out regions?

**Hypothesis and rival explanation:** Conditioning calibration on observed modality availability will reduce worst-regime selective error. Rival explanation: gains are just the benefit of using the SAR-only classifier in difficult cases.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Reliability-Aware Cross-Modal Fusion, 2026](https://doi.org/10.3390/rs18152484) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390%2Frs18152484) | Quality-aware radar–optical fusion, degraded inputs and a scene-held-out evaluation. | Broad fusion proposal is occupied; compare unseen combinations and explicit confidence calibration. | Primary indexed abstract/conclusion; direct full page returned 429; Abstract; indexed conclusion (X02-L1) |
| [A Novel Approach to Incomplete Multimodal Learning, 2024](https://doi.org/10.1109/TGRS.2024.3387837) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FTGRS.2024.3387837) | Learning with incomplete remote-sensing modalities. | Precise availability and calibration assumptions require full-text checking. | Scholarly abstract; methods not inspected; FastTrack X02-S2 result (X02-L2) |
| [UnCRtainTS, CVPR Workshops 2023](https://doi.org/10.1109/CVPRW59228.2023.00202) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1109%2FCVPRW59228.2023.00202) | Uncertainty for optical cloud-removal reconstruction. | Reconstruction uncertainty is a neighbour, not evidence that land-cover calibration is solved. | Scholarly abstract; methods not inspected; FastTrack X02-S2 result (X02-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.3390%2Frs18152484,10.1109%2FTGRS.2024.3387837,10.1109%2FCVPRW59228.2023.00202). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Freeze or lightly fine-tune small modality encoders. Investigate feature-quality estimation, availability-aware fusion and partial-pooling calibration on a shared patch classifier. Represent a missing modality explicitly rather than silently replacing it with a normal-looking tensor.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [SEN12MS author toolbox](https://github.com/schmitt-muc/SEN12MS), with paired SAR, optical patches and MODIS-derived land-cover labels. |
| Labels and grouping | Author README documents ROI/scene holdouts and one damaged SAR patch. MODIS-derived labels are coarse; they do not establish precise parcel boundaries. |
| Access and licence | Original [mediaTUM release](https://mediatum.ub.tum.de/1474000) returned 429. Toolbox and plain-text split/label routes are documented, but current payload access and dataset-specific terms were not independently verified. |
| Bounded core / fallback | A few whole ROIs and 5,000 paired patches, if selective downloads are practical. Otherwise defer; EuroSAT alone cannot validate radar–optical fusion. |
| Resources, estimated | An occasional 8–12 GB GPU, 16 GB RAM, tens of GB for a verified subset. Full-release storage and selective-download workload remain unresolved. |
| Prototype | Offline patch classification with available-modality indicators and uncertainty; no land-management recommendation. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: input quality | Can learned quality estimates distinguish corrupted from informative features? H: Feature quality predicts which modality will fail. | Quality head on frozen encoder outputs. | Handcrafted quality scores; omit quality supervision. | Quality ranking across corruption types. |
| B: fusion | Does availability-aware fusion outperform best single-modality use? H: Explicit missingness conditioning improves worst-regime classification. | Train modality-dropout fusion with an explicit missingness state. | Late fusion and SAR-only; remove missingness state. | Worst-regime classification and failure cases. |
| C: calibration | Does partial pooling improve confidence on sparse regimes? H: Partial pooling improves sparse-regime confidence. | Pool calibrators across quality/availability groups. | Global and per-regime calibration; remove pooling. | Selective risk at matched retained coverage. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Worst-regime selective classification risk at a source-validation-selected 80% retained coverage target; also report realised coverage on each test regime.
- **Split:** Whole ROI holdouts; group overlapping patches and all modality copies. Tune on source ROIs, not geographic test labels.
- **Baselines and code:** Author [ResNet/DenseNet classification code](https://github.com/schmitt-muc/SEN12MS), optical-only, SAR-only, late fusion and the 2026 reliability gate. Exact neighbour implementations/checkpoints unverified.
- **Ablations:** Quality head, availability state, modality dropout and calibration pooling; match sensor access and feature budgets.
- **Uncertainty and errors:** Repeated ROI partitions where feasible, training seeds and ROI-cluster intervals; errors by land-cover class, modality and degradation severity.
- **Useful result without winning:** Establish when the single SAR model is more reliable than a larger fused model.
- **Interpretation limit:** Synthetic cloud-like masking is not real cloud physics; no guarantee of calibrated confidence under arbitrary geographic shift.

## 8. Score and next decision

**Provisional score: 66.5/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 2/5; the required rating is 4/5. 5 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **2** | 6.4 | Low: an extremely close 2026 fusion study already covers much of the initial idea; the narrower calibration method needs full-text differentiation. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Low-medium: original label/split documentation exists, but payload access, subset size and release terms are not confirmed. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Low: substantial geospatial loading, label and fusion work remain, despite a proposed patch cap. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: quality learning, modality-dependent fusion and uncertainty fitting are empirical model investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: ROI grouping and explicit regime comparisons are sound in design; access is a critical dependency. |
| Three-member structure | 12 | 4 | 9.6 | Medium: quality, fusion and calibration can be assessed on the same frozen features independently. |
| Real-world significance | 9 | 4 | 7.2 | Medium: cloud and sensor availability are consequential mapping constraints; no operational benefit demonstrated. |
| Compute/storage | 5 | 3 | 3.0 | Low: selective-download feasibility and feature-cache size remain unknown. |
| Prototype | 3 | 4 | 2.4 | Medium: a local patch viewer is straightforward once data loading is solved. |
| **Normalised total / 100** | **98** |  | **66.5** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Unknown | Original mediaTUM payload could not be inspected; selective downloading is unverified. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Unknown | Closest fusion and incomplete-modality methods not fully differentiated. |
| 7. Beyond application assembly | Unknown | The proposed addition may reduce to ordinary gating plus calibration. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Unknown | Subset access, preprocessing and workload remain unbounded. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Unknown | Dataset-specific release terms need checking at the accessible original record. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** Redesign or defer; current overlap and access dependencies outweigh the appealing application.

**Next decision point:** Obtain the original release terms and a practical ROI download route, then inspect the closest two methods before implementing. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
