[← Research candidates](../research-candidates.md)

# Do small MCP attack detectors survive unfamiliar attacks?

**ID:** X35 · **Area:** Security ML — MCP tool screening

**Status:** Provisional; Refine; broad adaptive-attack novelty claim overlaps prior work; not qualified · **Imported:** 30 October 2026

**Provisional score:** 65.1/100 · No model training or timing performed.

**In plain language:** Test small tool-poisoning detectors on new servers and attack families; adaptive evaluation already exists.

**Origin:** supplied shortlist, rank 2, page(s) 3–4. Its source verdict was “GO”. This brief uses the team’s current criteria; the source rank and verdict are not our qualification decision. [Import record](../../metadata/pdf-shortlist-import.json).

## 1. Problem

MCP lets an AI assistant discover tools from descriptions. A poisoned description can try to redirect the assistant. A detector may score well because it recognises the wording of a training collection rather than the underlying attack.

## 2. Research gap and question

**Question:** Under a fixed offline attack budget, do compact detectors still recognise poisoned tool descriptions from unseen servers and attack families, and which low-cost adaptation helps?

**What is still uncertain:** The PDF says adaptive testing of lightweight trained detectors is missing. That broad claim is not defensible as stated: SchemaGuard explicitly includes an adaptive-attacker split. A narrower difference in threat model, data separation or resource budget must be established from its full methods first.

**Hypothesis and alternative:** Training on structurally varied examples will improve recall at a fixed benign blocking rate. An alternative is that existing structure-aware detectors already solve the chosen test or that gains come from duplicate templates.

## 3. Evidence from closest work

This is a bounded import check, not a complete novelty audit. “Checked” below refers to the stated abstract or source page, not a reproduction of the study. The supplied PDF’s wider search and verification claims are not independently certified.

