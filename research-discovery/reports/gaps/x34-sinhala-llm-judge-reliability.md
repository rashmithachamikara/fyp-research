[← Research candidates](../research-candidates.md)

# Can an AI judge reliably score Sinhala answers?

**ID:** X34 · **Area:** NLP — Sinhala answer evaluation

**Status:** Provisional; Reject as written; needs existing human ratings; not qualified · **Imported:** 30 October 2026

**Provisional score:** 53.5/100 · No model training or timing performed.

**In plain language:** Check whether AI scores agree with human ratings of Sinhala answers, then adapt a smaller judge.

**Origin:** supplied shortlist, rank 1, page(s) 2–3. Its source verdict was “GO”. This brief uses the team’s current criteria; the source rank and verdict are not our qualification decision. [Import record](../../metadata/pdf-shortlist-import.json).

## 1. Problem

A team may use an AI model to mark Sinhala answers because human marking is expensive. A fluent but wrong answer could receive a high score, while a correct answer with different wording could receive a low one. This matters for evaluating Sinhala assistants; it does not establish that automated exam marking is safe.

## 2. Research gap and question

**Question:** On an existing human-rated Sinhala answer set, which judge errors come from language, answer length or presentation order, and can a small adapted judge reduce them?

**What is still uncertain:** The supplied PDF proposes a Sinhala human-versus-model comparison. That is a plausible investigation, but a new language alone is not enough to establish novelty. A reusable human-rated Sinhala test set has not been verified.

**Hypothesis and alternative:** Training a small judge on existing human scores will reduce ranking errors on unseen prompts. An alternative is that the apparent gain comes from memorising answer style or from disagreement in the human ratings.

## 3. Evidence from closest work

This is a bounded import check, not a complete novelty audit. “Checked” below refers to the stated abstract or source page, not a reproduction of the study. The supplied PDF’s wider search and verification claims are not independently certified.

