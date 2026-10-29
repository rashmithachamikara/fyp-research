[← Research candidates](../research-candidates.md)

# Load forecasts using the weather forecast available at the time

**ID:** X36 · **Area:** Time series — electricity demand and uncertainty

**Status:** Provisional; Investigate; archive alignment and novelty unresolved; not qualified · **Imported:** 30 October 2026

**Provisional score:** 73.7/100 · No model training or timing performed.

**In plain language:** Test demand forecasts and prediction intervals with real archived weather forecasts, not future observed weather.

**Origin:** supplied shortlist, rank 3, page(s) 4–5. Its source verdict was “GO with reframing”. This brief uses the team’s current criteria; the source rank and verdict are not our qualification decision. [Import record](../../metadata/pdf-shortlist-import.json).

## 1. Problem

Tomorrow’s electricity demand depends on tomorrow’s weather. At forecast time, the actual future temperature is unknown. Testing a model with the weather that later occurred can make its forecast look more useful than it would have been.

## 2. Research gap and question

**Question:** When future weather inputs are replaced by archived forecasts issued before the electricity forecast, which compact adaptation best preserves demand accuracy and interval coverage?

**What is still uncertain:** The PDF proposes real issued-weather experiments rather than simulated errors, plus interval recalibration. Recent work already benchmarks forecasting under uncertain covariates. The precise extra contribution, including archived forecasts and uncertainty methods, still needs a full duplication search. This differs from TS2-R, which concerns meter outages.

**Hypothesis and alternative:** A learned correction using past weather forecast errors will improve interval sharpness at similar coverage. Alternatives are that a simple seasonal model is sufficient or that a foundation model gains nothing from weather inputs.

## 3. Evidence from closest work

This is a bounded import check, not a complete novelty audit. “Checked” below refers to the stated abstract or source page, not a reproduction of the study. The supplied PDF’s wider search and verification claims are not independently certified.

