[← Research candidates](../research-candidates.md)

# Estimating vessel length when AIS size labels may be wrong

**ID:** X28 · **Area:** Computer vision — SAR vessel measurement · **Status:** Provisional opportunity; not qualified

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

AIS-reported length is a convenient training target but is not guaranteed correct. SAR motion defocus changes visible extent, creating a second explanation for size-estimation error.

## 2. Research gap and question

**Question:** Can robust length regression identify sensitivity to corrupted AIS size labels while separating that effect from observable image degradation?

**Tentative hypothesis:** A robust heteroscedastic model reduces error under specified label-corruption patterns better than ordinary regression.

**Rival explanation:** Clipping extreme labels or using a robust loss is sufficient; the uncertainty output does not identify actual incorrect AIS reports.

**What is already addressed / what remains inferred:** Satellite length estimation and physical defocus compensation already exist. The proposed contribution concerns label reliability, not first length prediction. Without independent dimensions, natural AIS label errors and true physical accuracy cannot be verified.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [Satellite mapping reveals extensive industrial activity at sea (2024)](https://doi.org/10.1038/s41586-023-06825-8) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1038/s41586-023-06825-8) | Reported size errors, small-vessel sensitivity and service/pleasure-craft confusion constrain interpretation; spatial splits and class-prior tests already exist. | Methods: length/fishing models, spatial splits; limitations. Full text and dataset documentation inspected. |
| [Physics-Driven Multi-Modal Fusion for SAR Ship Detection Under Motion Defocusing (2026)](https://doi.org/10.3390/rs18081166) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/rs18081166) | Uses signal-derived physical features, not weather metadata; defocusing is an alternative explanation for distorted ship appearance. | Sections 3 and 5: intensity/TFD/RID fusion and limitations. Publisher-indexed method excerpts; direct page returned 429. |
| [xView3: Dark Fishing Detection with SAR Imagery and AIS Data (2022)](https://arxiv.org/abs/2206.00897) | AIS/manual annotation provenance and wind-quality inputs; does not make unreported vessels illegal. | Original paper: dataset, labels and auxiliary rasters. Full paper inspected in this session. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Train a compact crop regressor with robust losses and label-uncertainty modelling. Separate known synthetic target corruption from natural target disagreement. Avoid claiming to identify bad reports solely because they disagree with a model trained on the same reports.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

GFW CC BY 4.0 presence/length data and manifests were checked in the earlier audit. AIS lengths remain the target, not an independent reference. No adequately sized existing independent registry/manual length set has been secured.

**Original sources:** [GFW Nature training data](https://doi.org/10.6084/m9.figshare.24309469).

**Fallback and claim boundary:** Conduct a controlled corruption study on a high-consistency subset and report agreement with its reference labels. This narrows the claim; it does not prove more accurate physical vessel measurement.

**Unmeasured resource estimate:** Estimate: cached crop features, CPU regressors or an occasional 8 GB GPU; 5–20 GB storage. Raw SAR phase reconstruction is outside scope.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: robust targets | Which robust objective tolerates structured target errors? H: Group-aware robust loss beats ordinary Huber loss. | Train noise-tolerant length regression. | L1/L2/Huber baselines; remove group weighting. | Error under prespecified synthetic label errors. |
| B: degradation-aware estimation | Does visible image quality predict length error? H: Quality-conditioned regression improves bounded measurement agreement. | Train a small quality-conditioned regressor. | Image-only regressor; remove quality branch. | Error by measurable sharpness/extent strata, without claiming physical defocus ground truth. |
| C: interval reliability | Can intervals remain calibrated under target corruption? H: Robust residual modelling improves coverage at matched width. | Fit heteroscedastic/quantile regression and calibration. | Quantile and split-conformal controls; remove robust target model. | Coverage/width under controlled contamination. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** MAE in metres against an independent existing reference if secured; otherwise MAE/interval coverage against explicitly synthetic-corruption reference targets only.
- **Split:** Group repeat observations by vessel and acquisition; hold out regions if metadata permit. Never create evaluation truth by selecting labels because they agree with the final model.
- **Baselines:** Length/size feature regression, compact CNN, Huber regression and heteroscedastic or quantile regression; reproduce published GFW length features where released.
- **Ablations:** Loss, uncertainty and quality branch independently; random versus size-dependent corruption; measured image-quality strata separate from simulated blur.
- **Uncertainty and error analysis:** Vessel-block bootstrap and seeds; analyse small vessels, extreme reported dimensions, repeated-report consistency and image extent. Distinguish target disagreement from true length error.
- **Useful findings without outperforming the strongest baseline:** Show that uncertainty tracks image difficulty but not label error, or demonstrate that no physical-accuracy conclusion is possible with the available references.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 65.3/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

### Weighted rubric

Nine relative weights total 98; scores are normalised to 100. Decimal precision is arithmetic, not confidence.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: Specific failure is testable, but overlap with the cited neighbours remains unresolved; no certified novelty. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: Required independent labels or historical observations have not been secured. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: Completion depends on resolving data or methodological prerequisites early. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: Losses, trainable fusion/state models or calibration are substantive ML investigations. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: Evaluation for the stronger real-world claim needs independent references; controlled tests support less. |
| Three-member structure | 12 | 4 | 9.6 | Medium: Three related model investigations can each use an unchanged common baseline; data dependencies remain explicit. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: A specific observation/identity error affects maritime research; operational benefits remain untested. |
| Compute/storage | 5 | 4 | 4.0 | Medium: Bounded subsets and occasional GPU use appear manageable; storage/time estimates are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **65.3** | **Not qualified.** |

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
| 8. Objective evaluation | Unknown | Independent outcome/reception/event references are not secured; only a narrower controlled endpoint is currently definable. |
| 9. 6–8 month feasibility | Unknown | Data prerequisites must be resolved before completion in 6–8 months can be supported. |
| 10. Three connected contributions | Pass | Each member has a question, trained intervention, baseline/ablation and attributable result; all can use unchanged common features/models. |
| 11. No specialised/continuous high-end compute | Pass | Core design excludes raw global ingestion, new hardware and continuous high-end or multi-GPU pretraining; estimates appear in section 5. |
| 12. Manageable data reuse | Pass | The bounded public-data route uses a verified CC BY 4.0 release; source attribution and label interpretation remain required. |
| 13. Useful negative findings | Pass | Section 7 defines useful findings if the intervention loses or the stronger claim is not identifiable. |

**Next decision point:** Secure independent existing dimensions before retaining a real-world measurement claim. Otherwise score and scope it strictly as controlled label-noise research.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
