[← Research candidates](../research-candidates.md)

# Dengue forecasts that know when weather data is unhelpful

**ID:** X45 · **Area:** Time series — reported dengue cases in Sri Lanka

**Status:** Provisional research opportunity; not qualified · **Checked:** 30 October 2026

**Score:** 73.7/100, provisional · **No model has been trained or timed.**

**The idea:** Forecast reported cases using past counts, and add weather information only when it helps rather than making the forecast worse.

## 1. Problem

A district forecast may use rainfall and temperature to predict reported dengue cases. Missing or poorly matched weather data can make a more complicated model worse. Local planners could benefit from a forecast range that reflects this uncertainty, but benchmark work alone cannot establish public-health benefit.

**Example:** If rainfall data are absent for several weeks, the model should not treat a filled-in average as a real observation. It can fall back to past case patterns and show a wider forecast range.

## 2. Research gap and question

**Question:** For one- to four-week forecasts of reported dengue counts, can a small model learn when to use weather and when to rely on case history, while keeping its prediction ranges useful?

**Already done:** Sri Lankan dengue forecasting already has many models. A 2026 district study found that a temporal model beat its graph model and documented missing climate data for Jaffna. Another general forecast dashboard is not the contribution.

**What to investigate:** Investigate weather usefulness under genuine and clearly labelled simulated missingness. Compare a learned choice between count-only and weather-aware forecasts with always using weather, simple data filling and fixed fallback rules. Whether this adds beyond existing forecasting methods is unresolved.

**Prediction to test:** Learning when weather helps will reduce forecast errors under missing inputs. Alternatively, a count-only model or a fixed missing-data rule may remain better and simpler.

## 3. Evidence from closest work