| Source | What it supports | Reading limit |
|---|---|---|
| [Benchmarking Time Series Foundation Models for Load Forecasting Under Covariate Uncertainty](https://arxiv.org/abs/2610.07232) | The abstract reports that forecasting performance changes with the quality of future covariates; real issued-weather and interval details require methods review. | Primary abstract checked; methods not reviewed. |
| [Open-Meteo Previous Model Runs API](https://open-meteo.com/en/docs/previous-runs-api) | The documentation describes fixed lead-time offsets and model-specific archive start dates. Exact issue-time alignment remains to be checked. | Official documentation checked; API sample not downloaded. |
| [ERCOT Hourly Load Data Archives](https://www.ercot.com/gridinfo/load/load_hist) | The official hourly-load archive is an access lead; files have not been joined to weather data. | Official source page checked; data files not sampled. |

## 4. Proposed approach

Start with one ERCOT load zone and a fixed day-ahead issue time. Compare no weather, observed future weather as a clearly labelled upper-bound diagnostic, simulated weather error and actual archived forecasts. Train a small correction or adapter, then calibrate intervals using past residuals only.

**Prototype:** demonstrate the same research pipeline on held-out existing examples, showing its output, errors and uncertainty. The interface is supporting work, not an individual research contribution.

## 5. Data and resources

**Data and access:** ERCOT lists hourly load archives. Open-Meteo documents fixed 1–7-day lead-time offsets; most models start in January 2024, while GFS temperature extends to March 2021. This establishes plausible source routes, not a completed joined dataset. Check actual issue/availability times, time zones, daylight-saving changes, spatial matching and free-use terms.

**Resources:** Estimate only: one zone over overlapping archive years should fit ordinary storage and CPU baselines. Use one small pretrained forecasting model with occasional GPU adaptation if needed. No guaranteed 500 GPU-hours or paid API access is assumed.

**Fallback:** Use a shorter overlapping archive period and a simpler learned forecaster. If only observed weather or artificial forecast noise is available, do not claim realistic issued-weather evaluation.

These are feasibility estimates, not demonstrated training costs. The PDF’s resource allowance does not establish this team’s actual GPU or paid-service access.

## 6. Three-member contributions

All members address the shared question in section 2. Each investigation starts from the same unchanged baseline so that another member’s proposed improvement is not a prerequisite.

| Member | Question and hypothesis | Method, comparison and removal test | Independently assessable result |
|---|---|---|---|
| A: Weather-error adaptation | Can past forecast errors improve day-ahead inputs? H: a trained correction beats raw issued weather. | Compare raw weather, rolling bias correction and a learned correction; remove lead-time features. | Demand error attributable to weather correction under chronological evaluation. |
| B: Forecast adaptation | Does weather-aware small-model adaptation help? H: a covariate adapter improves on an unchanged model. | Compare seasonal/boosted-tree baselines, unchanged foundation model and equal-budget adaptation; remove weather inputs. | MAE by horizon and season at a matched training budget. |
| C: Reliable intervals | Can rolling calibration stay useful in unusual weather? H: past-weather-conditioned calibration improves interval scores. | Compare fixed residual intervals, rolling conformal calibration and learned residual scaling; remove conditioning. | Interval score, coverage and width, including extreme-weather periods. |

Shared data access is a common prerequisite. A failed proposed method can still produce an interpretable comparison. Papers are optional; the work must remain attributable through experiments and removal tests. Where the gate table marks the team structure Unknown, the shared data barrier prevents treating this as an execution-ready split.

## 7. Evaluation

- **Primary measure:** Mean absolute error for day-ahead load, with weighted interval score as the uncertainty endpoint. Report nominal versus observed coverage and interval width; wide intervals alone are not a success.
- **Keep data separate:** Rolling chronological train/validation/test windows. Every weather input and residual used for calibration must have been available at the forecast issue time; never randomly split hours.
- **Baselines:** Weekly seasonal naive, gradient-boosted trees, a conventional neural forecaster and Chronos-2 or another covariate-capable foundation model. Confirm the exact checkpoint, input support, licence and small-run memory first.
- **Removal tests:** use the member-specific tests above; keep data, tuning effort and inference budgets comparable.
- **Uncertainty, error analysis and useful negative findings:** Analyse forecast lead time, heat/cold episodes, season and load level. Bootstrap by week rather than independent hours and repeat trainable models with three seeds. A useful negative finding could show that archived weather removes an apparent foundation-model advantage.
- **Claim limit:** benchmark findings support the stated task and conditions. They do not establish reliable real-world deployment or a guaranteed benefit for users.

## 8. Score and next decision

**Provisional score: 73.7/100; not qualified.** Investigate; archive alignment and novelty unresolved. Ratings assess the imported proposal and access risks, not achieved results. Unknown gates block qualification; failed gates reject the current design regardless of score.

### Weighted rubric

The existing nine weights total 98. Scores are normalised to 100; decimals reflect arithmetic, not certainty. These comparison scores follow the existing provisional-scoring policy and do not override the gates.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: a concrete issued-weather contrast exists, but nearby covariate research may overlap. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium: both source routes are documented; the usable join and terms are not checked. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: one zone and small models offer a realistic bounded route, subject to archive validation. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: correction, adaptation and learned interval scaling involve training. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: chronological comparisons and interval metrics directly test the proposed claim. |
| Three-member structure | 12 | 4 | 9.6 | Medium: three connected investigations can use the same unchanged starting forecast. |
| Real-world significance | 9 | 4 | 7.2 | Medium: weather errors matter for demand planning; this is a benchmark study. |
| Compute/storage | 5 | 4 | 4.0 | Medium: bounded tabular data and CPU-first baselines should fit; no timing measured. |
| Prototype | 3 | 4 | 2.4 | Medium: a historical forecast replay can demonstrate the research. |
| **Normalised total / 100** | **98** | | **73.7** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 defines a concrete failure and affected users; its local magnitude is not measured. |
| 2. ML essential | Pass | The shared question concerns learned predictions rather than only an interface. |
| 3. Train/adapt models | Pass | The bounded design includes training or systematic model adaptation. |
| 4. Existing data accessible | Unknown | Source routes exist, but overlapping files and issue-time metadata were not sampled. |
| 5. No unavailable human evaluation | Pass | The retained plan uses existing labels and excludes new participants or expert labelling. |
| 6. Precise research gap | Unknown | Real-weather and interval additions need comparison with recent covariate benchmarks. |
| 7. Beyond application assembly | Pass | The proposal specifies learning experiments, comparisons and removal tests. |
| 8. Objective evaluation | Unknown | Correct forecast issue-time alignment and leakage-safe joins have not yet been demonstrated. |
| 9. 6–8 month feasibility | Unknown | The proposed 6–8 month scope depends on a successful bounded archive join. |
| 10. Three connected contributions | Pass | Three connected research questions have separate comparisons and attributable results. |
| 11. No specialised/continuous high-end compute | Pass | The retained scope starts with small models or cached features and no dedicated hardware. |
| 12. Manageable data reuse | Unknown | The exact combination of data, model and derivative-output reuse terms is not verified. |
| 13. Useful negative findings | Pass | Section 7 identifies useful findings even if the proposed method does not improve performance. |

**Next decision:** Validate one small load–weather join with exact issue times, then compare the full methods of the nearest forecasting benchmark with the supervisor.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source and import limits](../../metadata/pdf-shortlist-import.json)
