[← Research candidates](../research-candidates.md)

# A small Sinhala–English feedback model that does not miss mixed opinions

**ID:** X44 · **Area:** NLP — customer feedback in mixed languages

**Status:** Provisional research opportunity; not qualified · **Checked:** 30 October 2026

**Score:** 73.7/100, provisional · **No model has been trained or timed.**

**The idea:** Recognise comments that contain both praise and a complaint, even after making the model smaller.

## 1. Problem

Sri Lankan customers often mix Sinhala and English in comments. A comment can praise the price but complain about service. A model dominated by neutral examples may miss these less common mixed opinions. That is a testable risk, not yet a demonstrated baseline failure.

**Example:** “The package is cheap, but the connection keeps dropping.” This invented example contains both a positive and a negative opinion. It should not be treated as proof that a real customer is satisfied.

## 2. Research gap and question

**Question:** Can a compact Sinhala–English model retain recognition of the rare “Conflict” sentiment class without creating too many false alarms?

**Already done:** Sinhala–English sentiment classification, script-aware prompting and multi-task adapters already exist. A generic sentiment analyser or another adapter comparison is not enough.

**What to investigate:** Test whether training and compression disproportionately lose the rare mixed-opinion class. Compare ordinary class balancing with training that preserves the larger model’s minority-class behaviour, then test whether confidence identifies unreliable outputs. This narrower gap is still provisional.

**Prediction to test:** Minority-aware training will retain more mixed opinions in a smaller model at a similar false-positive rate. The alternative is that ordinary weighting or a simple classifier already works as well.

## 3. Evidence from closest work