| Source | What it supports | Reading limit |
|---|---|---|
| [How Reliable is Multilingual LLM-as-a-Judge?](https://aclanthology.org/2025.findings-emnlp.587/) | The study reports inconsistent judgments across languages, especially low-resource languages. This does not by itself demonstrate Sinhala judge-versus-human accuracy. | Primary abstract checked; methods not reviewed. |
| [SINHALA-GLUE lead supplied in the PDF](https://aclanthology.org/2025.acl-long.422/) | A source-supplied benchmark lead to inspect for task fit; it is not verified here as a human-rated generated-answer set. | Lead from supplied PDF; target methods/data not reviewed. |

## 4. Proposed approach

Start with one answer type, such as short factual explanations. Compare unchanged judges under matched prompts, then train a small ranking head or adapter. Keep answer order and length controlled. Do not use the model being tested to define the correct evaluation labels.

**Prototype:** demonstrate the same research pipeline on held-out existing examples, showing its output, errors and uncertainty. The interface is supporting work, not an individual research contribution.

## 5. Data and resources

**Data and access:** The PDF proposes 300–500 new instructions, answers from several models and three native-speaker ratings per answer. Those new ratings conflict with the no-primary-data requirement. Existing Sinhala benchmarks are leads, but their task labels are not automatically human quality ratings for generated answers.

**Resources:** Estimate only: cached outputs and a small ranking head can run on CPU; adapting a small open model may need an occasional GPU. Paid GPT/Gemini/Claude calls and an 8B-model training budget are not secured.

**Fallback:** Use a verified, already human-rated Sinhala subset if one exists. Without it, park the idea. Replacing human ratings with another AI judge would change the question and would not solve the validation problem.

These are feasibility estimates, not demonstrated training costs. The PDF’s resource allowance does not establish this team’s actual GPU or paid-service access.

## 6. Three-member contributions

All members address the shared question in section 2. Each investigation starts from the same unchanged baseline so that another member’s proposed improvement is not a prerequisite.

| Member | Question and hypothesis | Method, comparison and removal test | Independently assessable result |
|---|---|---|---|
| A: Stable judgments | Does answer order or length change the score? H: matched prompt training reduces this bias. | Train an order-invariant ranking head; compare a fixed judge and a head without order augmentation. | Paired ranking errors and order-flip rate on unseen prompts. |
| B: Language transfer | Does Sinhala adaptation improve agreement beyond multilingual training? H: existing Sinhala labels help on new topics. | Adapt the same base judge; compare no adaptation and equal-budget multilingual adaptation. | Human agreement by topic and script, with a Sinhala-data removal test. |
| C: Compact judge | Can a smaller judge retain the larger judge’s useful decisions? H: training on human labels plus teacher scores helps. | Compare a simple classifier, teacher-only distillation and mixed-label training. | Agreement versus memory and measured latency; separately count confident mistakes. |

Shared data access is a common prerequisite. A failed proposed method can still produce an interpretable comparison. Papers are optional; the work must remain attributable through experiments and removal tests. Where the gate table marks the team structure Unknown, the shared data barrier prevents treating this as an execution-ready split.

## 7. Evaluation

- **Primary measure:** Pairwise ranking agreement with existing human labels, alongside raw agreement, weighted kappa and rank correlation. State exactly what each agreement statistic compares; cross-language consistency is not automatically human agreement.
- **Keep data separate:** Group by original prompt and source; keep all answer variants together. Hold out topics and answer-generating models where the existing labels allow.
- **Baselines:** A simple feature-based ranking model, a fixed multilingual judge and a strong openly available instruction model with a fixed evaluation prompt. Model licences and exact checkpoints still need checking.
- **Removal tests:** use the member-specific tests above; keep data, tuning effort and inference budgets comparable.
- **Uncertainty, error analysis and useful negative findings:** Analyse order, answer length, topic, script and human disagreement. Bootstrap by prompt and repeat training with three seeds. A useful result could show that the small judge is unreliable or that simple prompt controls explain most gains.
- **Claim limit:** benchmark findings support the stated task and conditions. They do not establish reliable real-world deployment or a guaranteed benefit for users.

## 8. Score and next decision

**Provisional score: 53.5/100; not qualified.** Reject as written; needs existing human ratings. Ratings assess the imported proposal and access risks, not achieved results. Unknown gates block qualification; failed gates reject the current design regardless of score.

### Weighted rubric

The existing nine weights total 98. Scores are normalised to 100; decimals reflect arithmetic, not certainty. These comparison scores follow the existing provisional-scoring policy and do not override the gates.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low: Sinhala-specific novelty is plausible but has not passed a duplication audit. |
| Public dataset quality/accessibility | 15 | 1 | 3.0 | High confidence in the barrier: the proposed labels require new human raters. |
| Feasibility and learning curve | 14 | 2 | 5.6 | Low: labels and free model access are unresolved. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: ranking adaptation and compact-model training involve model research. |
| Evaluation/reproducibility | 12 | 2 | 4.8 | Low: the independent human reference set is missing. |
| Three-member structure | 12 | 3 | 7.2 | Medium-low: three questions are defined but all depend on the same missing labels. |
| Real-world significance | 9 | 4 | 7.2 | Medium: more reliable Sinhala model evaluation would be useful. |
| Compute/storage | 5 | 3 | 3.0 | Low-medium: small models are plausible; API and GPU budgets are unconfirmed. |
| Prototype | 3 | 4 | 2.4 | Medium: a side-by-side answer scoring demo is straightforward once labels exist. |
| **Normalised total / 100** | **98** | | **53.5** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 defines a concrete failure and affected users; its local magnitude is not measured. |
| 2. ML essential | Pass | The shared question concerns learned predictions rather than only an interface. |
| 3. Train/adapt models | Pass | The bounded design includes training or systematic model adaptation. |
| 4. Existing data accessible | Unknown | No reusable Sinhala answer-quality labels were verified. |
| 5. No unavailable human evaluation | Fail | The supplied design recruits native-speaker raters; current criteria exclude new human evaluation. |
| 6. Precise research gap | Unknown | Multilingual judging already exists; a distinct Sinhala failure is not demonstrated. |
| 7. Beyond application assembly | Pass | The proposal specifies learning experiments, comparisons and removal tests. |
| 8. Objective evaluation | Unknown | Independent human reference scores are not available for the proposed test. |
| 9. 6–8 month feasibility | Unknown | The rating-data dependency must be removed before a 6–8 month schedule is credible. |
| 10. Three connected contributions | Unknown | The three investigations share an unsecured human-rating prerequisite. |
| 11. No specialised/continuous high-end compute | Pass | The retained scope starts with small models or cached features and no dedicated hardware. |
| 12. Manageable data reuse | Unknown | The exact combination of data, model and derivative-output reuse terms is not verified. |
| 13. Useful negative findings | Pass | Section 7 identifies useful findings even if the proposed method does not improve performance. |

**Next decision:** Discuss with the supervisor whether a suitable existing human-rated Sinhala dataset can be secured. Otherwise reject the current design.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source and import limits](../../metadata/pdf-shortlist-import.json)
