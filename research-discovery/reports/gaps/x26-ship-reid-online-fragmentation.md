[← Research candidates](../research-candidates.md)

# Avoiding multiple identities for one ship in optical/SAR image streams

**ID:** X26 · **Area:** Computer vision — online vessel identity clustering · **Status:** Provisional opportunity; not qualified

[View the HTML infographic](../x26-vessel-identity-infographic.html).

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

HOSS-Bench already evaluates online optical/SAR clustering. Its reported TransOSS result creates about 214 clusters for 85 reference identities. This is a documented fragmentation problem, not an unimplemented task.

## 2. Research gap and question

**Question:** Can reversible, modality-aware cluster updates reduce identity fragmentation without increasing false merges?

**Tentative hypothesis:** Keeping multiple modality-specific exemplars and revisable assignments improves clustering at a fixed pairwise false-merge budget.

**Rival explanation:** Better static embeddings or a retuned clustering threshold explain the improvement; online state adds no value.

**What is already addressed / what remains inferred:** Online clustering and cross-modal identity prototypes already exist. A new method must beat the published online threshold protocol and embedding-only improvements. HOSS-Bench is a submission; acceptance and full public protocol code were not verified.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [HOSS-Bench: open-set and online cross-modal ship ReID (2026 submission)](https://openreview.net/pdf?id=hZwvQwTfU8) | Online clustering already exists. For 85 reference identities, the reported TransOSS result creates 214.0 ± 1.5 clusters. | Online clustering protocol and Table 3. Primary PDF sections/table inspected; acceptance not verified. |
| [Cross-modal Ship Re-Identification via Optical and SAR Imagery (ICCV 2025)](https://arxiv.org/abs/2506.22027) | TransOSS already uses approximate crop/GSD physical size; crop bounds are not exact hull dimensions. | Section 4.2 size embedding; Table 1 dataset. Full HTML methods inspected. |
| [SDF-Net cross-modal ship re-identification (2026 preprint)](https://arxiv.org/abs/2603.12588) | Structure/appearance disentanglement and cross-modal identity prototypes are established neighbouring methods. | Disentanglement, identity prototypes and batch construction. Full HTML inspected. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Cache common embeddings, then learn compact cluster-state or merge/split scoring functions using development identities. Compare irrevocable and reversible decisions under identical observation orders.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

HOSS archive contents, licence and sequence/frame filename structure were checked. Sequence/frame indices are not verified elapsed timestamps. Existing train/query/gallery counts are documented; no live stream or MMSI-linked truth is supplied.

**Original sources:** [HOSS author dataset](https://doi.org/10.5281/zenodo.15860212); [HOSS/TransOSS author code and model route](https://github.com/Alioth2000/Hoss-ReID).

**Fallback and claim boundary:** Use controlled arrival orders and sequence-grouped stress tests on the released crops. Conclusions concern benchmark identity consistency, not real-time voyage tracking or fleet-wide unique vessel counts.

**Unmeasured resource estimate:** Estimate: CPU cached-embedding clustering with occasional 8–12 GB GPU adaptation; 2–10 GB storage. No continuous satellite feed or satellite purchase is needed.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: modality-aware memory | Does retaining separate exemplars stop modality switches creating identities? H: Multi-exemplar memory reduces fragmentation. | Learn a compact prototype-update rule. | Single centroid and HOSS-Bench threshold clustering; remove modality memory. | Fragmentation at matched false-merge budget. |
| B: reversible clustering | Can a model undo early wrong cluster decisions? H: Reversible updates improve consistency after difficult early observations. | Train a merge/split evidence model. | Irreversible threshold clustering and agglomeration; disable reversal. | Corrected versus newly introduced merges/splits. |
| C: stable acceptance policy | Can acceptance adapt to evidence quantity without knowing the true number of vessels? H: Evidence-aware calibration outperforms a fixed threshold. | Fit uncertainty-aware join/new-cluster decisions. | Validation-fixed threshold and calibrated pair classifier; remove history features. | Pairwise error and cluster-count stability across orderings. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** B-cubed F1 and fragmentation at a validation-fixed pairwise false-merge ceiling; report ARI, cluster-count error and pairwise precision/recall.
- **Split:** Use disjoint identities for learning/calibration/testing. Keep duplicate protocol crops together, vary arrival order with fixed seeds, and test modality-blocked orders. Never set thresholds using the test identity count.
- **Baselines:** HOSS-Bench nearest-cluster threshold protocol, DINO/TransOSS fixed features and a conventional clustering control; SDF-Net embeddings test whether representation alone explains the result.
- **Ablations:** Multiple exemplars, modality information, reversal and learned acceptance separately. Match embeddings and observation order.
- **Uncertainty and error analysis:** Identity-block bootstrap over many order seeds; inspect first-observation errors, distractors, single-modality identities and same-size ships. Sequence order experiments are not elapsed-time validation.
- **Useful findings without outperforming the strongest baseline:** Quantify the embedding/threshold contribution, or show a false-merge cost that makes reversible clustering unsuitable despite lower cluster-count error.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 77.8/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

### Weighted rubric

Nine relative weights total 98; scores are normalised to 100. Decimal precision is arithmetic, not confidence.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: Specific failure is testable, but overlap with the cited neighbours remains unresolved; no certified novelty. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: HOSS archive and CC BY 4.0 terms inspected; metadata details and model loading remain untested. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: Cached features/compact models fit a bounded design; execution remains estimated. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: Losses, trainable fusion/state models or calibration are substantive ML investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: Explicit grouped evaluation, controls and uncertainty are defined, conditional on the documented data checks. |
| Three-member structure | 12 | 4 | 9.6 | Medium: Three related model investigations can each use an unchanged common baseline; data dependencies remain explicit. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: A specific observation/identity error affects maritime research; operational benefits remain untested. |
| Compute/storage | 5 | 5 | 5.0 | Medium-high: Cached-feature/CPU experiments are plausible; no runtime or peak memory measured. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **77.8** | **Not qualified.** |

### Mandatory gates

Pass refers to the bounded proposal design; it is not a completed experiment. Unknown gates are not waived.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest sources identify a concrete observation or identity failure; benefit is not yet demonstrated. |
| 2. ML essential | Pass | The research question concerns learned prediction, representation or adaptation. |
| 3. Train/adapt models | Pass | Sections 4 and 6 specify models/objectives to train or adapt, not an external API-only application. |
| 4. Existing data accessible | Pass | HOSS is downloadable and licensed; identity-labelled crops and sequence indices support controlled online-order experiments. |
| 5. No unavailable human evaluation | Pass | The bounded proposal uses existing observations/labels. No new fieldwork, interviews or expert annotation is required; absent existing labels block selection. |
| 6. Precise research gap | Unknown | The distinction beyond close prior methods remains an inferred opportunity, not a verified novel gap. |
| 7. Beyond application assembly | Pass | Trainable methodological interventions and ablations go beyond assembling a vessel dashboard. |
| 8. Objective evaluation | Pass | Section 7 defines objective bounded endpoints, grouped splits and baseline/ablation controls; data limitations constrain claims. |
| 9. 6–8 month feasibility | Pass | The cached-feature or compact-model route is a plausible 6–8 month design, not a demonstrated completion/runtime guarantee. |
| 10. Three connected contributions | Pass | Each member has a question, trained intervention, baseline/ablation and attributable result; all can use unchanged common features/models. |
| 11. No specialised/continuous high-end compute | Pass | Core design excludes raw global ingestion, new hardware and continuous high-end or multi-GPU pretraining; estimates appear in section 5. |
| 12. Manageable data reuse | Pass | The bounded public-data route uses a verified CC BY 4.0 release; source attribution and label interpretation remain required. |
| 13. Useful negative findings | Pass | Section 7 defines useful findings if the intervention loses or the stronger claim is not identifiable. |

**Next decision point:** Reproduce the HOSS-Bench protocol or document its exact reimplementation, then confirm fragmentation with cached released features before inventing a new clustering method.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
