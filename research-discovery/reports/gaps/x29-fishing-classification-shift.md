[← Research candidates](../research-candidates.md)

# Separating fishing-vessel classification from local fleet shortcuts

**ID:** X29 · **Area:** Multimodal ML — vessel type classification · **Status:** Provisional opportunity; not qualified

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

Published satellite activity models combine estimated length with environmental context. Service and recreational vessels can resemble fishing vessels in these features, especially when the local vessel mix changes.

## 2. Research gap and question

**Question:** How do size-estimation error and local class-composition shift interact, and can a reliability-aware classifier avoid compounding their effects?

**Tentative hypothesis:** Separating uncertain size evidence from local class priors improves type classification under joint shifts.

**Rival explanation:** Existing class-prior correction already handles the effect, or apparent gains reflect AIS-label selection rather than classification robustness.

**What is already addressed / what remains inferred:** The GFW work already uses spatially buffered splits, ensembles and class-prior sensitivity tests. Geography splits or priors alone are not new. The proposed interaction study is inferred; the other two sources are adjacent label/selection evidence, not direct methodological predecessors.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [Satellite mapping reveals extensive industrial activity at sea (2024)](https://doi.org/10.1038/s41586-023-06825-8) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1038/s41586-023-06825-8) | Reported size errors, small-vessel sensitivity and service/pleasure-craft confusion constrain interpretation; spatial splits and class-prior tests already exist. | Methods: length/fishing models, spatial splits; limitations. Full text and dataset documentation inspected. |
| [Bias in AIS-based fishing-impact estimation (2025)](https://doi.org/10.1093/icesjms/fsaf033) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1093/icesjms/fsaf033) | AIS-based activity representation can be biased; this is adjacent evidence, not proof of a new satellite-classification gap. | Fishing-effort representation and bias. Primary abstract/indexed passages; complete methods not inspected. |
| [Tracking the elusive and shifting identities of the global fishing fleet (2023)](https://doi.org/10.1126/sciadv.abp8200) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1126/sciadv.abp8200) | Registry identity and AIS labels can change; adjacent evidence about target-label provenance, not a direct classifier baseline. | Vessel identity and registry linkage. Primary abstract inspected in earlier audit. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Train compact feature classifiers with uncertain-size inputs and explicit prior correction. Compare naturally observed regional mixes with controlled reweighting, and keep predicted size versus reference-reported size separate.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

Official CC BY 4.0 feature/label releases were checked; context feature archive is about 18.5 GB. The model uses context and estimated length, not necessarily hull imagery. Independent vessel-type labels for unmatched ships are not secured; AIS-labelled transfer is the presently defensible endpoint.

**Original sources:** [GFW Nature training data](https://doi.org/10.6084/m9.figshare.24309469); [GFW Nature analysis data](https://doi.org/10.6084/m9.figshare.24309475).

**Fallback and claim boundary:** Use a cached region/feature subset and restrict findings to vessels with existing type labels. Do not extrapolate classification accuracy to untracked vessels without reference labels.

**Unmeasured resource estimate:** Estimate: 32 GB RAM for selected feature extraction, CPU tree/MLP models or occasional 8 GB GPU; 30–80 GB including one archive/subset. No global image ingestion.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: uncertain size | Does treating length as uncertain improve class decisions? H: Probabilistic size features reduce errors under size shifts. | Train uncertainty-aware feature classification. | Tree/MLP with fixed size and size-free model; remove uncertainty. | Classification change by size-error stratum. |
| B: prior adaptation | Can local prior adjustment avoid context shortcuts? H: Validated prior correction beats naive regional context. | Fit prior-aware classifier using training/development groups. | Published prior-ratio controls and label-shift correction; remove context. | Error under observed and controlled class-composition changes. |
| C: subgroup reliability | Can confidence expose unsupported fleet types? H: Group-aware calibration reduces confident service/recreational misclassification. | Fit a compact reliability model. | Global calibration and reject threshold; remove subgroup features. | Calibration and selective error for labelled subgroups. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** Balanced accuracy and class-specific precision/recall on labelled vessels; report Brier score and service/recreational errors where labels permit.
- **Split:** Use published buffered geographic splits or stricter grouped equivalents; group repeat vessels. Vary size quality and class mix independently before their joint stress test.
- **Baselines:** Published GFW feature model if available; logistic/tree/MLP models, size-free controls, ensemble and prior-ratio/label-shift adjustment.
- **Ablations:** Size uncertainty, context removal and prior correction separately; fixed class mix versus shifted mix; identical labelled cohorts.
- **Uncertainty and error analysis:** Spatial/vessel block bootstrap; show cohort counts, size bands and label provenance. AIS type describes vessel function, not current fishing activity or legality.
- **Useful findings without outperforming the strongest baseline:** Demonstrate that prior correction suffices, or identify unsupported transfer from AIS-labelled to unmatched vessels.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 73.7/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

### Weighted rubric

Nine relative weights total 98; scores are normalised to 100. Decimal precision is arithmetic, not confidence.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: Specific failure is testable, but overlap with the cited neighbours remains unresolved; no certified novelty. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium-low: An original-source dataset route exists, but labels, access or evaluation support remain incomplete. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: Cached features/compact models fit a bounded design; execution remains estimated. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: Losses, trainable fusion/state models or calibration are substantive ML investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: Explicit grouped evaluation, controls and uncertainty are defined, conditional on the documented data checks. |
| Three-member structure | 12 | 4 | 9.6 | Medium: Three related model investigations can each use an unchanged common baseline; data dependencies remain explicit. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: A specific observation/identity error affects maritime research; operational benefits remain untested. |
| Compute/storage | 5 | 4 | 4.0 | Medium: Bounded subsets and occasional GPU use appear manageable; storage/time estimates are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **73.7** | **Not qualified.** |

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
| 9. 6–8 month feasibility | Pass | The cached-feature or compact-model route is a plausible 6–8 month design, not a demonstrated completion/runtime guarantee. |
| 10. Three connected contributions | Pass | Each member has a question, trained intervention, baseline/ablation and attributable result; all can use unchanged common features/models. |
| 11. No specialised/continuous high-end compute | Pass | Core design excludes raw global ingestion, new hardware and continuous high-end or multi-GPU pretraining; estimates appear in section 5. |
| 12. Manageable data reuse | Pass | The bounded public-data route uses a verified CC BY 4.0 release; source attribution and label interpretation remain required. |
| 13. Useful negative findings | Pass | Section 7 defines useful findings if the intervention loses or the stronger claim is not identifiable. |

**Next decision point:** Parse label/type provenance and feature joins; determine whether sufficient service/recreational examples exist for the proposed subgroup analysis.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
