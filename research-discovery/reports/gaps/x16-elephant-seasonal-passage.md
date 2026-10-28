[← Research candidates](../research-candidates.md)

# Forecasting seasonal elephant passage using changing water and crop conditions

**ID:** X16 · **Area:** Ecological ML / satellite time series and passage forecasting · **Status:** Conditional opportunity; local outcome data not secured

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

In Sri Lankan park–farmland mosaics, elephant use of human-dominated areas changes with season and social grouping. Existing seasonal associations do not by themselves show that remotely sensed changes can improve a genuinely future forecast of a recorded crossing.

**Potential stakeholders:** Conservation analysts and researchers studying park-edge coexistence; forecasts would require further validation before use for public warnings.

## 2. Research gap and question

**Tentative gap:** Predict passage during a predefined future week using only information available at forecast time, separating crop/water phenology from calendar seasonality and camera effort. The outcome is passage at monitored locations, not an island-wide migration trajectory.

**Documented versus inferred:** The Wasgamuwa study establishes seasonal/nocturnal passage patterns and requests data access through SLWCS. The added predictive question and missing-data treatment are inferred opportunities. The supplied review makes a similar proposal on p. 5, so that proposal itself is not independent evidence of novelty.

**Research question:** Do lagged crop-phenology and surface-water features improve next-week elephant-passage forecasts over calendar, persistence and static-proximity models at held-out Sri Lankan camera sites and seasons?

**Hypothesis and rival explanation:** Lagged resource-change features improve out-of-time passage predictions after accounting for active camera-days. Rival explanation: the model learns the month, repeated animals, camera uptime or harvest-calendar shortcuts.

