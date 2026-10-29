[← Research candidates](../research-candidates.md)

# Does shrinking a code model change the security of its code?

**ID:** X40 · **Area:** Software ML — quantisation and secure code

**Status:** Provisional; Refine; execution-based difference and training scope unresolved; not qualified · **Imported:** 30 October 2026

**Provisional score:** 66.5/100 · No model training or timing performed.

**In plain language:** Check low-precision code models with security tests and see whether a small secure-coding adaptation survives compression.

**Origin:** supplied shortlist, rank 7, page(s) 6. Its source verdict was “GO with reframing”. This brief uses the team’s current criteria; the source rank and verdict are not our qualification decision. [Import record](../../metadata/pdf-shortlist-import.json).

## 1. Problem

Quantisation stores a model’s numbers using fewer bits so it needs less memory. Code may still pass ordinary tests while mishandling a security-sensitive case or naming a package that does not exist. Developers need evidence about these trade-offs, not an assumption that smaller means unsafe.

## 2. Research gap and question

**Question:** At matched model and decoding settings, does 3–4-bit quantisation change security-test outcomes, and does a small secure-coding adaptation preserve its benefit after quantisation?

**What is still uncertain:** Quantize with Confidence? already compares six quantisation methods and reports stable security attributes. The PDF proposes execution-based security tests and adaptation retention as narrower contrasts. Whether those are genuinely absent from prior methods has not been checked. Do not claim quantisation causes vulnerabilities before testing.

**Hypothesis and alternative:** Some security behaviours are more sensitive to quantisation than ordinary correctness, and adaptation may reduce this difference. An alternative is that security remains stable and differences are mostly sampling noise.

## 3. Evidence from closest work

This is a bounded import check, not a complete novelty audit. “Checked” below refers to the stated abstract or source page, not a reproduction of the study. The supplied PDF’s wider search and verification claims are not independently certified.

