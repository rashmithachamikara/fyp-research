[← Research candidates](../research-candidates.md)

# Predicting when elephant fences are permeable to particular animals

**ID:** X19 · **Area:** Behavioural ML / time-varying elephant barrier crossing · **Status:** Conditional opportunity; local outcome data not secured

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

An electric fence is not a permanently closed line on a map. Udawalawe observations show different crossing methods and repeated use by particular elephants. Predicting crossing requires monitoring effort and changing barrier conditions, not simply counts of crossing photographs.

**Potential stakeholders:** Researchers studying barrier permeability and coexistence; no operational fence or electrical intervention is proposed.

## 2. Research gap and question

**Tentative gap:** Learn time-varying crossing probability conditional on monitoring effort, gate/fence state and individual history, then test unseen individuals and sites. Descriptions of crossing behaviour are not already validated forecasts.

**Documented versus inferred:** The fence study documents methods/timing and supplementary summaries. The predictive formulation is inferred. Protected-area studies already distinguish individual strategies, and fence ecology already treats permeability as context dependent.

**Research question:** Can an individual- and condition-aware model predict future crossing at monitored Sri Lankan fence sites better than a static barrier score or site/time baseline?

**Hypothesis and rival explanation:** History and barrier-state features improve future predictions after effort adjustment. Rival explanation: habitual crossers, camera placement and unequal recording duration explain apparent skill.

