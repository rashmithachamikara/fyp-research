[← Research candidates](../research-candidates.md)

# Load forecast uncertainty during meter outages

**ID:** TS2-R · **Area:** Time series / uncertainty / missing data · **Status:** Verify gap

**Evidence reviewed:** 27 October 2026

## 1. Problem

Missing meter readings can damage a load forecast. They can also remove the observations needed to check past predictions and update their uncertainty intervals.

A system that assumes immediate feedback may therefore appear better calibrated in an offline experiment than it could be with the same missing observations in operation.

## 2. Research gap and question

**Established:** missing-data forecasting, conformal intervals and adaptive calibration already exist.

**Gap to investigate:** uncertainty updates when outages interrupt both historical inputs and the later outcomes needed for calibration, including delayed, batched and permanently unavailable feedback.

**Research question:** Can a missingness-aware forecaster and observation-aware calibration update maintain useful intervals during controlled outages and chronological distribution change?

**Novelty status:** unresolved. The closest incomplete-time-series paper may already cover the proposed distinction. Delayed feedback alone is not a new contribution.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Incomplete-time-series conformal prediction, TMLR 2026](https://openreview.net/forum?id=KMBU4wx79B) | Temporal dependence and structured missingness | Whether its assumptions cover unavailable calibration outcomes | Abstract; full text unavailable |
| [Conformal Prediction with Missing Values, 2023](https://arxiv.org/abs/2306.02732) | Missingness-pattern-dependent uncertainty | A causal time-series feedback schedule | Abstract |
| [Online Conformal Prediction with Corrupted Feedback, 2026](https://arxiv.org/html/2605.20515v1) | Robustness to feedback errors | Distinguish missing/delayed outcomes from corrupted feedback | Full-text sections |
| [Missing-data-aware load forecasting, 2026 issue](https://www.sciencedirect.com/science/article/pii/S0306261925019397) | Learning directly from incomplete load histories | Uncertainty updates when outcomes are unavailable | Publisher text and section snippets |
| [Adaptive Probabilistic Forecasting of Electricity (Net-)Load](https://doi.org/10.1109/TPWRS.2023.3310280) | Adaptive probabilistic load forecasting | A distinct observation-schedule method, rather than ordinary adaptive intervals | Scholarly abstract/metadata |

The unresolved closest-paper comparison prevents a defensible novelty claim.

## 4. Proposed approach

Train a small missingness-aware load predictor. Add a calibration update that uses only outcomes actually available at each forecast origin. Investigate whether sharing calibration across clients helps scarce-history clients.

Maintain a timestamped feedback ledger. An imputed target must never be treated as an observed outcome for calibration.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary data | [UCI ElectricityLoadDiagrams20112014](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014) |
| Verified access | Original download, licence and documented loading route checked |
| Contents | 370 client series; quarter-hourly measurements during 2011–2014 |
| Licence | CC BY 4.0 |
| Size | Approximately 249.2 MB compressed; 678.1 MB text |
| Compute | CPU-first quantile boosting or a small temporal model |
| Fallback | 20–50 clients with hourly aggregation |
| Unverified | Payload parsing, training time and the closest paper's feedback assumptions |

**The source contains no missing values.** Outages would be deliberately masked experiments, not observed outage records. Handle pre-activation zeros and daylight-saving conventions separately from missingness.

Measurements are in kW at quarter-hour intervals. Preserve the distinction between hourly average power and energy when aggregating. A smaller client subset reduces compute; it is not an independent validation dataset.

A bounded core is estimated to need 2–8 GB RAM and under 10 GB of processed data. Those resource figures have not been measured.

**Prototype:** local historical replay showing forecasts, intervals, observation availability and calibration update timing.

## 6. Three-member contributions

| Member | Research question | Method investigation | Assessable result |
|---|---|---|---|
| A: forecasting | Do missingness and time-since-observation features protect forecast quality? | Mask-aware temporal or quantile predictor | Error and interval-score sensitivity to outage patterns |
| B: feedback | Can calibration remain useful while outcomes are unavailable? | Observation-aware residual weighting and delayed updates | Coverage, width and recovery after gaps |
| C: sharing | Can pooled calibration help scarce-history clients without hiding failures? | Shrinkage between global, client and missingness-group calibration | Worst-client coverage and conditions where pooling harms |

All three contributions address the same forecasting problem and can use a shared forecaster, dataset and evaluation pipeline. Contribution-specific comparisons should establish each member's work. Separate papers are not required; paper writing and publication are optional.

## 7. Evaluation

- **Primary metric:** interval score at a predefined 90% nominal level.
- **Secondary metrics:** coverage, width, peak-period forecast error, recovery time and worst-client coverage.
- **Baselines:** seasonal naive, lag regression, quantile boosting and a small temporal model; fixed, rolling and adaptive interval calibration.
- **Split:** chronological training, selection, calibration and test periods; additional client holdouts for transfer claims.
- **Ablations:** missingness features, observation-aware updates and calibration sharing.
- **Stress tests:** random missingness, contiguous blocks, simultaneous client gaps and predefined value-dependent masks.
- **Uncertainty:** repeated mask seeds, rolling-origin tests and week/client block resampling.
- **Useful negative result:** identify uncertainty methods that fail when their feedback assumptions are violated.

Do not infer real outage causes, grid topology or a universal coverage guarantee from this benchmark.

Start with 24-hour-ahead hourly forecasting. Fit scaling and imputation on training history only and update intervals only after outcomes are revealed. Compare input-only masking with input-plus-feedback masking; outcome-conditioned masks are oracle stress tests, not causal models of outages. Report coverage beside interval score because a better score can hide worse undercoverage.

## 8. Score and next decision

**Provisional score: 72.7/100.** Scored for comparison at the team's request before gate clearance. Gates 6 and 7 remain Unknown; this is not a qualified shortlist score. Overall assessment confidence is medium-low, principally because the closest paper's methods remain inaccessible.

### Weighted rubric

Scoring updated: **28 October 2026**. The nine weights total **98**; weighted points below are out of 98 and the total is normalised to 100.

Ratings assess the current proposal using the module's revised nine-category rubric. Unknowns reduce the relevant ratings; they are not assumed to pass. Shared models and infrastructure are acceptable, and papers are optional.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---:|---:|---:|---|
| Research gap and defensible novelty | 16 | **2** | 6.4 | Low: section 3 identifies close incomplete-series and feedback methods; a distinct methodological addition is not established |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: section 5 documents public UCI data, licence and loading route; synthetic outages limit representativeness and payload parsing is pending |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: CPU-first forecasting and a reduced client panel bound execution; conformal methods and feedback replay require learning and a pilot |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: learned prediction, residual weighting and calibration sharing support substantial experiments; originality is assessed separately |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: section 7 specifies chronological replay, feedback availability, baselines and block resampling; outage realism and implementations remain untested |
| Three-member structure | 12 | 4 | 9.6 | Medium: section 6 defines attributable forecasting, feedback and sharing investigations within one system; individual comparisons need to be fixed before experiments |
| Real-world significance | 9 | 3 | 5.4 | Medium: incomplete load forecasts are a documented problem, but controlled masks cannot establish actual outage or operational benefits |
| Compute/storage | 5 | 5 | 5.0 | Medium: the small tabular dataset and 20–50-client CPU fallback provide ample scope control; RAM and wall time remain estimates |
| Prototype | 3 | 4 | 2.4 | Medium-high: local historical replay fits the team's backend skills and needs no live meter integration |
| **Normalised total / 100** | **98** | | **72.7** | **Provisional only: novelty is below 4/5 and gates 6 and 7 are unresolved** |

### Mandatory gates

Pass means a bounded design is supported by current evidence; it is not a completed experimental result. Unknown gates prevent qualification, even when a provisional comparison score is provided.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | documented incomplete-load forecasting problem |
| 2. ML essential | Pass | forecasting and learned uncertainty |
| 3. Train/adapt models | Pass | train quantile/temporal predictors |
| 4. Existing data accessible | Pass | original UCI download/licence/loading route checked |
| 5. No unavailable human evaluation | Pass | hidden complete outcomes for controlled masks |
| 6. Precise research gap | Unknown | closest paper's feedback setting unverified |
| 7. Beyond application assembly | Unknown | proposed extension may reduce to established methods |
| 8. Objective evaluation | Pass | causal replay, coverage and interval score |
| 9. 6–8 month feasibility | Pass | bounded CPU-first panel |
| 10. Three connected contributions | Pass | forecasting, feedback updating and calibration sharing |
| 11. No specialised/continuous high-end compute | Pass | CPU-first core |
| 12. Manageable responsible use | Pass | CC BY 4.0 anonymous client series; no individual inference |
| 13. Useful negative findings | Pass | causal uncertainty failures |

**Decision:** retain as a discussion reserve. The current design is potentially viable, but 72.7 is below 75 and novelty is 2/5. If novelty alone were defensibly raised to 4/5, the arithmetic would become 79.2; that is a sensitivity calculation, not a promised improvement or qualification.

**Next decision point:** inspect the closest TMLR paper's methods and supplement. Establish a distinct contribution before running a small causal replay pilot.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Evidence ledger](../../metadata/evidence-ledger.csv).
