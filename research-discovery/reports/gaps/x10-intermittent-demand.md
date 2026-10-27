[← Research candidates](../research-candidates.md)

# Intermittent-demand intervals that distinguish missing readings from zero sales

**ID:** X10 · **Area:** Time series / probabilistic forecasting · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Missing observations and genuine zero sales have different meanings for intermittent-demand forecasts. The Monash Car Parts archive releases both original missing values and a zero-filled variant, making their effects directly testable without collecting new business data.

**Potential stakeholders:** Spare-parts forecasting and planning analysts; inventory outcomes are outside this dataset.

## 2. Research gap and question

**Tentative gap:** Investigate missingness-aware occurrence/size modelling and pooled uncertainty after long observed zero runs. Probabilistic forecast combinations and zero-preserving feature engineering already exist; simply correcting preprocessing is insufficient for three research contributions.

**Research question:** Can a missingness-aware occurrence/size model with history-conditioned pooling improve prediction intervals for intermittent demand without treating unobserved sales as zero?

**Hypothesis and rival explanation:** Separating observation availability from zero demand will improve probability quality, particularly after long zero runs. Rival explanation: gains are purely a preprocessing correction or ordinary cross-series pooling rather than a new modelling contribution.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Combining Probabilistic Forecasts of Intermittent Demand, 2024 / preprint 2023](https://arxiv.org/html/2304.03092v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1016%2Fj.ejor.2024.01.032) | Distribution, bootstrap and ML forecasts, combinations and inventory trade-offs. | Probabilistic intermittent forecasts and combinations are occupied; compare explicit observation availability and conditional intervals. | Full preprint methods and evaluation; Sections 3–5 (X10-L1) |
| [Feature Engineering: Zero-Detection and Forecast Performance, 2026](https://doi.org/10.1007/s10845-026-02964-7) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1007%2Fs10845-026-02964-7) | Zero/nonzero diagnostic trade-offs on intermittent demand. | Aggregate forecast metrics can hide occurrence failures; uncertainty and missing-data semantics need comparison. | Primary indexed abstract/limitations; full methods not inspected; Publisher abstract; indexed limitations (X10-L2) |
| [Event-Preserving Feature Engineering Using SHOS, 2026](https://doi.org/10.1038/s41598-026-57129-6) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1038%2Fs41598-026-57129-6) | Preserves true zero-demand periods in feature engineering. | Preserving zeros is already argued; the proposed learned probability/interval method must add more. | Primary indexed publisher text; direct full page blocked; Indexed data preparation sections (X10-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1016%2Fj.ejor.2024.01.032,10.1007%2Fs10845-026-02964-7,10.1038%2Fs41598-026-57129-6). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Train a small two-part occurrence/positive-size model with an explicit observation mask. Investigate missingness-aware likelihood/training weights, pooled interval calibration and a learned history-based pooling policy. Treat the two archive variants as an audit comparison, not as independent validation datasets.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary sources | Monash [original Car Parts](https://zenodo.org/records/4656022) and [zero-filled variant](https://zenodo.org/records/4656021). Both API records and CC BY 4.0 licences checked. |
| Actually parsed | The 39,656-byte original ZIP contains 2,674 monthly series of length 51, with 6,122 missing markers and 97,398 observed zero entries. Counts and archive hash are in the metadata audit. |
| Labels and scope | Observed sales are the targets. No inventory, stockout, price or part-family metadata is assumed; do not infer unmet demand or obsolescence causes from zeros. |
| Temporal evaluation | Rolling origins; select models, calibration history and zero-run strata using only past observations. Exclude genuinely missing evaluation targets rather than calling imputations ground truth. |
| Resources, estimated | CPU boosting or a small global hurdle model, 2–8 GB RAM and under 2 GB disk. The source parsing is demonstrated; training time and model memory are unmeasured. |
| Fallback / prototype | Fewer series and shorter forecast horizons, retaining the original missingness flags; local intermittent-sales replay with intervals and observation availability. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: predictive distribution | Does observation-aware two-part training help beyond corrected preprocessing? H: Observation-aware predictive training improves on corrected-preprocessing baselines. | Train occurrence/positive-size heads with missingness-aware likelihood or weights. | Same clean preprocessing with ordinary hurdle/quantile model; remove mask-aware term. | Probability/quantile error by zero-run length. |
| B: interval updates | Can pooled calibration protect low-history series? H: Partial pooling improves low-history interval quality. | Fit history-conditioned partially pooled interval calibration. | Global and per-series rolling calibration; remove pooling. | Coverage/width across history and sparsity strata. |
| C: sharing policy | Can past-only similarity improve sharing without negative transfer? H: Past-only learned sharing reduces negative transfer. | Learn cross-series grouping or shrinkage weights from training histories. | Uniform/global pooling and static clusters; remove learned policy. | Worst-series trade-offs and negative-transfer cases. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Mean scaled weighted interval score over observed test targets, using training-only scaling and a predefined safeguard/report for all-zero training series. Report unscaled interval score as a sensitivity check.
- **Split:** Rolling-origin chronological train/selection/calibration/test periods. Series-group holdouts only if making a new-series claim; the core forecasts known series. Both archive variants use identical observed target indices.
- **Baselines and code:** Zero/seasonal-naive, Croston/SBA/TSB, zero-inflated or hurdle model, quantile LightGBM and scoring-rule forecast combinations. [StatsForecast](https://github.com/Nixtla/statsforecast) and the [Monash evaluation repository](https://github.com/rakshitha123/TSForecasting) are implementation routes.
- **Ablations:** Missingness-aware predictive term, interval pooling and learned sharing. Include zero-filled versus original-input variants while scoring only genuinely observed targets; match lags and training examples.
- **Uncertainty and errors:** Series-cluster and time-block resampling, several model seeds; coverage by past zero-run length, historical observation count, horizon and sparsity. Report near-zero interval collapse and nonzero-demand misses.
- **Useful result without winning:** Quantify when zero filling changes conclusions or when a simple occurrence/size model outperforms a more complex temporal model.
- **Interpretation limit:** Only 51 historical months per series and an old domain are available. No causal stockout, inventory-cost, modern retail or operational service-level claim is supported.

## 8. Score and next decision

**Provisional score: 80.2/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 3/5; the required rating is 4/5. 2 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Medium-low: paired-source semantics create a concrete study, but probabilistic pooling and zero-aware learning are established; model-level originality remains unresolved. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | High for access: original archive actually parsed and source licences checked; short histories and absent business covariates limit suitability. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium-high: tiny data and bounded CPU models fit the schedule; short-history calibration needs careful design. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: learned predictive distributions, calibration and pooling policy are substantive if they exceed a preprocessing fix. |
| Evaluation/reproducibility | 12 | 5 | 12.0 | Medium-high for design: identical observed targets, rolling origins and explicit zero/missing controls isolate the central issue. |
| Three-member structure | 12 | 4 | 9.6 | Medium: prediction, interval updating and learned sharing can be evaluated separately within one forecasting system. |
| Real-world significance | 9 | 4 | 7.2 | Medium: intermittent spare-part forecasting is consequential; data cannot establish actual stockout or inventory savings. |
| Compute/storage | 5 | 5 | 5.0 | High for data size, medium for models: parsing demonstrated and CPU fallback is small; training costs remain estimates. |
| Prototype | 3 | 4 | 2.4 | Medium-high: a local historical replay with missingness and intervals is bounded. |
| **Normalised total / 100** | **98** |  | **80.2** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Pass | Section 5 records an original public release or author-documented loading route, existing labels and the access-check limit. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Unknown | Distinct model-level gap beyond current intermittent-demand probability and combination work is unresolved. |
| 7. Beyond application assembly | Unknown | A preprocessing correction alone is insufficient; the learned likelihood/sharing contributions need stronger justification. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Pass | The bounded core and fallback in Section 5 are plausible within the team window; training costs remain estimates. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Pass | Section 5 records source terms and a bounded offline use; no deployment or high-stakes benefit is assumed. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** One of the strongest additional execution fits; the high score does not clear the novelty or contribution gates.

**Next decision point:** Compare a properly masked simple hurdle/quantile baseline with zero-filled inputs on identical observed rolling-origin targets; then retain only a demonstrated residual modelling failure. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
