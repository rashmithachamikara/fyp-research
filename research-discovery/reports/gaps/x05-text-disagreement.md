[← Research candidates](../research-candidates.md)

# Rare-emotion uncertainty from limited and disagreeing text annotations

**ID:** X05 · **Area:** NLP / multi-label learning / uncertainty · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

A majority-vote emotion label hides disagreement, especially for rare co-occurring labels. Recent work already models annotator distributions and shows that hard-label calibration and distribution fidelity can move in opposite directions.

**Potential stakeholders:** Annotation teams and NLP developers working with subjective, multi-label datasets.

## 2. Research gap and question

**Tentative gap:** Study finite-vote uncertainty for multi-label emotion probabilities when training annotations are reduced and the source community changes. Marginal probabilities for co-occurring labels must not automatically be forced into a single categorical distribution. Soft-label learning itself is established.

**Research question:** Can vote-count-aware shrinkage and label-dependence learning preserve rare-label probability quality under reduced annotation budgets and held-out Reddit communities?

**Hypothesis and rival explanation:** Accounting for the finite number of votes will reduce rare-label overconfidence without erasing minority labels. Rival explanation: simple class balancing or ordinary soft-label BCE explains the entire gain.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [Uncertainty Decomposition via cSG-MCMC, 2026](https://arxiv.org/html/2605.24773v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2605.24773) | Frozen RoBERTa heads, soft targets and multiple uncertainty axes on GoEmotions. | Use as a strong small-compute baseline; finite-vote multi-label marginals and community transfer need explicit comparison. | Full text; methods, setup and limitations; Sections 3–5; Limitations (X05-L1) |
| [Crowd-Calibrator, 2024](https://arxiv.org/html/2408.14141v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2408.14141) | Disagreement-aware calibration and selective prediction. | Do not claim disagreement-aware rejection is new; distinguish finite-vote and rare-label behaviour. | Full text; Sections 2–5 (X05-L2) |
| [Quality and Agreement in Multilabel Emotion Annotation, 2026](https://arxiv.org/html/2606.21069v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2606.21069) | Multilabel annotation behaviour and aggregation choices. | Specific shrinkage and transfer protocol needs deeper method-level differentiation. | Full text located; abstract/framework inspected; Abstract and evaluation framework (X05-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2605.24773,10.48550%2FarXiv.2408.14141,10.48550%2FarXiv.2606.21069). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Cache a generic frozen text encoder's features. Train vote-count-aware probabilistic heads and a small dependency model. Fit calibration on source-only validation communities. Evaluate each label as a Bernoulli marginal; only use a normalised distribution metric when the label representation genuinely warrants it.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary source | [Original GoEmotions README](https://github.com/google-research/google-research/tree/master/goemotions) and the [Google dataset release](https://huggingface.co/datasets/google-research-datasets/go_emotions). |
| Required version | Use raw per-rater CSVs, with comment, rater, author, thread and subreddit fields. The agreement-filtered 43,410/5,426/5,427 split is insufficient on its own for raw disagreement analysis. |
| Access and licence | Original Google Storage loading commands and schema inspected; official dataset card declares Apache 2.0. Public release card is 28.3 MB across configurations, not a measured raw-CSV footprint. |
| Split and target caveats | Group comments by thread and author; hold out subreddits. Finite votes estimate annotator-population marginals, not a person's hidden emotion. No new annotation is required. |
| Resources, estimated | Frozen encoder plus small heads: 4–8 GB RAM, under 5 GB disk; one-off CPU or modest-GPU embedding extraction. Runtime unmeasured. |
| Fallback / prototype | Common-label subset with the reduced scope stated; local text probabilities and uncertainty display. Do not use a checkpoint already tuned on held-out GoEmotions comments. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: finite votes | Does vote-count-aware shrinkage improve probability estimation? H: Vote-count-aware shrinkage reduces rare-label overconfidence. | Train a beta-binomial-style or equivalent count-aware head. | Soft BCE; remove count/shrinkage terms. | Marginal Brier score versus number of votes. |
| B: co-occurrence | Does a learned dependence term help rare joint labels? H: Dependency learning improves co-occurring label probability estimates. | Train a small structured dependency component. | Independent heads; remove dependency edges. | Rare/co-occurring label recall and probability error. |
| C: transfer calibration | Can source-only pooling improve community-held-out confidence? H: Partial pooling improves held-out-community calibration. | Fit partially pooled label/group calibrators. | Global temperature/vector scaling; remove pooling. | Worst-community calibration and selective risk. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Macro-average marginal Brier score against full held-out per-rater vote proportions; report rare-label strata and vote-count uncertainty.
- **Split:** All votes for one comment stay together; group by thread and author, and hold out communities. Fit encoders/heads/calibrators only on permitted source partitions.
- **Baselines and code:** TF–IDF logistic regression, the [original BERT baseline](https://github.com/google-research/google-research/blob/master/goemotions/bert_classifier.py), frozen RoBERTa soft-BCE heads and cSG-MCMC-head reimplementation from its paper; exact cSG-MCMC checkpoint availability unverified.
- **Ablations:** Finite-vote shrinkage, dependency term and calibration pooling; hold model, annotation count and class weighting fixed. Simulate reduced training votes without reducing the full test reference.
- **Uncertainty and errors:** Training seeds plus nested comment/thread and rater resampling where assignments support it. Stratify by label frequency, co-occurrence, vote count and community.
- **Useful result without winning:** Find where aggregate accuracy or a categorical normalisation hides poor marginal probabilities for rare co-occurring emotions.
- **Interpretation limit:** A few votes cannot identify a precise universal emotion distribution. Existing social-media labels do not validate mental-state, hiring or clinical inference.

## 8. Score and next decision

**Provisional score: 75.9/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 3/5; the required rating is 4/5. 1 mandatory gate(s) remain Unknown.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Low-medium: closely related soft-label and multilabel-aggregation studies exist; finite-vote/source-transfer novelty is provisional. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: original per-rater schema, grouping fields and official release licence support the target; raw reconstruction is pending. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: frozen features and small heads fit the schedule; statistical handling of sparse votes requires care. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: probabilistic heads, dependency learning and transfer calibration are substantive model investigations. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: marginal metrics and grouped votes address key confounders; small vote counts and community sizes limit inference. |
| Three-member structure | 12 | 4 | 9.6 | Medium: vote modelling, label dependence and calibration have separate controls within one predictor. |
| Real-world significance | 9 | 3 | 5.4 | Medium-low: relevance to annotation-aware NLP is clear; no end-user benefit is demonstrated by acted/text emotion benchmarks. |
| Compute/storage | 5 | 5 | 5.0 | Medium-high: cached features and small heads make the core CPU-feasible; costs are estimates. |
| Prototype | 3 | 4 | 2.4 | Medium-high: a local probabilistic text demo is bounded. |
| **Normalised total / 100** | **98** |  | **75.9** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Pass | Section 5 records an original public release or author-documented loading route, existing labels and the access-check limit. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Unknown | Closest 2026 multilabel and uncertainty methods need a detailed finite-vote/transfer comparison. |
| 7. Beyond application assembly | Pass | Section 6 investigates learned interventions with baseline comparisons and ablations, rather than application assembly. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Pass | The bounded core and fallback in Section 5 are plausible within the team window; training costs remain estimates. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Pass | Section 5 records source terms and a bounded offline use; no deployment or high-stakes benefit is assumed. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** A manageable text-learning lead; requires a sharper novelty argument.

**Next decision point:** Reconstruct raw votes and leakage-safe groups, then compare the finite-vote likelihood with ordinary soft BCE before introducing dependence or calibration. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
