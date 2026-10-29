[← Research candidates](../research-candidates.md)

# Does a Sinhala AI assistant behave differently across scripts?

**ID:** X39 · **Area:** NLP — Sinhala model reliability and safety

**Status:** Provisional; Refine; independent labels and script novelty unresolved; not qualified · **Imported:** 30 October 2026

**Provisional score:** 58.6/100 · No model training or timing performed.

**In plain language:** Compare equivalent Sinhala, Romanised and mixed-script prompts while separating refusal from incomprehensible output.

**Origin:** supplied shortlist, rank 6, page(s) 6. Its source verdict was “GO with reframing”. This brief uses the team’s current criteria; the source rank and verdict are not our qualification decision. [Import record](../../metadata/pdf-shortlist-import.json).

## 1. Problem

The same Sinhala request can be typed in Sinhala letters, Latin letters or a mixture. An assistant may respond differently because of script and language understanding. A meaningless answer is not evidence that it safely understood and refused the request.

## 2. Research gap and question

**Question:** On existing labelled Sinhala prompts, do equivalent script forms change meaningful refusal and harmless-answer quality, and can small-model adaptation reduce that difference?

**What is still uncertain:** Multilingual safety testing and orthography effects already have direct prior work. The PDF’s claim that nobody has tested all three Sinhala forms has not been verified. The useful question must go beyond a script comparison and establish that the evaluation can distinguish comprehension failures from genuine refusal.

**Hypothesis and alternative:** Training with paired script forms will reduce inconsistent behaviour without increasing refusals on harmless questions. An alternative is that the apparent safety improvement comes from poorer language understanding or a biased automatic judge.

## 3. Evidence from closest work

This is a bounded import check, not a complete novelty audit. “Checked” below refers to the stated abstract or source page, not a reproduction of the study. The supplied PDF’s wider search and verification claims are not independently certified.

