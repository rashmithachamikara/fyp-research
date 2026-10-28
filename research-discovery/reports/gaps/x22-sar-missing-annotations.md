[← Research candidates](../research-candidates.md)

# Learning SAR ship detectors without inheriting AIS annotation blind spots

**ID:** X22 · **Area:** Computer vision — SAR ship detection · **Status:** Provisional opportunity; not qualified

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

Some SAR training ships have no box because annotations were generated from AIS. Treating every unlabelled location as sea background can therefore create false negatives. This matters to researchers estimating vessels missed by broadcast-based monitoring.

## 2. Research gap and question

**Question:** Can annotation-provenance-aware training preserve small-ship recall under structured label omissions better than teacher pseudo-label completion and uncertainty-based negative mining?

**Tentative hypothesis:** Modelling omission risk by source and apparent size improves recall at a fixed false-positive budget.

**Rival explanation:** Apparent improvement comes from extra manual labels or scene-domain differences, rather than better treatment of missing annotations.

**What is already addressed / what remains inferred:** Pseudo-labelling and uncertainty-based suppression of ambiguous negatives are already implemented. The proposed distinction is AIS-dependent, non-random omission and evaluation on independently annotated ships. That distinction is inferred and not verified novel.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [xView3: Dark Fishing Detection with SAR Imagery and AIS Data (2022)](https://arxiv.org/abs/2206.00897) | AIS/manual annotation provenance and wind-quality inputs; does not make unreported vessels illegal. | Original paper: dataset, labels and auxiliary rasters. Full paper inspected in this session. |
| [Allen AI xView3 detector: author implementation](https://github.com/allenai/sar_vessel_detect) | Missing AIS-derived training annotations are documented; manual-validation-trained pseudo-label completion is already implemented. | README: pseudo-labelling procedure. Author README inspected. |
| [Uncertainty-based confusing/challenging negative proposal mining (2026)](https://doi.org/10.3390/rs18162737) | Already separates difficult background and possible unlabelled objects using uncertainty and IoU; broad missing-label mining is not new. | Sections 3, UGPS and UADGR. Publisher-indexed method excerpts; direct page returned 429. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Fit a compact detector with source-specific background weights or a positive–unlabelled objective. Compare matched label budgets, identical teachers and both random and size-dependent deletion of existing boxes. Use natural annotation-source comparisons only when provenance can be reconstructed.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

xView3 has automated/manual label provenance and a documented loading route, but its old dataset subpage returns 404 and the current complete download/licence route was not completed. The GFW CC BY 4.0 detection archive is a smaller fallback; its AIS-derived presence labels alone cannot measure recovery of naturally unlabelled ships.

**Original sources:** [xView3: Dark Fishing Detection with SAR Imagery and AIS Data (2022)](https://arxiv.org/abs/2206.00897); [GFW Nature training data](https://doi.org/10.6084/m9.figshare.24309469).

**Fallback and claim boundary:** Use a fully annotated, licensed subset and controlled label deletion. This supports robustness to specified omissions, not a claim to have recovered actual dark vessels.

**Unmeasured resource estimate:** Estimate: 8–12 GB GPU with small chips, 16–32 GB RAM, 20–80 GB for a bounded scene subset and caches. Full xView3 ingestion is excluded. No training speed or peak memory has been measured.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: omission-aware learning | Can a source-aware loss avoid background penalties? H: It retains recall under source/size-dependent omissions. | Train a provenance-weighted detection loss. | Ordinary detector and teacher pseudo-labels; remove source weights. | Recall versus omission pattern at equal label budget. |
| B: safe negative mining | Can a learned ambiguous-negative filter avoid confusing ships and clutter? H: It reduces false negatives without a matching rise in coastal false alarms. | Adapt negative-proposal selection with a held-out calibration set. | Uncertainty mining/UA-PMP control; remove omission features. | False-positive/recall trade-off on independently annotated scenes. |
| C: teacher reliability | Which pseudo-labels should receive training weight? H: Source-group calibration improves useful pseudo-label precision. | Fit a confidence/reliability model on development scenes. | Fixed-confidence teacher and temperature scaling; remove source grouping. | Pseudo-label precision and downstream detector sensitivity. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** Small-ship recall at a development-fixed false-positive rate per square kilometre, only where geospatial scene area is available; otherwise recall at a fixed false positives/chip budget.
- **Split:** Group complete acquisitions/geographies. Reserve manually annotated scenes for disjoint development and locked evaluation; never train on official validation scenes and then report the same scenes as independent validation.
- **Baselines:** Conventional compact Faster R-CNN/RetinaNet; Allen AI xView3 teacher completion; uncertainty-based negative mining as a close modern control, subject to reproducible code/method access.
- **Ablations:** Random versus source/size-dependent omission; provenance loss, negative filtering and calibration separately; equal manual-label budgets and teacher data.
- **Uncertainty and error analysis:** Bootstrap acquisitions, use three feasible seeds; stratify by box size, AIS/manual provenance, coastal clutter and sensor. Missing AIS status is not a class label.
- **Useful findings without outperforming the strongest baseline:** Show that the observed omission effect disappears after scene/source controls, or that pseudo-label completion already resolves it.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 69.8/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

### Weighted rubric

Nine relative weights total 98; scores are normalised to 100. Decimal precision is arithmetic, not confidence.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: Specific failure is testable, but overlap with the cited neighbours remains unresolved; no certified novelty. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium-low: An original-source dataset route exists, but labels, access or evaluation support remain incomplete. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: Completion depends on resolving data or methodological prerequisites early. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: Losses, trainable fusion/state models or calibration are substantive ML investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: Explicit grouped evaluation, controls and uncertainty are defined, conditional on the documented data checks. |
| Three-member structure | 12 | 4 | 9.6 | Medium: Three related model investigations can each use an unchanged common baseline; data dependencies remain explicit. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: A specific observation/identity error affects maritime research; operational benefits remain untested. |
| Compute/storage | 5 | 3 | 3.0 | Medium-low: Scene extraction and multiple detector runs may exceed the initial resource estimate. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **69.8** | **Not qualified.** |

### Mandatory gates

Pass refers to the bounded proposal design; it is not a completed experiment. Unknown gates are not waived.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest sources identify a concrete observation or identity failure; benefit is not yet demonstrated. |
| 2. ML essential | Pass | The research question concerns learned prediction, representation or adaptation. |
| 3. Train/adapt models | Pass | Sections 4 and 6 specify models/objectives to train or adapt, not an external API-only application. |
| 4. Existing data accessible | Unknown | Section 5 identifies missing access, label, alignment or independent-reference requirements; adjacent public data do not resolve them. |
| 5. No unavailable human evaluation | Pass | The bounded proposal uses existing observations/labels. No new fieldwork, interviews or expert annotation is required; absent existing labels block selection. |
| 6. Precise research gap | Unknown | The distinction beyond close prior methods remains an inferred opportunity, not a verified novel gap. |
| 7. Beyond application assembly | Pass | Trainable methodological interventions and ablations go beyond assembling a vessel dashboard. |
| 8. Objective evaluation | Pass | Section 7 defines objective bounded endpoints, grouped splits and baseline/ablation controls; data limitations constrain claims. |
| 9. 6–8 month feasibility | Unknown | Data prerequisites must be resolved before completion in 6–8 months can be supported. |
| 10. Three connected contributions | Pass | Each member has a question, trained intervention, baseline/ablation and attributable result; all can use unchanged common features/models. |
| 11. No specialised/continuous high-end compute | Pass | Core design excludes raw global ingestion, new hardware and continuous high-end or multi-GPU pretraining; estimates appear in section 5. |
| 12. Manageable data reuse | Unknown | Dataset imagery/API terms remain to verify for the exact intended subset. |
| 13. Useful negative findings | Pass | Section 7 defines useful findings if the intervention loses or the stronger claim is not identifiable. |

**Next decision point:** Secure the xView3 terms and scene/provenance files, then compare existing pseudo-label and UA-PMP controls on a bounded omission experiment.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