| Source | What it supports | Reading limit |
|---|---|---|
| [Machine Learning-Based Detection of MCP Attacks](https://arxiv.org/abs/2604.10534) | The abstract reports perfect binary F1 for several models on its tested data; that is not evidence of broad robustness. | Primary abstract checked; methods not reviewed. |
| [SchemaGuard](https://www.techscience.com/cmc/online/detail/28645) | The publisher abstract describes a compact structure-aware model and explicitly lists an adaptive-attacker evaluation split. The PDF’s broad missing-adaptive-evaluation claim needs narrowing. | Primary abstract checked; methods not reviewed. |
| [MCPTox dataset lead](https://arxiv.org/abs/2508.14925) | Dataset lead from the supplied PDF; corpus licence and download contents remain unchecked. | Lead from supplied PDF; target methods/data not reviewed. |

## 4. Proposed approach

Use inert, labelled tool descriptions in an offline harness. Train a small detector; compare text-only and field-aware inputs. Evaluate on held-out servers and bounded adaptive variants. No production services, credentials or live tool execution are needed.

**Prototype:** demonstrate the same research pipeline on held-out existing examples, showing its output, errors and uncertainty. The interface is supporting work, not an individual research contribution.

## 5. Data and resources

**Data and access:** MCPTox and the detector paper are dataset leads. The actual downloadable corpus, licence, benign tool provenance and template groups still need inspection. Public visibility of a tool registry is not a reuse licence. Keep copies of source versions and remove duplicates before splitting.

**Resources:** Estimate only: TF-IDF classifiers are CPU-friendly and a compact encoder should allow modest GPU adaptation. Start with hundreds of examples and a fixed attack budget. No model or attack run was performed during import.

**Fallback:** Run a reproducible held-out-server comparison using an already licensed corpus. If the full SchemaGuard study covers the same threat model and controls, drop this gap or identify a materially different failure before proceeding.

These are feasibility estimates, not demonstrated training costs. The PDF’s resource allowance does not establish this team’s actual GPU or paid-service access.

## 6. Three-member contributions

All members address the shared question in section 2. Each investigation starts from the same unchanged baseline so that another member’s proposed improvement is not a prerequisite.

| Member | Question and hypothesis | Method, comparison and removal test | Independently assessable result |
|---|---|---|---|
| A: Generalisation | Do field-aware representations survive new servers? H: structural inputs transfer better than flat text. | Train both on identical data; compare TF-IDF/SVC and a compact text encoder; remove field markers. | Attack recall at matched benign blocking rates on held-out servers. |
| B: Robust training | Does adversarial training help against a separate attack procedure? H: gains extend beyond the training templates. | Compare ordinary training and fixed-budget adversarial training; remove structural variation. | Recall on held-out attack families and adaptive variants, with attack validity counted separately. |
| C: Reliable blocking | Can a calibrated reject-or-review rule avoid blocking harmless tools? H: calibration helps on shifted data. | Fit a small confidence head on the unchanged base detector; compare thresholding and uncalibrated scores. | False blocks, retained attack recall and review workload at matched coverage. |

Shared data access is a common prerequisite. A failed proposed method can still produce an interpretable comparison. Papers are optional; the work must remain attributable through experiments and removal tests. Where the gate table marks the team structure Unknown, the shared data barrier prevents treating this as an execution-ready split.

## 7. Evaluation

- **Primary measure:** Attack recall at a validation-chosen benign blocking rate, with the full precision/recall curve and actual test false-positive rate. Do not optimise the operating point on attacks in the test set.
- **Keep data separate:** Separate servers, source repositories and attack templates before augmentation. Reserve a separate attack generator or procedure for the final adaptive test.
- **Baselines:** Keyword/YARA-style rules, TF-IDF with SVC, the published BERT-style detector and SchemaGuard if code/data permit. Baseline implementation and licence availability remain unresolved.
- **Removal tests:** use the member-specific tests above; keep data, tuning effort and inference budgets comparable.
- **Uncertainty, error analysis and useful negative findings:** Report attacks that fail to remain valid as well as successful evasions. Bootstrap by server/template, use three training seeds and report runtime. Useful findings include simple features being sufficient or adaptive gains disappearing after deduplication.
- **Claim limit:** benchmark findings support the stated task and conditions. They do not establish reliable real-world deployment or a guaranteed benefit for users.

## 8. Score and next decision

**Provisional score: 65.1/100; not qualified.** Refine; broad adaptive-attack novelty claim overlaps prior work. Ratings assess the imported proposal and access risks, not achieved results. Unknown gates block qualification; failed gates reject the current design regardless of score.

### Weighted rubric

The existing nine weights total 98. Scores are normalised to 100; decimals reflect arithmetic, not certainty. These comparison scores follow the existing provisional-scoring policy and do not override the gates.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | High confidence in overlap: SchemaGuard already reports an adaptive-attacker split. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Low-medium: public corpus leads exist; licences and grouping are not inspected. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Medium-low: compact methods are manageable after data access is resolved. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: detector learning and robust adaptation have substantial ML content. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: metrics are clear but attack validity and deduplication need work. |
| Three-member structure | 12 | 4 | 9.6 | Medium: representation, training and reliability can be tested against one shared base. |
| Real-world significance | 9 | 4 | 7.2 | Medium: screening poisoned tool descriptions has a clear defensive use. |
| Compute/storage | 5 | 4 | 4.0 | Medium: CPU baselines and compact encoders are plausible; unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: an offline tool-description screening demo is bounded. |
| **Normalised total / 100** | **98** | | **65.1** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 defines a concrete failure and affected users; its local magnitude is not measured. |
| 2. ML essential | Pass | The shared question concerns learned predictions rather than only an interface. |
| 3. Train/adapt models | Pass | The bounded design includes training or systematic model adaptation. |
| 4. Existing data accessible | Unknown | Corpus files, reuse terms and independent benign examples have not been inspected. |
| 5. No unavailable human evaluation | Pass | The retained plan uses existing labels and excludes new participants or expert labelling. |
| 6. Precise research gap | Unknown | SchemaGuard already tests adaptive attackers; the added contribution is not established. |
| 7. Beyond application assembly | Pass | The proposal specifies learning experiments, comparisons and removal tests. |
| 8. Objective evaluation | Unknown | Attack-validity labels and leakage-safe source/template groups are not verified. |
| 9. 6–8 month feasibility | Unknown | A baseline reproduction and full nearest-neighbour comparison are still needed. |
| 10. Three connected contributions | Pass | Three connected research questions have separate comparisons and attributable results. |
| 11. No specialised/continuous high-end compute | Pass | The retained scope starts with small models or cached features and no dedicated hardware. |
| 12. Manageable data reuse | Unknown | The exact combination of data, model and derivative-output reuse terms is not verified. |
| 13. Useful negative findings | Pass | Section 7 identifies useful findings even if the proposed method does not improve performance. |

**Next decision:** Compare the proposed split and attack budget with SchemaGuard’s full methods before choosing this scope.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source and import limits](../../metadata/pdf-shortlist-import.json)
