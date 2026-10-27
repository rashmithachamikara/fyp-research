[← Research candidates](../research-candidates.md)

# Choosing anomaly detectors when sensor availability changes

**ID:** X08 · **Area:** Time series / anomaly detection / model selection · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

A detector that ranks well on one sensor stream need not be the best on another, and current unsupervised selectors can be far from an oracle. Missing channels can also alter reconstruction scores and alarm rates. The proposed selector's response to missing channels remains a hypothesis, not an already measured failure here.

**Potential stakeholders:** Industrial-monitoring developers and operators affected by missed faults and alarm burden.

## 2. Research gap and question

**Tentative gap:** Learn context-dependent detector selection or ensemble weights under changed sensor availability, while locking alarm calibration without test anomaly labels. Neither model selection nor low-false-alarm evaluation alone is new.

**Research question:** Can a selector trained on normal data and controlled proxy faults choose more useful detectors under sensor dropout than a fixed detector or static selector at the same false-alarm budget?

**Hypothesis and rival explanation:** Availability-aware proxy evaluation will reduce detector-selection regret after channels disappear. Rival explanation: a fixed robust detector or a simple median ensemble explains all gains, and synthetic proxy faults mis-rank real faults.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [mTSBench, 2025](https://arxiv.org/html/2506.21550v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2506.21550) | 24 detectors and MetaOD/FMMS/Orthus selection benchmarks; substantial selector gaps. | Appendix G proposes context-aware mixtures; investigate changed channel availability rather than another static ranking benchmark. | Full text; selection results and limitations; Sections 4.2–4.4; Appendix G (X08-L1) |
| [Causal Wavelet Residual Learning with Observation-Support Gating, 2026](https://doi.org/10.3390/s26185751) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.3390%2Fs26185751) | Normal-only causal detection, missingness, alarm burden and trade-offs. | A learned detector selector differs from a new residual detector; compare against this type of robust detector. | Scholarly abstract; methods not inspected; FastTrack X08-D1 neighbour (X08-L2) |
| [Low-False-Alarm Evaluation Changes the Ranking of Multisensor Anomaly Detectors, 2026](https://doi.org/10.55972/spectrum.v27i1.439) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.55972%2Fspectrum.v27i1.439) | Ranking dependence on low-false-alarm evaluation. | A fixed false-alarm regime is a required control, not a novelty claim. | Scholarly record/abstract only; methods not inspected; FastTrack X08-D1 neighbour (X08-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2506.21550,10.3390%2Fs26185751,10.55972%2Fspectrum.v27i1.439). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Build a pool of four or five small detectors. Generate proxy corruptions only from normal training data, fit a regularised selector, and investigate availability-conditioned ensemble weighting. Real test anomaly labels are reserved for the evaluator and an explicitly labelled oracle bound.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [SKAB author release](https://github.com/waico/SKAB): 34 anomaly experiments plus a normal-only file, eight sensor channels, anomaly/changepoint labels. |
| Actually checked | Original README, data-folder schema and first rows of valve1/1.csv inspected through GitHub. Columns confirm timestamps, sensors and two label fields. |
| Licence and scope | Repository release is GPL-3.0; retain its terms when using/distributing code or data. One physical testbed and few independent faults limit claims about general industrial monitoring. |
| Split | Reserve whole experiments/fault groups before windows; fit normalisation and thresholds on normal training/calibration blocks. Repeated masks from one experiment are not independent test cases. |
| Resources, estimated | CPU-first small models, 8 GB RAM and under 5 GB working data. Small TCN/GRU training can use occasional GPU; wall time and full data footprint unmeasured. |
| Fallback / prototype | Three detectors and one dropout family; retain independent experiment holdouts. Offline alarm timeline with selected model and false-alarm counts. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: proxy validity | Which proxy corruptions predict real-detector ranking? H: Learned proxy weights predict real detector rankings better than uniform proxies. | Learn constrained proxy-fault weights using training normals only. | Uniform proxy mix and score agreement; remove learned weights. | Proxy-to-held-out-fault rank correlation. |
| B: selector | Does availability conditioning improve detector choice? H: Availability features reduce selection regret after channel loss. | Train a small regularised selection/ranking model. | Fixed detector/static selector; remove channel-availability features. | Selection regret on unseen experiments. |
| C: ensembles | Can constrained mixtures be more stable than choosing one model? H: Constrained mixtures improve stability over selecting one model. | Learn availability-conditioned detector weights. | Uniform/median ensemble and winner-take-all; remove weight constraints. | Recall–false-alarm trade-offs and weight stability. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Event recall at a predeclared calibration false-alarm budget; report realised false-alarm events per normal hour on test separately, without retuning.
- **Split:** Whole experiments and fault families disjoint; causal windows, no point adjustment, no test-label threshold selection and no labelled test anomalies in selector fitting.
- **Baselines and code:** PCA/Isolation Forest, causal TCN and GRU autoencoder; fixed best-source detector, random/static selection and median ensemble. [mTSBench code](https://github.com/PLAN-Lab/mTSBench) supplies modern selector references; reproduce their prerequisites or label an omission.
- **Ablations:** Proxy weighting, availability features and ensemble constraints; match detector pool, missing-data treatment and calibration access.
- **Uncertainty and errors:** Experiment-cluster bootstrap plus detector/selector seeds; report each fault family, dropout pattern, detection delay and missed events. Use raw scores and label access logs.
- **Useful result without winning:** Identify when proxy faults give misleading rankings, or when a single robust detector beats a complex selector.
- **Interpretation limit:** A single testbed cannot validate general industrial reliability. Fixed calibration thresholds do not guarantee future false-alarm control under shift.

## 8. Score and next decision

**Provisional score: 74.7/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 3/5; the required rating is 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Low-medium: context-aware selection is motivated by a documented limitation, but the availability-specific method needs a stronger distinction. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium: source CSV schema, labels and repository terms checked; only one testbed and few independent fault experiments. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: capped detector pool and CPU-first selector fit the schedule; modern selector reproduction needs a bounded configuration. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: proxy learning, trained selection and constrained ensembles are research rather than a monitoring dashboard. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: causal calibration and experiment grouping address common leakage; few independent events widen uncertainty. |
| Three-member structure | 12 | 4 | 9.6 | Medium: proxy validity, selector and ensemble learning can be assessed independently with a shared score cache. |
| Real-world significance | 9 | 4 | 7.2 | Medium: false alarms and missed faults are consequential; operational savings are not demonstrated. |
| Compute/storage | 5 | 5 | 5.0 | Medium-high: small CPU models and bounded normal/proxy data fit; no timing experiment performed. |
| Prototype | 3 | 4 | 2.4 | Medium-high: an offline multichannel alarm replay is bounded. |
| **Normalised total / 100** | **98** |  | **74.7** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Pass | Section 5 records an original public release or author-documented loading route, existing labels and the access-check limit. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Unknown | Need to distinguish the availability-aware selector from current context-aware selection and gating methods. |
| 7. Beyond application assembly | Pass | Section 6 investigates learned interventions with baseline comparisons and ablations, rather than application assembly. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Pass | The bounded core and fallback in Section 5 are plausible within the team window; training costs remain estimates. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Pass | Section 5 records source terms and a bounded offline use; no deployment or high-stakes benefit is assumed. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** A practical CPU-first methods/evaluation lead, limited by independent-data diversity.

**Next decision point:** Reproduce one normal-only detector and compare proxy rankings with evaluator-only real-fault rankings on disjoint experiments before training a selector. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
