[← Research candidates](../research-candidates.md)

# Forecasting reported human–elephant conflict without learning reporting shortcuts

**ID:** X17 · **Area:** Spatiotemporal ML / Sri Lankan conflict-risk forecasting · **Status:** Conditional opportunity; local outcome data not secured

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Sri Lankan conflict mapping commonly uses officially reported incidents. Reporting differs across harm types and locations, and a static risk surface can perform well through geographic proximity without predicting when recorded incidents will occur.

**Potential stakeholders:** Researchers and agencies analysing recorded human–elephant conflict; this is not a system for allocating emergency responses.

## 2. Research gap and question

**Tentative gap:** Test next-month prediction of reported incidents under future-year and geographic holdouts, measuring sensitivity to reporting assumptions, background selection and incident type. True unreported conflict cannot be recovered from one biased source without additional identifying information.

**Documented versus inferred:** Gunawansa et al. describe differences in incident reporting. The 2026 LUCIS paper explicitly notes absent independent predictive validation. Combining these into a forecast-and-ascertainment investigation is an inferred gap; no claim is made that reporting correction or HEC forecasting is new.

**Research question:** Can a calibrated spatiotemporal model improve next-month reported-conflict forecasts beyond static proximity and seasonal baselines while remaining robust to plausible reporting and background-sampling assumptions?

**Hypothesis and rival explanation:** Dynamic features and a separate observation sensitivity model improve transferable predictions of recorded incidents. Rival explanation: improved scores mainly reflect administrative reporting intensity or leakage from nearby past events.