| Source | What it supports | Reading limit |
|---|---|---|
| [Quantize with Confidence?](https://arxiv.org/abs/2607.14181) | The abstract reports six quantisation methods and stable security attributes. This is direct prior work; it does not establish the proposed execution-test gap. | Primary abstract checked; methods not reviewed. |
| [Earlier quantisation study lead](https://arxiv.org/abs/2507.09665) | Additional predecessor supplied in the PDF; precise overlap is not reviewed here. | Lead from supplied PDF; target methods/data not reviewed. |

## 4. Proposed approach

Start with one small code-model family and Python only. Compare full precision with two quantisers at fixed decoding settings. Train a small secure-coding adapter on separate existing examples, then quantise it. Treat package-existence errors as a related secondary outcome, not a substitute for security tests.

**Prototype:** demonstrate the same research pipeline on held-out existing examples, showing its output, errors and uncertainty. The interface is supporting work, not an individual research contribution.

## 5. Data and resources

**Data and access:** CWEval and BaxBench are source-supplied test-suite leads; their licences, test isolation and exact supported model tasks are not inspected. Version and deduplicate training and test tasks. Package checks need a fixed registry snapshot: existence does not establish that a package is safe or appropriate.

**Resources:** Estimate only: inference with a small model is plausible on modest hardware, but repeated code tests and adapter training may be expensive. A full-precision comparison must fit the available device. Generated code should be evaluated in an isolated, resource-limited test environment without credentials or network access.

**Fallback:** Use a smaller model, fewer quantisers and one verified test suite. If model training cannot be included, the original inference-only design needs module approval or a different scope; a comparison app alone does not meet the modelling requirement.

These are feasibility estimates, not demonstrated training costs. The PDF’s resource allowance does not establish this team’s actual GPU or paid-service access.

## 6. Three-member contributions

All members address the shared question in section 2. Each investigation starts from the same unchanged baseline so that another member’s proposed improvement is not a prerequisite.

| Member | Question and hypothesis | Method, comparison and removal test | Independently assessable result |
|---|---|---|---|
| A: Quantisation effects | Does quantisation change security beyond correctness? H: paired security failures vary by quantiser. | Compare full precision and matched quantised checkpoints; keep prompts and decoding fixed. | Paired changes in secure pass rate and functional pass rate. |
| B: Secure adaptation retention | Does learned secure behaviour survive quantisation? H: mixed secure/ordinary training preserves both. | Train a small adapter; compare ordinary adaptation and a model without secure examples. | Secure pass rate after quantisation and ordinary correctness retention. |
| C: Error prediction | Can a small predictor flag quantisation-sensitive outputs? H: learned confidence helps at fixed review coverage. | Train a lightweight risk head on separate generated examples; compare raw confidence and a head without package/test features. | Security-error detection at matched retained coverage; include latency and memory. |

Shared data access is a common prerequisite. A failed proposed method can still produce an interpretable comparison. Papers are optional; the work must remain attributable through experiments and removal tests. Where the gate table marks the team structure Unknown, the shared data barrier prevents treating this as an execution-ready split.

## 7. Evaluation

- **Primary measure:** Secure functional pass rate under fixed decoding and test budgets, accompanied by ordinary pass@1. Report paired task-level changes; a static scanner score is a separate diagnostic.
- **Keep data separate:** Deduplicate by task/template and keep training solutions separate from held-out security tests. Fix model revision, quantiser version, decoding seeds and package-registry date.
- **Baselines:** Full-precision unchanged model, two post-training quantisation methods, static analysis and the nearest quantisation study’s protocol. Security-trained adaptation is compared with equal-budget ordinary adaptation.
- **Removal tests:** use the member-specific tests above; keep data, tuning effort and inference budgets comparable.
- **Uncertainty, error analysis and useful negative findings:** Use paired bootstrap intervals by task and multiple decoding/training seeds. Analyse vulnerability family, task difficulty and package errors separately. Useful findings include stable security, scanner/test disagreement or secure adaptation failing after compression.
- **Claim limit:** benchmark findings support the stated task and conditions. They do not establish reliable real-world deployment or a guaranteed benefit for users.

## 8. Score and next decision

**Provisional score: 66.5/100; not qualified.** Refine; execution-based difference and training scope unresolved. Ratings assess the imported proposal and access risks, not achieved results. Unknown gates block qualification; failed gates reject the current design regardless of score.

### Weighted rubric

The existing nine weights total 98. Scores are normalised to 100; decimals reflect arithmetic, not certainty. These comparison scores follow the existing provisional-scoring policy and do not override the gates.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | Low: quantisation and security already have a direct recent empirical predecessor. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Low-medium: public benchmark leads exist; access terms and test content remain unchecked. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: Python and a small model bound the work, but secure execution adds effort. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: the retained design includes adapter and risk-head training; inference alone would not suffice. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: paired execution tests address the proposed difference directly, if verified. |
| Three-member structure | 12 | 4 | 9.6 | Medium: sensitivity, adaptation retention and error prediction support distinct results. |
| Real-world significance | 9 | 4 | 7.2 | Medium: code security on limited hardware is a clear concern. |
| Compute/storage | 5 | 3 | 3.0 | Low-medium: full-precision baselines and repeated sandbox tests are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: a fixed-task comparison view can demonstrate results. |
| **Normalised total / 100** | **98** | | **66.5** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 defines a concrete failure and affected users; its local magnitude is not measured. |
| 2. ML essential | Pass | The shared question concerns learned predictions rather than only an interface. |
| 3. Train/adapt models | Unknown | The supplied design is inference-only; the added trainable extension needs a feasible data/model plan. |
| 4. Existing data accessible | Unknown | Benchmark files, training data, licences and executable test routes have not been inspected. |
| 5. No unavailable human evaluation | Pass | The retained plan uses existing labels and excludes new participants or expert labelling. |
| 6. Precise research gap | Unknown | Execution-test and adaptation-retention differences require a full nearest-neighbour check. |
| 7. Beyond application assembly | Pass | The proposal specifies learning experiments, comparisons and removal tests. |
| 8. Objective evaluation | Unknown | Executable security tests and independent task groups have not been inspected. |
| 9. 6–8 month feasibility | Unknown | Full-precision baseline memory and secure test execution need a bounded feasibility check. |
| 10. Three connected contributions | Pass | Three connected research questions have separate comparisons and attributable results. |
| 11. No specialised/continuous high-end compute | Pass | The retained scope starts with small models or cached features and no dedicated hardware. |
| 12. Manageable data reuse | Unknown | The exact combination of data, model and derivative-output reuse terms is not verified. |
| 13. Useful negative findings | Pass | Section 7 identifies useful findings even if the proposed method does not improve performance. |

**Next decision:** Inspect the full quantisation paper and one executable benchmark before agreeing the added training question with the supervisor.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source and import limits](../../metadata/pdf-shortlist-import.json)