| Source | Why it matters | What was checked |
|---|---|---|
| [denguedatahub maintainer repository](https://github.com/thiyangt/denguedatahub) | The maintainer packages Sri Lankan weekly surveillance counts. A public CSV and the package licence were checked directly. | README, package DESCRIPTION and bounded full CSV parsed. |
| [When Spatial Message Passing Fails to Help](https://onlinelibrary.wiley.com/doi/10.1155/acis/2627876) | This Sri Lankan study documents a temporal baseline beating the tested graph model and a Jaffna climate-data limitation. | Primary full-text methods, limitations and conclusion inspected; no reproduction. |
| [NASA POWER daily data](https://power.larc.nasa.gov/docs/services/api/temporal/daily/) | Official documentation gives a route to historical weather, not a verified region-week join or a historical forecast-issue archive. | Official API documentation checked; no complete weather join. |
| [Sri Lanka dengue dashboard source](https://github.com/amalirajapaksha/denguedashboard_SriLanka) | The author explains that Ampara and Kalmunai reporting areas need reconciliation when making administrative-district maps. | Author README checked; demonstrates a mapping issue, not forecasting novelty. |

The problem evidence and the proposed solution are different things. No baseline failure or improvement has been demonstrated by this project. The searches do not prove novelty. [Search and data-check record](../../metadata/sri-lanka-practical-checks.json).

## 4. Proposed approach

Start with weekly reported counts. Join existing historical gridded weather only after checking region mapping and dates. Train count-only and weather-aware models, plus a small selection model using past information. Calibrate a prediction range on past errors; a range should widen when evidence is weak.

**Simple prototype:** show a held-out example, the baseline answer, the proposed answer and any uncertainty. Building the screen is supporting work, not a member’s research contribution.

## 5. Data and resources

**Existing data:** The maintainer’s denguedatahub CSV was downloaded and parsed: 26,311 rows, years 2006–2026, and 26 reporting-area names, including Ampara and Kalmune. These are not 26 administrative districts. The file has week/date fields and reported case counts. No blank case fields were found, but missing weeks, revisions and source extraction accuracy are not yet audited. The package declares GPL-3; original surveillance-data reuse terms need confirmation.

**What the team needs:** Estimate: CPU models and a small sequence model should be sufficient. NASA POWER provides an existing historical-weather route, but no complete weather join was downloaded or validated. No hospital partnership, individual patient records or clinical labelling is needed.

**Fallback:** Keep a useful count-only forecast as the starting result. If compatible weather or its timing cannot be established, limit claims to retrospective forecasting and do not present this as an operational early-warning system.

Costs and training times are estimates until measured. No paid services, new participants or guaranteed university GPU are assumed.

## 6. Three-member contributions

One shared problem, three testable contributions. Each can start from the same unchanged baseline; another member’s proposed method does not have to succeed first.

| Member | Question and prediction | Method, baseline and removal test | Separate result |
|---|---|---|---|
| A: Choosing weather inputs | When should weather be ignored? H: a learned choice beats always filling and using it. | Compare count-only, always-weather, fixed fallback and learned selection; remove missingness indicators. | Forecast error under real gaps and separately labelled artificial outages. |
| B: Sharing across areas | Does sharing patterns help smaller reporting areas? H: limited shared training improves weak-data forecasts. | Compare separate-area models and a pooled small model; remove area-specific adjustments. | Error by reporting area and case volume, against the unchanged starting model. |
| C: Useful forecast ranges | Can ranges stay reliable around unusual rises? H: rolling calibration improves coverage. | Compare fixed residual ranges and a learned residual-scale model; remove weather-quality inputs. | Range coverage, width and interval score by horizon and period. |

All members share data and evaluation code. Papers are optional. “Removal test” means taking out the proposed change to see whether it actually helped.

## 7. Evaluation

- **Main measures:** Mean absolute error in reported weekly cases, plus interval score, which penalises both missed outcomes and needlessly wide ranges. Show observed coverage for each stated forecast range.
- **Fair data split:** Use rolling chronological evaluation. Keep all areas on the same calendar cut-offs; never randomly split weeks. Harmonise reporting areas before joining data. Use only weather and reported cases available by the forecast date; if release histories are unavailable, label the test retrospective and add explicit delay sensitivity tests.
- **Comparisons:** Seasonal naive, a count regression/SARIMAX model, boosted trees and a small LSTM or temporal network. The recent graph-model study is an important comparison; a larger graph model is not automatically stronger.
- **Removal tests:** use the member-specific comparisons above and keep training/tuning budgets matched.
- **Uncertainty and useful failures:** Repeat trained models with three seeds and bootstrap whole time blocks. Report periods before, during and after major reporting disruption separately. Analyse small/large reporting areas, weather gaps and outbreak peaks. Useful findings include weather not helping or simple fallback rules matching the learned selector.
- **What the results cannot prove:** The outcome is reported cases, not all infections, individual illness, mosquito abundance or hospital demand. Filling missing weather cannot recover missing disease reports. Do not turn this benchmark into clinical advice.

## 8. Score and next decision

**Provisional score: 73.7/100; not qualified.** This is a promising practical direction, not a verified new gap. The score describes the plan; unknown gates still prevent selection.

### Weighted rubric

The existing nine weights total 98 and are normalised to 100. Ratings use the project’s provisional comparison policy. Decimal totals are arithmetic, not scientific certainty.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: a concrete weather-reliability question follows documented limitations; generic forecasting is crowded. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium: weekly counts were parsed, but reporting units, release timing and the weather join need audit. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: CPU-first models and aggregate public counts give a realistic bounded starting point. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: input selection, shared learning and range modelling involve training. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: chronological metrics are clear; operational claims remain unsupported without release histories. |
| Three-member structure | 12 | 4 | 9.6 | Medium: selection, shared learning and prediction ranges have separate comparisons. |
| Real-world significance | 9 | 4 | 7.2 | Medium: reported dengue trends are directly relevant locally; improved health outcomes are not demonstrated. |
| Compute/storage | 5 | 4 | 4.0 | Medium: small tabular series should fit ordinary hardware; no runtime measured. |
| Prototype | 3 | 4 | 2.4 | Medium: replay historical forecasts with ranges and missing-input indicators. |
| **Normalised total / 100** | **98** | | **73.7** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan. Unknown means evidence is still needed.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | A specific local task and evidence-backed limitation are described in sections 1–3. |
| 2. ML essential | Pass | The question tests learned predictions and model errors, not only an application. |
| 3. Train/adapt models | Pass | All three investigations train or systematically adapt models. |
| 4. Existing data accessible | Unknown | Case-count CSV access is demonstrated, but the weather join and reporting-area mapping are not verified. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing reference labels or aggregate counts; no new raters or recordings. |
| 6. Precise research gap | Unknown | The specific learned weather-selection contribution has not passed a complete duplication search. |
| 7. Beyond application assembly | Pass | The research is tested through comparisons and removal tests; the interface is supporting work. |
| 8. Objective evaluation | Unknown | Publication timing, revisions, missing weeks and climate alignment need an audit before operational forecasting claims. |
| 9. 6–8 month feasibility | Unknown | A count baseline and bounded weather join are needed to confirm the workload. |
| 10. Three connected contributions | Pass | Three connected questions have separate comparisons and results using a shared unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | The bounded plan uses CPU baselines and occasional modest GPU access, with no special hardware. |
| 12. Manageable data reuse | Unknown | The package licence is known; original surveillance-data terms and weather/model reuse require checking. |
| 13. Useful negative findings | Pass | Simple baselines winning or a proposed method failing still answers the stated questions. |

**Next decision:** Audit reporting-area/date consistency and one small weather join, then review whether the learned selector has a distinct contribution beyond simple baselines with the supervisor.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source checks](../../metadata/sri-lanka-practical-checks.json)