This is an AI-assisted research opportunity, not certified novelty. Sri Lankan geography alone is not an original contribution. Seasonal ranging, local passage, habitat suitability, reported conflict and migration are different targets.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Maxent conflict-risk mapping in Sri Lanka, 2024](https://doi.org/10.1016/j.apgeog.2024.103447) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1016%2Fj.apgeog.2024.103447) | A national spatial conflict-suitability model with elephant-range proximity as a major predictor. | Compare temporal forecasts and ascertainment sensitivity; a new Sri Lankan risk map alone is insufficient. | Publisher/indexed abstract; full methods not inspected; Abstract/highlights (X17-L1) |
| [Greenery change and HEC in Sri Lanka, 2023](https://doi.org/10.1080/01431161.2023.2244644) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1080%2F01431161.2023.2244644) | Relates satellite-derived cover/greenness to reported incidents; describes unequal reporting by incident type. | Mapping greenery is covered; distinguish lagged predictive value and observation bias. | Primary indexed full-text sections; direct publisher access limited; Sections 2.3–2.4 and limitations (X17-L2) |
| [Game theory-enhanced LUCIS planning in Sri Lanka, 2026](https://www.frontiersin.org/journals/sustainability/articles/10.3389/frsus.2026.1838933/full) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3389%2Ffrsus.2026.1838933) | Suitability overlap and modelled allocation scenarios; authors explicitly note missing independent predictive validation. | Test external outcomes rather than treating an improved planning index as reduced conflict. | Full text; source data, limitations and repository statement; Sections 2.1 and 4.5; Data availability (X17-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1016%2Fj.apgeog.2024.103447,10.1080%2F01431161.2023.2244644,10.3389%2Ffrsus.2026.1838933). The supplied 63-page review informed discovery; selected original sources were checked, not all 50 references. [Evidence ledger](../../metadata/evidence-ledger.csv) · [Search, access and review records](../../metadata/elephant-expansion-records.json).

## 4. Proposed approach

Use a bounded administrative-area/month panel with incident type preserved. Train an interpretable count or occurrence model and a boosted comparator. Analyse missing-reporting sensitivity and region-specific calibration; report conclusions about observed records unless independent reporting information is available.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary outcome leads | DWC-derived records used in the [2023 greenery study](https://doi.org/10.1080/01431161.2023.2244644) and [2026 planning study](https://doi.org/10.3389/frsus.2026.1838933). Original event-level data, timestamp precision, negative reporting periods and reuse terms are not secured. |
| Public repository audit | The [paper-linked LUCIS supplement](https://github.com/batlahiya/Supplementary-data-and-figures-for-the-LUCIS) README names HecIncidents.gpkg, but that exact path returned 404. The inspected 1.14 MB Overlays archive contains four overlap rasters; two inspected GeoPackages contain planning polygons, not an incident table. This is a partial audit, not proof that no author-held data exist. |
| Needed metadata | Event date at least monthly, location/administrative unit, harm type, reporting provenance and definition changes. Annual totals or figure points cannot support a claimed monthly event forecast. Multiple observation sources are needed to identify true reporting probabilities. |
| Bounded core / fallback | One region with several consecutive years; simple reported-count forecasting is the fallback if richer ascertainment data are unavailable. A static public map can support pipeline exploration only, not the proposed temporal claim. |
| Resources, estimated | CPU-first GAM/count, point-process or boosting models; 16 GB RAM and 5–20 GB feature/cache storage. No outcome corpus or training runtime measured. |
| Prototype | Historical forecast-versus-observed dashboard with uncertainty, incident definitions and reporting limitations; no live safety warning. |

**Access is a selection dependency.** No institutional partnership, free licensed local outcome corpus or author permission is assumed. No data-access request was sent. Resource figures are estimates; no model training or timing experiment ran. The bounded supplement audit inspected an archive listing and two GeoPackage schemas, not a complete ecological dataset.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: temporal forecasting | Do seasonal/environmental features improve future recorded counts? H: Lagged dynamic inputs beat static proximity on future months. | Train a boosted/count model with time-aware features. | Seasonal climatology, persistence and static MaxEnt/logistic risk; remove temporal features. | Held-out future-month predictive loss. |
| B: reporting sensitivity | Which conclusions survive different observation assumptions? H: Explicit ascertainment sensitivity exposes unstable apparent hotspots. | Train/evaluate positive-background or weighted observation models over predefined reporting scenarios. | Uniform background and unweighted model; vary effort proxies and assumptions. | Sensitivity bounds and hotspot/ranking stability, without claiming recovered true incidents. |
| C: transferable uncertainty | Can uncertainty remain reliable across districts? H: Region-aware calibration improves predictive intervals versus pooled fitting. | Fit group-aware calibration or count intervals on source validation only. | Global calibration and conventional count intervals; remove group adjustment. | Brier/coverage and worst-region error on common baseline predictions. |

One shared problem, three independently assessable contributions. Each intervention runs against an unchanged common baseline, so another member's method need not succeed first. Shared data/code/models are allowed; papers are optional. The team design is conditional on adequate existing data, not a reason to start new fieldwork.

## 7. Evaluation

- **Primary metric:** Held-out monthly count deviance or negative log-likelihood; for a preregistered occurrence target, Brier score and PR-AUC. Do not equate presence-background AUC with calibrated incident probability.
- **Split:** Train on earlier complete years, tune on a later year, lock a future year and a geographic block/district. Aggregate duplicate reports before splitting; maintain original temporal/geographic resolution.
- **Baselines:** Seasonal mean, lagged count, spatial GAM/negative-binomial model, static proximity/MaxEnt and gradient boosting. Compare the 2024 MaxEnt study only under equivalent targets; its validation protocol remains to be fully read.
- **Ablations:** Dynamic resource inputs, reporting/background treatment and calibration independently; vary administrative granularity without changing the target definition after seeing results.
- **Uncertainty and errors:** Block bootstrap by area/year; predictive intervals and scenario sensitivity. Analyse harm type, reporting-source changes, rare high-count months and low-record-density areas. Do not label unsurveyed periods as confirmed zero-conflict.
- **Useful result without winning:** Show that static exposure or reporting intensity explains apparent gains, or that geographic holdout performance collapses despite high random-split scores.
- **Interpretation limit:** The target is reported conflict. Causal effects of habitat change and reductions in human/elephant harm require separate evidence.

## 8. Score and next decision

**Provisional conditional score: 70.6/100.** This compares the current proposal design and access risks. It is not qualification or achieved model performance. Novelty is 3/5; dataset suitability and/or feasibility are below required thresholds. Four mandatory gates remain Unknown.

### Weighted rubric

Nine relative weights total 98; the final score is normalised to 100. Unresolved gates prevent qualification regardless of arithmetic.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: forecast validation is a concrete need, but reporting-aware ecological risk modelling has substantial prior work. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: relevant records exist in studies; a complete licensed monthly dataset is not verified in the public supplement. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: CPU scope is manageable, but access and ascertainment identifiability threaten completion. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: temporal, observation and uncertainty models support substantial empirical ML. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: forward/spatial splits and sensitivity analysis are appropriate; effective sample size is unknown. |
| Three-member structure | 12 | 4 | 9.6 | Medium: each contribution tests a common baseline independently. |
| Real-world significance | 9 | 5 | 9.0 | Medium-high: the recorded harm is directly relevant to people and elephants in Sri Lanka; model utility is unproven. |
| Compute/storage | 5 | 5 | 5.0 | Medium-high: tabular/count models can run on ordinary hardware. |
| Prototype | 3 | 4 | 2.4 | Medium-high: historical forecast dashboard fits team skills. |
| **Normalised total / 100** | **98** | | **70.6** | **Not qualified; data access and gap verification required.** |

### Mandatory gates

Pass is supported at bounded design level only. The same provisional-comparison convention used in the existing table applies; unknown gates are not waived and these entries are not admitted as qualified projects.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the Sri Lankan source studies establish a concrete problem; proposed benefits remain untested. |
| 2. ML essential | Pass | Learning or adapting a predictive model is central, not an optional app feature. |
| 3. Train/adapt models | Pass | Sections 4 and 6 define trainable models/objectives; no paid inference service is required. |
| 4. Existing data accessible | Unknown | A suitable licensed Sri Lankan event-level outcome dataset has not been secured; public predictor layers do not replace outcome labels. |
| 5. No unavailable human evaluation | Pass | The bounded design uses existing observations/annotations, without new questionnaires, fieldwork or expert labelling; access is assessed separately. |
| 6. Precise research gap | Unknown | The specific methodological distinction needs checking beyond the cited local studies and broader ecological ML work. |
| 7. Beyond application assembly | Pass | Model-level investigations and ablations go beyond integrating a detector or producing a map. |
| 8. Objective evaluation | Pass | Section 7 specifies an objective conditional evaluation, baseline controls and grouped uncertainty; it is not evidence those outcomes are currently available. |
| 9. 6–8 month feasibility | Unknown | Completion in 6–8 months depends on obtaining adequate existing data early; no partnership or access guarantee exists. |
| 10. Three connected contributions | Pass | Three related contributions can each run against a common unchanged baseline; no separate papers required. |
| 11. No specialised/continuous high-end compute | Pass | The bounded design uses CPU/cached features or an occasional modest GPU; new collars, cameras, microphones and field infrastructure are not required. |
| 12. Manageable responsible use | Unknown | Outcome-data reuse terms, precision restrictions and permitted sharing remain unresolved. |
| 13. Useful negative findings | Pass | Section 7 defines useful negative results and limits when a proposed model is not better. |

**Decision:** Strong problem relevance, conditional on a legitimate timestamped incident dataset and a narrower reporting claim.

**Next decision point:** Check the incident table itself for dates, harm definitions, coverage and licence before modelling; a repository README is insufficient evidence of availability. Then discuss the evidence, ecological interpretation and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Data feasibility audit](../../metadata/source-checks/elephant-data-checks.json).