This is an AI-assisted research opportunity, not certified novelty. Sri Lankan geography alone is not an original contribution. Seasonal ranging, local passage, habitat suitability, reported conflict and migration are different targets.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [How did the elephant cross the fence?, 2025 issue / online 2024](https://zslpublications.onlinelibrary.wiley.com/doi/10.1111/acv.12982) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1111%2Facv.12982) | Observed Udawalawe crossings vary by individual, location and crossing method; fence voltage alone is insufficient. | Do not rediscover crossing behaviour; predict future crossing exposure with observation effort and held-out individuals. | Publisher abstract and supporting-information list; full methods not inspected; Abstract; supplementary figures and Table S1 (X19-L1) |
| [Strategies of protected-area use by Asian elephants, 2022](https://doi.org/10.1038/s41598-022-22989-1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1038%2Fs41598-022-22989-1) | Longitudinal Udawalawe observations reveal sex/state/social differences in protected-area use. | Individual reuse and observation effort can confound transfer; sightings are not complete trajectories. | Author manuscript selected Methods/Discussion and indexed data statement; Methods and Data availability; author manuscript (X19-L2) |
| [Fence Ecology, 2020](https://doi.org/10.1093/biosci/biaa103) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.1093%2Fbiosci%2Fbiaa103) | Framework for context-dependent fence effects. | Changing permeability is not new; distinguish local learning and validation. | Retrieved scholarly record; full text not inspected; HEC-D4R nearest neighbour (X19-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.1111%2Facv.12982,10.1038%2Fs41598-022-22989-1,10.1093%2Fbiosci%2Fbiaa103). The supplied 63-page review informed discovery; selected original sources were checked, not all 50 references. [Evidence ledger](../../metadata/evidence-ledger.csv) · [Search, access and review records](../../metadata/elephant-expansion-records.json).

## 4. Proposed approach

Fit a crossing occurrence/hazard model using complete site-time exposure and existing identity labels. Separately study crossing-method classification and transfer uncertainty. No photograph does not mean no crossing without verified camera operation and detection effort.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary lead | [Udawalawe fence-crossing study](https://doi.org/10.1111/acv.12982). The public supplement lists figures and a per-individual method summary; a complete licensed timestamped event/effort dataset was not located. |
| Required fields | Camera/site, timestamp, operating effort, crossing/non-crossing exposure, individual label, direction and barrier condition. Positive crossing events alone cannot estimate unconditional site-night crossing probability. |
| Existing annotations only | Use author-supplied identities and condition/method labels if legally obtained. No new installations, wildlife observations, voltage experiments or expert relabelling. |
| Bounded core / fallback | One park boundary. Conditional crossing-method analysis among recorded events is a possible reduced study, but changes the question and cannot validate a hazard forecast. Foreign data do not validate Sri Lankan fence behaviour. |
| Resources, estimated | CPU survival/mixed-effects/boosting, 16 GB RAM and 5–15 GB working storage; optional cached photo features. Corpus size and runtime unmeasured. |
| Prototype | Historical site-time probabilities and uncertainty with anonymised individuals; no operational fence control. |

**Access is a selection dependency.** No institutional partnership, free licensed local outcome corpus or author permission is assumed. No data-access request was sent. Resource figures are estimates; no model training or timing experiment ran. The bounded supplement audit inspected an archive listing and two GeoPackage schemas, not a complete ecological dataset.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: condition-aware forecast | Does barrier state improve time/site baselines? H: State features improve effort-adjusted future forecasts. | Train a time-varying occurrence/hazard model. | Static barrier/site/time models; remove state features. | Out-of-time predictive loss across all monitored exposure. |
| B: individual strategy | Can predictions transfer beyond habitual crossers? H: Partial pooling improves sparse/new-individual predictions. | Train hierarchical history or existing crossing-method models. | Pooled model and individual-frequency lookup; remove history. | Held-out-individual predictions; method accuracy conditional on crossing. |
| C: reliability under change | Can uncertainty identify unsupported conditions? H: Shift-aware calibration improves reliability versus pooled fitting. | Fit conditional calibration/abstention on a fixed baseline. | Global calibration and rarity score; remove shift features. | Brier/coverage and reliability by site/state, independent of A/B. |

One shared problem, three independently assessable contributions. Each intervention runs against an unchanged common baseline, so another member's method need not succeed first. Shared data/code/models are allowed; papers are optional. The team design is conditional on adequate existing data, not a reason to start new fieldwork.

## 7. Evaluation

- **Primary metric:** Brier score or survival log-loss at a predefined site-night horizon, conditional on monitoring. False alerts per monitored night require suitable non-crossing exposure.
- **Split:** Forward blocks and leave-individual/site-out sensitivity; keep repeated frames of a crossing together. Few locations limit national inference.
- **Baselines:** Site/time frequency, logistic mixed-effects/survival model and gradient boosting; identical state/history availability for comparisons.
- **Ablations:** Barrier state, individual history and calibration separately; identity-free comparison for unfamiliar animals.
- **Uncertainty and errors:** Cluster bootstrap by individual/site and temporal blocks; analyse repeat crossers, unknown identities, gate/wire methods and state changes. Report wide intervals for few independent groups.
- **Useful result without winning:** Show that site rates and habitual individuals explain most gains, or that crossing-only records cannot support calibrated hazard prediction.
- **Interpretation limit:** Crossing prediction does not establish fence effectiveness, safe voltage or a causal reduction in conflict.

## 8. Score and next decision

**Provisional conditional score: 63.5/100.** This compares the current proposal design and access risks. It is not qualification or achieved model performance. Novelty is 3/5; dataset suitability and/or feasibility are below required thresholds. Four mandatory gates remain Unknown.

### Weighted rubric

Nine relative weights total 98; the final score is normalised to 100. Unresolved gates prevent qualification regardless of arithmetic.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: behaviour is documented; a distinct predictive method remains unverified. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: event/exposure data and photo terms are unsecured; summary counts are insufficient. |
| Feasibility and learning curve | 14 | 2 | 5.6 | Low: access, denominators and sparse independent sites are critical dependencies. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: hierarchical behaviour and time-varying models provide substantive ML investigations. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: objective tests exist, but operational negatives and independent sites may be insufficient. |
| Three-member structure | 12 | 4 | 9.6 | Medium: distinct methods each use the common baseline; B also yields a conditional-event result. |
| Real-world significance | 9 | 4 | 7.2 | Medium-high: permeability matters to coexistence research; intervention benefit is untested. |
| Compute/storage | 5 | 5 | 5.0 | Medium-high: event/tabular models fit CPU resources. |
| Prototype | 3 | 4 | 2.4 | Medium: historical replay is feasible if usable data are supplied. |
| **Normalised total / 100** | **98** | | **63.5** | **Not qualified; data access and gap verification required.** |

### Mandatory gates

Pass is supported at bounded design level only. The same provisional-comparison convention used in the existing table applies; unknown gates are not waived and these entries are not admitted as qualified projects.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the Sri Lankan source studies establish a concrete problem; proposed benefits remain untested. |
| 2. ML essential | Pass | Learning or adapting a predictive model is central, not an optional app feature. |
| 3. Train/adapt models | Pass | Sections 4 and 6 define trainable models/objectives; no paid inference service is required. |
| 4. Existing data accessible | Unknown | Complete event/exposure records, identity/state fields and image rights were not located; summaries are not a forecasting corpus. |
| 5. No unavailable human evaluation | Pass | The bounded design uses existing observations/annotations, without new questionnaires, fieldwork or expert labelling; access is assessed separately. |
| 6. Precise research gap | Unknown | The specific methodological distinction needs checking beyond the cited local studies and broader ecological ML work. |
| 7. Beyond application assembly | Pass | Model-level investigations and ablations go beyond integrating a detector or producing a map. |
| 8. Objective evaluation | Pass | Section 7 specifies an objective conditional evaluation, baseline controls and grouped uncertainty; it is not evidence those outcomes are currently available. |
| 9. 6–8 month feasibility | Unknown | Completion in 6–8 months depends on obtaining adequate existing data early; no partnership or access guarantee exists. |
| 10. Three connected contributions | Pass | Three related contributions can each run against a common unchanged baseline; no separate papers required. |
| 11. No specialised/continuous high-end compute | Pass | The bounded design uses CPU/cached features or an occasional modest GPU; new collars, cameras, microphones and field infrastructure are not required. |
| 12. Manageable responsible use | Unknown | Outcome-data reuse terms, precision restrictions and permitted sharing remain unresolved. |
| 13. Useful negative findings | Pass | Section 7 defines useful negative results and limits when a proposed model is not better. |

**Decision:** Interesting behavioural ML, conditional on author-held longitudinal records.

**Next decision point:** Inspect the event-and-exposure table; reject a hazard-forecast formulation if only crossing counts are available. Then discuss the evidence, ecological interpretation and individual contribution boundaries with the supervisor before committing.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Data feasibility audit](../../metadata/source-checks/elephant-data-checks.json).