| Source | Why it matters | What was checked |
|---|---|---|
| [NLPC-UOM mixed-language dataset](https://huggingface.co/datasets/NLPC-UOM/Sinhala-English-Code-Mixed-Code-Switched-Dataset) | Public sentiment annotations and a licence statement exist. The sentence CSV was independently parsed; its counts differ from the card. | Card and full small sentence CSV checked; words CSV not downloaded. |
| [AdapterFusion multi-task classification](https://www.sciencedirect.com/science/article/abs/pii/S0952197623014239) | Multi-task adapters already combine sentiment and humour in Sinhala–English. Adding humour is not by itself a new contribution. | Publisher abstract and available methods/results excerpts inspected. |
| [Script-aware prompt learning](https://link.springer.com/article/10.1007/s11280-024-01302-2) | The study already evaluates Sinhala–English scripts and code-mixing. Script awareness is a baseline, not a new gap. | Primary full-text page: abstract and experimental description inspected. |
| [Jev Sinhala evaluation repository](https://github.com/Azri-Muhsin/jev-sinhala-review) | An author repository already describes Sinhala classification calibration and script sensitivity. Its model and test protocol require closer comparison. | Author README checked; peer-review status and experiments not independently verified. |

The problem evidence and the proposed solution are different things. No baseline failure or improvement has been demonstrated by this project. The searches do not prove novelty. [Search and data-check record](../../metadata/sri-lanka-practical-checks.json).

## 4. Proposed approach

Use the released sentiment labels and begin with a simple text classifier. Train one multilingual teacher and a smaller student. Keep all four classes, including Conflict. Quarantine duplicate groups with inconsistent labels instead of silently changing their labels. Use confidence to leave uncertain cases undecided.

**Simple prototype:** show a held-out example, the baseline answer, the proposed answer and any uncertainty. Building the screen is supporting work, not a member’s research contribution.

## 5. Data and resources

**Existing data:** The NLPC-UOM dataset card says 10,000 comments and MIT. The downloaded sentence CSV actually contains 13,518 rows: 8,597 Neutral, 3,641 Negative, 1,156 Positive and 124 Conflict. A case/whitespace check found 75 extra duplicate rows and seven groups with inconsistent sentiment labels. These are file checks, not a completed annotation audit. The card/file mismatch needs documenting before experiments.

**What the team needs:** Estimate: the CSV is about 1.69 MB. CPU feature baselines and cached multilingual embeddings are practical; limited adapter/student training may use an occasional GPU. No paid language-model service is needed.

**Fallback:** Start with frozen multilingual features and a trained classifier. Keep the original four classes. If 124 mixed-opinion examples cannot support a stable result, report that uncertainty rather than claiming a reliable business tool.

Costs and training times are estimates until measured. No paid services, new participants or guaranteed university GPU are assumed.

## 6. Three-member contributions

One shared problem, three testable contributions. Each can start from the same unchanged baseline; another member’s proposed method does not have to succeed first.

| Member | Question and prediction | Method, baseline and removal test | Separate result |
|---|---|---|---|
| A: Rare-class learning | Do balanced training methods recover mixed opinions? H: calibrated class weighting improves rare-class recall. | Compare ordinary loss, class weighting and focal loss; remove the weighting. | Conflict precision/recall alongside performance on all four classes. |
| B: Compact model | Does ordinary compression erase rare-class behaviour? H: minority-aware teacher imitation retains it. | Compare a large model, an ordinary student and a minority-aware student with identical training text; remove minority weighting. | Rare-class retention versus model size and measured speed. |
| C: Reliable decisions | Can uncertain mixed-language comments be flagged? H: a trained confidence head beats raw probabilities. | Use the unchanged baseline outputs; compare temperature scaling and a small error predictor; remove script/mixing features. | Errors and class coverage among automatically decided comments. |

All members share data and evaluation code. Papers are optional. “Removal test” means taking out the proposed change to see whether it actually helped.

## 7. Evaluation

- **Main measures:** Four-class macro-F1, which gives each class equal importance, plus Conflict-class precision and recall. Report false Conflict alerts as well as missed mixed opinions; overall accuracy alone can hide the rare class.
- **Fair data split:** Group duplicate and near-duplicate comments before splitting. Quarantine the seven inconsistent duplicate groups and report a sensitivity check. Use repeated grouped, class-stratified splits; keep a fixed final test set untouched. No date/source fields were verified, so do not claim time or cross-platform transfer.
- **Comparisons:** Character/word TF-IDF with logistic regression or SVM, frozen multilingual features, an adapted XLM-R baseline, the published script-aware method where reproducible, ordinary student training and simple class weighting.
- **Removal tests:** use the member-specific comparisons above and keep training/tuning budgets matched.
- **Uncertainty and useful failures:** Use three training seeds and group-level confidence intervals. Show test counts for the rare class and wide intervals honestly. Analyse script, text length, humour labels and mixed opinions. A useful result is that a simple classifier matches the larger model or compression harms the rare class.
- **What the results cannot prove:** These released social-media comments are not private support tickets or all Sri Lankan businesses. The labels support whole-comment sentiment, not a separate sentiment label for every product feature.

## 8. Score and next decision

**Provisional score: 73.7/100; not qualified.** This is a promising practical direction, not a verified new gap. The score describes the plan; unknown gates still prevent selection.

### Weighted rubric

The existing nine weights total 98 and are normalised to 100. Ratings use the project’s provisional comparison policy. Decimal totals are arithmetic, not scientific certainty.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: rare-class retention under compression is narrower than existing sentiment work; novelty remains unchecked. |
| Public dataset quality/accessibility | 15 | 3 | 9.0 | Medium: a small labelled CSV was parsed; rare labels, duplicate conflicts and the card mismatch reduce suitability. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: simple baselines and small students fit the team better than building a new language model. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: balanced training, compression and error prediction involve model-level experiments. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: labels allow objective tests, with explicit limits from rare-class counts. |
| Three-member structure | 12 | 4 | 9.6 | Medium: learning, compression and confidence provide connected but separable experiments. |
| Real-world significance | 9 | 4 | 7.2 | Medium: mixed-language feedback is locally relevant; business impact is not demonstrated. |
| Compute/storage | 5 | 4 | 4.0 | Medium: small data and CPU baselines are manageable; GPU costs are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: paste a comment and display the prediction or uncertainty, using held-out examples. |
| **Normalised total / 100** | **98** | | **73.7** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan. Unknown means evidence is still needed.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | A specific local task and evidence-backed limitation are described in sections 1–3. |
| 2. ML essential | Pass | The question tests learned predictions and model errors, not only an application. |
| 3. Train/adapt models | Pass | All three investigations train or systematically adapt models. |
| 4. Existing data accessible | Pass | The sentence CSV was downloaded and parsed; four sentiment labels and class counts were checked. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing reference labels or aggregate counts; no new raters or recordings. |
| 6. Precise research gap | Unknown | Script-aware classification and calibration have prior work; the rare-class compression distinction needs deeper checking. |
| 7. Beyond application assembly | Pass | The research is tested through comparisons and removal tests; the interface is supporting work. |
| 8. Objective evaluation | Pass | Existing four-class labels support grouped comparisons; ambiguous duplicate groups can be quarantined without new labelling. |
| 9. 6–8 month feasibility | Unknown | A baseline must show whether the small rare class gives stable, independently assessable findings. |
| 10. Three connected contributions | Pass | Three connected questions have separate comparisons and results using a shared unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | The bounded plan uses CPU baselines and occasional modest GPU access, with no special hardware. |
| 12. Manageable data reuse | Unknown | The dataset card states MIT, but underlying comment reuse and exact model licences still need confirmation. |
| 13. Useful negative findings | Pass | Simple baselines winning or a proposed method failing still answers the stated questions. |

**Next decision:** Reproduce a duplicate-grouped baseline and check the 124 rare labels before investing in a new compact-model method. Discuss the result with the supervisor.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source checks](../../metadata/sri-lanka-practical-checks.json)
