[← Research candidates](../research-candidates.md)

# Using wind metadata without making SAR detection brittle

**ID:** X24 · **Area:** Multimodal ML — SAR and environmental data · **Status:** Provisional opportunity; not qualified

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

SAR appearance varies with sea conditions. A detector that relies on environmental metadata can fail when the metadata are low-quality, stale or spatially coarse.

## 2. Research gap and question

**Question:** Does quality-aware environmental fusion preserve small-ship detection when wind inputs are absent or inaccurate, while retaining gains on trustworthy inputs?

**Tentative hypothesis:** A learned reliability gate matches image-only robustness under unreliable metadata and improves recall when metadata are useful.

**Rival explanation:** The model learns location/season shortcuts or gains simply from metadata dropout regularisation.

**What is already addressed / what remains inferred:** Environmental conditioning is established in wake research, and physical-feature fusion already addresses motion defocus. The latter uses signal-domain features, not weather. The inferred question concerns measured metadata quality and detector sensitivity, not first multimodal fusion.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [xView3: Dark Fishing Detection with SAR Imagery and AIS Data (2022)](https://arxiv.org/abs/2206.00897) | AIS/manual annotation provenance and wind-quality inputs; does not make unreported vessels illegal. | Original paper: dataset, labels and auxiliary rasters. Full paper inspected in this session. |
| [UEIKAP: annotated optical/SAR ship wakes (2026)](https://doi.org/10.1016/j.apor.2026.105245) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1016/j.apor.2026.105245) | SAR wake visibility is condition-dependent; the project already uses wake/hull labels and environmental information. | Abstract and author ESA poster. Publisher abstract and author poster inspected; not full journal methods. |
| [Physics-Driven Multi-Modal Fusion for SAR Ship Detection Under Motion Defocusing (2026)](https://doi.org/10.3390/rs18081166) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/rs18081166) | Uses signal-derived physical features, not weather metadata; defocusing is an alternative explanation for distorted ship appearance. | Sections 3 and 5: intensity/TFD/RID fusion and limitations. Publisher-indexed method excerpts; direct page returned 429. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Adapt a compact detector using wind/wind-quality channels with learned gating and missing-input indicators. Evaluate real quality strata separately from synthetic lag/noise experiments; phase errors are not simulated by ordinary image blur.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

xView3 documents 500 m wind and wind-quality rasters, but a licensed, aligned scene subset is not yet secured. UEIKAP is CC BY 4.0 and lists AIS/image directories; environmental field availability and scene alignment inside its imagery archives remain uninspected.

**Original sources:** [xView3: Dark Fishing Detection with SAR Imagery and AIS Data (2022)](https://arxiv.org/abs/2206.00897); [UEIKAP author dataset](https://doi.org/10.5281/zenodo.18391027).

**Fallback and claim boundary:** Use xView3 image-only versus quality-channel models on a bounded accessible subset. If quality fields are unavailable, synthetic missingness alone supports a narrower input-robustness study.

**Unmeasured resource estimate:** Estimate: 8–12 GB GPU, 16–32 GB RAM and 20–80 GB storage for selected scenes. No raw-complex SAR reconstruction, simulation platform or continuous weather API is required.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: reliability fusion | Can a learned gate recognise harmful metadata? H: It avoids performance loss at low wind quality. | Train gated image/environment fusion. | Image-only, concatenation and metadata dropout; remove quality gate. | Recall conditional on recorded quality and missingness. |
| B: training under input errors | Which training perturbations transfer? H: Physically bounded missing/lag scenarios outperform unrestricted noise. | Train uncertainty-aware metadata augmentation. | Ordinary augmentation and dropout; remove lag/quality constraints. | Real-quality-stratum transfer versus synthetic-only gains. |
| C: confidence under environmental shift | Can confidence remain reliable across wind-quality groups? H: Group-aware calibration limits overconfident false alarms. | Fit a small source-only calibration head. | Global temperature scaling; remove quality grouping. | Calibration and threshold-transfer errors across groups. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** Small-ship recall at a fixed scene-area or chip false-positive budget, reported separately for available real wind-quality groups.
- **Split:** Hold out complete acquisitions and, if supported, regions/seasons. Fit metadata transformations and calibration only on training/development scenes.
- **Baselines:** Compact image-only detector, straightforward metadata concatenation, dropout fusion and a gated-fusion modern control; physics-driven defocus fusion is a conceptual neighbour, not a weather baseline.
- **Ablations:** Quality channel, gate and training perturbations separately; missing versus stale versus noisy inputs; image-only lower-dependency control.
- **Uncertainty and error analysis:** Scene-block bootstrap and repeated seeds; evaluate sea clutter, tiny ships, nearshore scenes and metadata resolution. Report whether recorded quality actually predicts errors.
- **Useful findings without outperforming the strongest baseline:** Demonstrate no useful environmental signal at the available resolution, or quantify when image-only detection is preferable.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 70.8/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

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
| Compute/storage | 5 | 4 | 4.0 | Medium: Bounded subsets and occasional GPU use appear manageable; storage/time estimates are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **70.8** | **Not qualified.** |

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

**Next decision point:** Inspect one licensed xView3 scene with its quality raster; require real quality variation before claiming practical metadata reliability.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