This is an AI-assisted research opportunity, not certified novelty. Sri Lankan geography alone is not an original contribution. Seasonal ranging, local passage, habitat suitability, reported conflict and migration are different targets.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Asian elephant movements and crop damage, online 2022 / Oryx issue 2023](https://doi.org/10.1017/S0030605321000971) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1017%2FS0030605321000971) | Camera-trap passage varies with crop season and social group in Wasgamuwa. | Seasonality is established; test genuinely future passage prediction beyond calendar effects. | Full text; methods, discussion and access statement; Methods, Discussion and Data availability (X16-L1) |
| [Greenery change and HEC in Sri Lanka, 2023](https://doi.org/10.1080/01431161.2023.2244644) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1080%2F01431161.2023.2244644) | Relates satellite-derived cover/greenness to reported incidents; describes unequal reporting by incident type. | Mapping greenery is covered; distinguish lagged predictive value and observation bias. | Primary indexed full-text sections; direct publisher access limited; Sections 2.3–2.4 and limitations (X16-L2) |
| [Strategies of protected-area use by Asian elephants, 2022](https://doi.org/10.1038/s41598-022-22989-1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1038%2Fs41598-022-22989-1) | Longitudinal Udawalawe observations reveal sex/state/social differences in protected-area use. | Individual reuse and observation effort can confound transfer; sightings are not complete trajectories. | Author manuscript selected Methods/Discussion and indexed data statement; Methods and Data availability; author manuscript (X16-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1017%2FS0030605321000971,10.1080%2F01431161.2023.2244644,10.1038%2Fs41598-022-22989-1). The supplied 63-page review informed discovery; selected original sources were checked, not all 50 references. [Evidence ledger](../../metadata/evidence-ledger.csv) · [Search, access and review records](../../metadata/elephant-expansion-records.json).

## 4. Proposed approach

Build a camera-site/week panel with active monitoring effort. Compare a seasonal count/rate model with gradient boosting and a compact temporal encoder only if sample size supports it. Inputs must be historic composites that would actually have existed at the forecast date.

## 5. Data and resources

| Item | Current position |
|---|---|
| Outcome source / access | The [Wasgamuwa Oryx study](https://doi.org/10.1017/S0030605321000971) states that data requests go to SLWCS. Timestamped passages, station IDs and operating-effort logs have not been acquired. Existing study data are a lead, not confirmed public access. |
| Available predictors | [Copernicus Sentinel-2 documentation](https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel2.html) provides an optical-imagery route. Optical cloud gaps and acquisition times need auditing; satellite greenness is not a direct forage measurement. |
| Label requirements | Passage direction, timestamp, social-group label if available, camera/site and active effort including zero-passage periods. If individual identity is unavailable, claim group passage, not individual routes or unique elephant counts. |
| Bounded core / fallback | One landscape and a next-week horizon, retaining enough complete seasons for temporal testing. A calendar-versus-dynamic comparison on existing passages is the fallback. Non-Sri Lankan data can test code but cannot validate the Sri Lankan claim. |
| Resources, estimated | CPU-first feature extraction and boosted models; optional 8–12 GB GPU for a small temporal encoder; 16 GB RAM and 10–30 GB local working data. No imagery, passage corpus or runtime was measured. |
| Prototype | Weekly probability/rate map for historical replay with missing-data indicators; no live wildlife alerting. |

**Access is a selection dependency.** No institutional partnership, free licensed local outcome corpus or author permission is assumed. No data-access request was sent. Resource figures are estimates; no model training or timing experiment ran. The bounded supplement audit inspected an archive listing and two GeoPackage schemas, not a complete ecological dataset.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: dynamic resource features | Do resource changes add information beyond month? H: Lagged water/crop changes improve future passage prediction. | Learn temporal resource representations or nonlinear interactions. | Calendar/persistence/static predictors; remove water and crop features separately. | Out-of-time predictive gain and feature ablation, without B/C. |
| B: incomplete observations | Can a model remain useful when optical images are cloudy or irregular? H: Missingness-aware fusion avoids treating stale imagery as current. | Train time-since-observation and missingness-aware features or a small encoder. | Forward-fill/seasonal imputation; remove image-age information. | Predictive loss under held-out real missing-data patterns. |
| C: transfer reliability | Do forecast scores transfer to new sites/seasons? H: Group-aware calibration improves reliability beyond pooled calibration. | Fit hierarchical calibration or predictive intervals using source validation only. | Global calibration and seasonal count model; remove group pooling. | Brier/interval coverage and worst-site errors on fixed baseline outputs. |

One shared problem, three independently assessable contributions. Each intervention runs against an unchanged common baseline, so another member's method need not succeed first. Shared data/code/models are allowed; papers are optional. The team design is conditional on adequate existing data, not a reason to start new fieldwork.

## 7. Evaluation

- **Primary metric:** Brier score for at-least-one-passage in the next week, with PR-AUC and calibration; use count deviance separately if event counts and effort are trustworthy.
- **Split:** Forward-chaining seasons and held-out complete camera sites; keep bursts/repeated identifiable animals grouped where possible. Never randomly split nearby observations or use future cloud-free composites.
- **Baselines and code:** Persistence, month-of-year climatology, negative-binomial/GAM with effort offset, and gradient boosting. Compact temporal models are a stronger optional comparison, not a foundation-model training requirement.
- **Ablations:** Calendar versus static versus dynamic resources; crop, water, image age and calibration individually; match forecast horizon and data availability.
- **Uncertainty and errors:** Block bootstrap by site/season and repeated small-model seeds. Report male/family-group results only if labels support them, camera effort, cloud gaps and rare high-passage weeks.
- **Useful result without winning:** Show that calendar and active effort explain most of the apparent satellite gain, or identify when cloud gaps make the dynamic model worse.
- **Interpretation limit:** Passage forecasting does not establish migration, crop damage, safe movement or reduced conflict.

## 8. Score and next decision

**Provisional conditional score: 64.9/100.** This compares the current proposal design and access risks. It is not qualification or achieved model performance. Novelty is 3/5; dataset suitability and/or feasibility are below required thresholds. Four mandatory gates remain Unknown.

### Weighted rubric

Nine relative weights total 98; the final score is normalised to 100. Unresolved gates prevent qualification regardless of arithmetic.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: an explicit forecast question is plausible, but seasonal movement and dynamic habitat modelling are established. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: the relevant local camera outcomes and effort logs are request-only and unacquired. |
| Feasibility and learning curve | 14 | 2 | 5.6 | Low: access, number of independent seasons and ecological learning needs remain unresolved. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: temporal learning, missingness and calibration are model-level investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: forward/site holdouts are appropriate if enough independent observations exist. |
| Three-member structure | 12 | 4 | 9.6 | Medium: three methods each work against the same unchanged baseline. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: local passage is directly relevant to understanding farm-edge elephant use; warning benefit is unmeasured. |
| Compute/storage | 5 | 4 | 4.0 | Medium: CPU-first models and bounded image features fit the team if data are supplied. |
| Prototype | 3 | 4 | 2.4 | Medium-high: historical replay is straightforward. |
| **Normalised total / 100** | **98** | | **64.9** | **Not qualified; data access and gap verification required.** |

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

**Decision:** Conditional research opportunity; do not commit while passage/effort data are unsecured.

**Next decision point:** Verify an existing passage-and-effort dataset's access terms, timestamps, site coverage and number of independent seasons. Then discuss the evidence, ecological interpretation and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Data feasibility audit](../../metadata/source-checks/elephant-data-checks.json).