| Source | What it supports | Reading limit |
|---|---|---|
| [A Framework to Assess Multilingual Vulnerabilities of LLMs](https://arxiv.org/abs/2503.13081) | The abstract warns that apparent low-resource vulnerabilities can include incoherent responses; refusal and comprehension need separate assessment. | Primary abstract checked; methods not reviewed. |
| [IndicJR](https://arxiv.org/abs/2602.16832) | The abstract explicitly studies romanised/mixed inputs and orthography effects. Sinhala-specific data coverage and methods need checking. | Primary abstract checked; methods not reviewed. |

## 4. Proposed approach

Use existing permitted prompts and labels. Generate script variants only where meaning can be established using existing references. Train a small adapter and compare it with no adaptation and an existing steering method. Keep harmless prompts in the experiment to detect over-refusal.

**Prototype:** demonstrate the same research pipeline on held-out existing examples, showing its output, errors and uncertainty. The interface is supporting work, not an individual research contribution.

## 5. Data and resources

**Data and access:** The cited multilingual-vulnerability paper and IndicJR are leads for existing prompts and labels. Their exact Sinhala coverage, licences and script-paired reference labels were not inspected. Automatic transliteration does not guarantee equivalent meaning. This design excludes new human raters; if existing labels cannot establish meaning and response quality, the study must pause or change scope.

**Resources:** Estimate only: use one small openly licensed model and a bounded prompt collection. Cache outputs and fit a modest adapter. API access, model licence, harmful-content handling requirements and evaluation costs still need checking with the supervisor.

**Fallback:** Restrict to already validated paired prompts and report only the supported behaviours. Without independent labels, do not call an automated judge’s score a measured safety guarantee.

These are feasibility estimates, not demonstrated training costs. The PDF’s resource allowance does not establish this team’s actual GPU or paid-service access.

## 6. Three-member contributions

All members address the shared question in section 2. Each investigation starts from the same unchanged baseline so that another member’s proposed improvement is not a prerequisite.

| Member | Question and hypothesis | Method, comparison and removal test | Independently assessable result |
|---|---|---|---|
| A: Script consistency | Does paired-script training reduce changes in behaviour? H: equivalent-form training improves consistency. | Adapt one model; compare ordinary training and an adapter without script pairing. | Meaningful refusal consistency and harmless-answer quality on held-out prompt families. |
| B: Training versus steering | Which correction preserves ordinary usefulness? H: a small adapter improves the trade-off over a steering-only baseline. | Compare equal-data adaptation, steering and unchanged weights; remove harmless-data rehearsal. | Harmful-answer rate versus over-refusal on existing independently labelled tests. |
| C: Decision reliability | Can a small evaluator flag incomprehensible outputs? H: a separate quality head reduces false safety conclusions. | Compare keyword refusal scoring, a fixed judge and an evaluator trained only on existing labels; remove quality features. | Evaluator agreement and error-detection coverage against independent reference labels. |

Shared data access is a common prerequisite. A failed proposed method can still produce an interpretable comparison. Papers are optional; the work must remain attributable through experiments and removal tests. Where the gate table marks the team structure Unknown, the shared data barrier prevents treating this as an execution-ready split.

## 7. Evaluation

- **Primary measure:** Meaningful harmful-response rate on an independently labelled test set, together with harmless over-refusal and comprehension quality. Report each script separately; a keyword refusal count alone cannot answer the question.
- **Keep data separate:** Group all script variants, translations and paraphrases of a source prompt together. Hold out prompt families and evaluate both harmful and harmless prompts without using test labels for adaptation.
- **Baselines:** Keyword refusal scoring as a diagnostic, unchanged open model, existing steering and matched-data adapter training. IndicJR is a necessary protocol comparison, not proof that the Sinhala case is empty.
- **Removal tests:** use the member-specific tests above; keep data, tuning effort and inference budgets comparable.
- **Uncertainty, error analysis and useful negative findings:** Bootstrap by original prompt and use three training seeds. Analyse script, prompt family, coherence and automatic-judge disagreement. Useful negative findings include a supposed safety gain being explained by loss of comprehension.
- **Claim limit:** benchmark findings support the stated task and conditions. They do not establish reliable real-world deployment or a guaranteed benefit for users.

## 8. Score and next decision

**Provisional score: 58.6/100; not qualified.** Refine; independent labels and script novelty unresolved. Ratings assess the imported proposal and access risks, not achieved results. Unknown gates block qualification; failed gates reject the current design regardless of score.

### Weighted rubric

The existing nine weights total 98. Scores are normalised to 100; decimals reflect arithmetic, not certainty. These comparison scores follow the existing provisional-scoring policy and do not override the gates.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | Low: multilingual safety and script effects are already studied. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: independently validated Sinhala script-pair labels are not verified. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Low-medium: small-model work is plausible but evaluation access is unresolved. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: adapter training and evaluator learning supply ML depth. |
| Evaluation/reproducibility | 12 | 2 | 4.8 | Low: meaning equivalence and response quality lack an independent reference set. |
| Three-member structure | 12 | 4 | 9.6 | Medium: consistency, corrective learning and evaluator reliability can be separately tested. |
| Real-world significance | 9 | 4 | 7.2 | Medium: script-dependent reliability matters to Sinhala users. |
| Compute/storage | 5 | 3 | 3.0 | Low-medium: bounded prompts help, but multiple model passes and training are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: a controlled script-comparison viewer is feasible. |
| **Normalised total / 100** | **98** | | **58.6** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 defines a concrete failure and affected users; its local magnitude is not measured. |
| 2. ML essential | Pass | The shared question concerns learned predictions rather than only an interface. |
| 3. Train/adapt models | Pass | The bounded design includes training or systematic model adaptation. |
| 4. Existing data accessible | Unknown | Existing Sinhala script-pair data and independent response labels are unverified. |
| 5. No unavailable human evaluation | Pass | The retained plan uses existing labels and excludes new participants or expert labelling. |
| 6. Precise research gap | Unknown | IndicJR already studies orthography effects; the Sinhala-specific added contribution is not established. |
| 7. Beyond application assembly | Pass | The proposal specifies learning experiments, comparisons and removal tests. |
| 8. Objective evaluation | Unknown | Meaning equivalence, comprehension and refusal cannot yet be independently scored. |
| 9. 6–8 month feasibility | Unknown | A bounded model run and suitable label set are prerequisites. |
| 10. Three connected contributions | Pass | Three connected research questions have separate comparisons and attributable results. |
| 11. No specialised/continuous high-end compute | Pass | The retained scope starts with small models or cached features and no dedicated hardware. |
| 12. Manageable data reuse | Unknown | The exact combination of data, model and derivative-output reuse terms is not verified. |
| 13. Useful negative findings | Pass | Section 7 identifies useful findings even if the proposed method does not improve performance. |

**Next decision:** Inspect existing Sinhala labels and the closest script-sensitivity methods with the supervisor before claiming a new Sinhala safety gap.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source and import limits](../../metadata/pdf-shortlist-import.json)
