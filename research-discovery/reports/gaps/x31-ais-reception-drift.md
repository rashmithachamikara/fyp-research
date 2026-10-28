[← Research candidates](../research-candidates.md)

# Updating AIS-gap anomaly models when reception coverage changes

**ID:** X31 · **Area:** Time-series ML — AIS reception and satellite corroboration · **Status:** Provisional opportunity; not qualified

**Evidence reviewed:** 28 October 2026. This is a source-grounded candidate question, not a certified novel gap. No model was trained or runtime measured.

## 1. Problem

GFW documentation states that reception-quality estimates use 2017–2019 data pending automated updates. Later changes in reception can therefore affect the interpretation of AIS reporting gaps.

## 2. Research gap and question

**Question:** Can a compact time-adaptive reception model reduce false gap anomalies under receiver-coverage drift compared with static reception filters?

**Tentative hypothesis:** Updating background reception estimates from other vessels improves later-period reception prediction and gap-score reliability.

**Rival explanation:** Changing traffic/transmission behaviour explains the apparent drift; a rolling frequency baseline performs as well as learned adaptation.

**What is already addressed / what remains inferred:** Reception-aware gap rules, expected-reception self-supervision and AIS reception GNNs already exist. The graph study itself calls for temporal extensions. The proposed opportunity is a bounded later-period drift comparison, not first distinguishing reception from disabling.

## 3. Evidence from closest work

| Source | Supported observation or overlap | Reading limit |
|---|---|---|
| [GFW API data caveats](https://api-doc.globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats) | Documentation says reception quality uses 2017–2019 data pending automated monthly updates; gaps have duration/distance/reception filters. | AIS gaps: reception quality and thresholds. Official documentation inspected 2026-10-28. |
| [Hot spots of unseen fishing vessels (2022)](https://doi.org/10.1126/sciadv.abq2109) | Gap screening already accounts for reception; event screening does not supply independent intent labels. | Methods: reception filters and AIS-gap events. Primary full-text passages inspected. |
| [Detecting Intentional AIS Shutdown using Self-Supervised Learning (2023)](https://arxiv.org/abs/2310.15586) | Expected-reception self-supervision already exists; the large Norwegian source feed is not verified freely reusable. | Methods and data access. Author PDF inspected in earlier audit. |
| [Attention-Aware Graph Neural Network Modeling for AIS Reception Area Prediction (2025)](https://doi.org/10.3390/s25196259) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390/s25196259) | Model is described as temporally agnostic and geographically bounded; private receiver data and heavy training limit direct reuse. | Sections 4.2, 5.4 and 6. Publisher-indexed method/conclusion passages; direct page returned 429. |

The table distinguishes documentary evidence from the proposed method. Sparse duplication-search returns do not establish originality; full comparison of unresolved neighbours remains required.

## 4. Proposed approach

Train a compact reception model using other-vessel/background observations and time adaptation. Keep receiver changes, vessel transmission changes and traffic density as rival explanations. Satellite presence may corroborate a vessel's location, but cannot reveal shutdown intent.

**Prototype:** An offline viewer showing source observations, baseline versus proposed outputs, confidence and grouped errors. Its UI is a demonstration, not an individual research contribution.

## 5. Data and resources

Public GFW derived gap documentation and analysis routes exist, but raw multi-year messages with reliable receiver provenance and independent outage labels are not secured. Bernabé's large feed and the GNN study's private antenna are not assumed accessible. API eligibility is not the same as downloaded historical data.

**Original sources:** [GFW API data caveats](https://api-doc.globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats); [GFW Nature analysis data](https://doi.org/10.6084/m9.figshare.24309475).

**Fallback and claim boundary:** Use an existing licensed regional track set for controlled reception-loss experiments. Such experiments test reception robustness, not real intentional disabling; without message exposure, stop the stronger topic.

**Unmeasured resource estimate:** Estimate: CPU boosted trees/small temporal model, 16–32 GB RAM, 10–50 GB selected logs; no receiver hardware. The published two-RTX8000/100-hour GNN training is excluded.

The source audits checked metadata/manifests and the HOSS archive, not every image or baseline. [This pass’s dataset checks](../../metadata/source-checks/maritime-expansion-data-checks.json) and [the earlier satellite data checks](../../metadata/source-checks/satellite-ais-data-checks.json) preserve what was inspected.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: temporal reception | Does online adaptation beat a stale map? H: A compact temporal model improves later-period prediction. | Train a time-adaptive background reception model. | Static map, rolling frequency and self-supervised predictor; remove adaptation. | Later-period prediction and calibration. |
| B: exposure confounding | Can traffic exposure be separated from reception loss? H: Exposure-normalised learning avoids traffic-driven false gaps. | Train exposure-adjusted missingness model. | Raw message-count model; remove normalisation. | Error under traffic and controlled receiver changes. |
| C: anomaly reliability | Can updated reception improve gap-score interpretation? H: Reception-aware calibration reduces false alarms on supported outage references. | Fit a reception-conditioned anomaly/calibration head. | Welch-style filters and fixed threshold; remove reception update. | Calibration or controlled false-alarm rate, not inferred intent. |

One shared problem with three independently assessable contributions. Each experiment uses a common unchanged baseline, so another member’s proposed method need not succeed first. Missing existing labels remain an access prerequisite, not an invitation to collect new data. Papers are optional.

## 7. Evaluation

- **Primary metric:** Brier/log loss for future reception on adequately observed cells; false gap-anomaly rate only for independently labelled or explicitly simulated reception losses.
- **Split:** Forward-chaining months/years and held-out geographic/receiver groups. Exclude the target vessel from its contemporaneous background estimate and prevent future-message leakage.
- **Baselines:** GFW/Welch static reception rules, rolling frequency, compact boosted model, expected-reception self-supervision and a small temporal variant; no need to reproduce the heavy private-data GNN.
- **Ablations:** Time adaptation, exposure adjustment and calibration independently; controlled receiver dropout versus traffic changes; satellite corroboration reported separately if available.
- **Uncertainty and error analysis:** Time/receiver-block intervals; analyse low traffic, coastal/offshore areas, receiver outages and vessel hardware/transmission effects. AIS reception gaps do not provide intent labels.
- **Useful findings without outperforming the strongest baseline:** Show that a rolling count baseline suffices, or quantify inability to distinguish reception loss from transmission changes with the available data.
- **Interpretation:** Visible presence, visual identity, vessel type, co-location and AIS-reporting anomalies are different targets. None alone labels a vessel illegal or establishes intentional AIS disabling.

## 8. Score and next decision

**Provisional score: 66.3/100. Not qualified.** Ratings assess the current topic design, not achieved performance or the truth of its hypothesis. The novelty rating is 3/5; all Unknown gates must be resolved before selection.

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
| Compute/storage | 5 | 5 | 5.0 | Medium-high: Cached-feature/CPU experiments are plausible; no runtime or peak memory measured. |
| Prototype | 3 | 4 | 2.4 | Medium: An offline evidence/error viewer is feasible; the prototype is not the research contribution. |
| **Normalised total / 100** | **98** | | **66.3** | **Not qualified.** |

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
| 12. Manageable data reuse | Unknown | Dataset imagery/API terms remain to verify for the exact intended subset. |
| 13. Useful negative findings | Pass | Section 7 defines useful findings if the intervention loses or the stronger claim is not identifiable. |

**Next decision point:** Locate a genuinely reusable historical feed with exposure/receiver information. Do not use a vessel-disabling classification endpoint without independent labels.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Search, duplication and rejection records](../../metadata/maritime-expansion-records.json).
