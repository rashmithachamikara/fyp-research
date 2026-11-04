[← Research candidates](../research-candidates.md)

# Reading Sinhala documents without introducing new mistakes

**ID:** X43 · **Area:** Computer vision and NLP — Sinhala document reading

**Status:** Parked; current formulation needs redesign; not qualified · **Rechecked:** 30 October 2026

**Score:** 73.5/100, provisional · **Novelty: 2/5** · **No model has been trained or timed.**

**Current verdict:** The practical problem is real, but X43 does not yet identify a defensible new gap. OCR correction, error detection before correction, and copying correct characters already exist. The earlier recommendation to prioritise X43 is withdrawn.

[Earlier two-page PDF explanation](../../../output/pdf/x43-sinhala-document-reading.pdf) — written before this novelty recheck. Its 76.7 score and recommendation are superseded by this brief.

## 1. Problem

Libraries, publishers and public offices may need searchable copies of printed Sinhala documents. OCR means reading text from an image. A second model can try to repair OCR mistakes, but it might also change text that was already correct.

**Example:** A date or section number is read correctly, but an automatic “correction” changes it. This is an example of the risk, not an observed result from our own experiment.

## 2. Research gap and question

**Earlier question, withdrawn as a novelty claim:** Can a small correction model fix remaining Sinhala OCR errors while making fewer unnecessary edits, especially to numbers?

**Already done:** Sinhala OCR post-processing exists. Low-resource OCR research already learns common recognition errors and uses copying to retain correct characters. Other work separates error detection from correction. Recent Sinhala page-level OCR also performs strongly on legislative documents. These are necessary comparisons, not new contributions we can claim.

**Why the current gap is weak:** “Correct mistakes without damaging correct text” is already an established aim. Using Sinhala, adding a confidence score, protecting numbers or making a model smaller does not by itself establish a new contribution. We have not shown a specific failure that remains after applying existing methods.

**What would justify reopening it:** First show a repeatable, important error on the existing Sinhala data that strong correction methods and simple rules do not adequately handle. Then define a method that addresses that failure. Damage to correctly read numbers is one possible test, not an observed finding or a verified remaining gap.

## 3. Evidence from closest work

| Source | Why it matters | What was checked |
|---|---|---|
| [Sinhala legislative OCR dataset](https://huggingface.co/datasets/avishadilhara/sinhala-ocr-lk-acts-1010) | The official card lists a real-page dataset, licence and source-document fields. File listing and a row preview were checked. | Dataset card, manifest and bounded preview; no image inspection. |
| [Cross-Temporal Sinhala OCR](https://arxiv.org/html/2606.29378) | The paper already adapts page-level OCR and limits its claims to legislative documents. Another generic Sinhala OCR fine-tune would overlap. | Dataset, experiments and limitations sections inspected; no reproduction. |
| [Confident but Wrong](https://arxiv.org/html/2609.29680) | This studies translation post-editing, not OCR. It already diagnoses harmful edits and unreliable confidence, so confidence-based editing itself is not new. | Abstract and methods outline inspected; adjacent-task comparison. |
| [Existing Sinhala OCR post-processing](https://www.theekshana.lk/project/optical-character-recognition-for-sinhala/) | UCSC/Theekshana already describes a Sinhala OCR post-processing engine. Do not claim to introduce Sinhala post-processing. | Original project description checked. |
| [OCR Post Correction for Endangered Language Texts (2020)](https://aclanthology.org/2020.emnlp-main.478.pdf) | Already learns OCR error patterns and uses a choice between copying existing characters and generating replacements. This overlaps the proposed careful-copying approach. | ACL record and indexed primary-text excerpts from sections 5.2–5.3 checked; no reproduction. |
| [Post-OCR text correction for Bulgarian historical documents (2025)](https://strathprints.strath.ac.uk/92317/1/Beshirov-etal-IJDL-2025-Post-OCR-text-correction-for-Bulgarian-historical-documents.pdf) | The published pipeline detects errors before correction and includes a character-copying mechanism. Detecting, correcting and retaining correct text is therefore not a new overall workflow. | Indexed primary-text excerpts including Figure 1 and methods checked; full PDF retrieval timed out. |

These studies do not establish that all Sinhala OCR problems are solved. They do establish substantial overlap with X43's current formulation. No remaining Sinhala-specific failure or new solution has been demonstrated by this project. [Search and data-check record](../../metadata/sri-lanka-practical-checks.json).

## 4. Proposed approach

**Baseline audit only, if the team considers reopening X43:** choose one fixed OCR engine and compare unchanged output, simple correction rules, an existing copy-based corrector and a detect-then-correct method. Check harmful edits and number errors against the released reference text. Inspect full methods, code and licences before implementing the comparisons. Do not treat a newly assembled correction pipeline as a new research contribution.

**Simple prototype:** show a held-out example, the baseline answer, the proposed answer and any uncertainty. Building the screen is supporting work, not a member’s research contribution.

## 5. Data and resources

**Existing data:** The public sinhala-ocr-lk-acts-1010 release contains 1,010 legislative pages with reference text. Its card states CC BY 4.0 and about 872 MB. A bounded preview returned 45 rows and confirmed image, text, year, doc_id and page_num fields. The file listing contains four Parquet files. Images were not downloaded for visual inspection and no OCR baseline was run.

**What the team needs:** Estimate: cached OCR output, small correction models and an occasional modest GPU. Start with 100 training pages to measure time and memory. A larger OCR model is a comparison, not a requirement for every experiment.

**Fallback:** Keep the topic parked if established correction methods are sufficient, or if too few meaningful errors remain. A useful reproduction or benchmark finding does not automatically meet the module's novelty requirement.

Costs and training times are estimates until measured. No paid services, new participants or guaranteed university GPU are assumed.

## 6. Three-member contributions

The earlier three-member split is retained below for reference. It gives separately measurable experiments, but it does not repair the missing shared research gap. It is not a recommendation to proceed with the current project. Each investigation could start from the same unchanged baseline if a distinct failure is later established.

| Member | Question and prediction | Method, baseline and removal test | Separate result |
|---|---|---|---|
| A: Better correction examples | Does learning actual OCR confusions beat generic text rewriting? H: real error patterns help. | Train a compact corrector; compare dictionary rules and equal-sized synthetic-error training; remove real-error examples. | Character errors fixed versus new errors introduced. |
| B: Choosing when to edit | Can a model predict whether an edit helps? H: a trained edit selector beats a fixed confidence threshold. | Train against reference text; compare no selection, edit-distance limits and confidence thresholds; remove image/OCR features. | Useful corrections at matched numbers of harmful edits. |
| C: A smaller corrector | Can compression preserve careful copying and number accuracy? H: copy-aware training helps the smaller model. | Compare a compact student, ordinary teacher imitation and copy-weighted training; remove copy/number weighting. | Error rate, exact numeric-token matches, memory and measured processing time. |

All members share data and evaluation code. Papers are optional. “Removal test” means taking out the proposed change to see whether it actually helped.

## 7. Evaluation

- **Main measures:** Character error rate: the share of characters that are inserted, deleted or read wrongly. Also count harmful edits that turn correct text into wrong text, and exact matches for digit-containing tokens. Do not claim to protect all personal names without name labels.
- **Fair data split:** Keep pages from the same legislative document together using doc_id. Publish a document-grouped split and report the released split separately for comparison. Keep test documents out of the error examples and tuning process.
- **Comparisons:** Unchanged Tesseract/Surya output, simple dictionary or edit-distance correction, an existing copy-based OCR corrector, a detect-then-correct approach, and a strong Sinhala-adapted OCR model such as the published LightOnOCR baseline. Check exact checkpoint/code licences before reuse.
- **Removal tests:** use the member-specific comparisons above and keep training/tuning budgets matched.
- **Uncertainty and useful failures:** Repeat trainable methods with three seeds. Use document-level confidence intervals, not independent characters. Analyse old/new pages, numbers and initially correct words. A useful result is that a simple edit limit or no correction performs best.
- **What the results cannot prove:** The verified dataset contains legislative pages. It cannot establish reliable handwriting recognition, arbitrary phone-photo reading or automatic form processing.

## 8. Score and next decision

**Provisional score: 73.5/100; not qualified; park pending redesign.** Novelty falls from 3/5 to 2/5 after locating closer OCR-correction studies. Gate 6 fails for the current formulation. The earlier 76.7 score and first-choice recommendation are withdrawn. This does not rule out every future Sinhala OCR question.

### Weighted rubric

The existing nine weights total 98 and are normalised to 100. Ratings use the project’s provisional comparison policy. Decimal totals are arithmetic, not scientific certainty.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | Medium-high confidence in overlap: existing OCR work learns error patterns, copies correct characters and detects errors before correction; no distinct remaining failure is demonstrated. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium: real Sinhala images, references and document identifiers have a verified public route; full quality audit remains. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: frozen OCR and small correctors offer a bounded 6–8 month plan; no timing measured. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: correction, edit selection and compact-model training are empirical ML work. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: reference text supports character errors and harmful-edit counts without new raters. |
| Three-member structure | 12 | 4 | 9.6 | Medium: three investigations can use the same unchanged OCR output independently. |
| Real-world significance | 9 | 4 | 7.2 | Medium: searchable Sinhala documents are a direct local use; savings have not been measured. |
| Compute/storage | 5 | 4 | 4.0 | Medium: cached outputs reduce repeated GPU work; resource figures are estimates. |
| Prototype | 3 | 4 | 2.4 | Medium: a page, original text and highlighted edits make a simple prototype. |
| **Normalised total / 100** | **98** | | **73.5** | **Park pending redesign; not qualified.** |

### Mandatory gates

Pass describes the bounded plan. Unknown means evidence is still needed.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | A specific local task and evidence-backed limitation are described in sections 1–3. |
| 2. ML essential | Pass | The question tests learned predictions and model errors, not only an application. |
| 3. Train/adapt models | Pass | All three investigations train or systematically adapt models. |
| 4. Existing data accessible | Pass | The official release and a bounded preview expose images, reference text and document-group fields. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing reference labels or aggregate counts; no new raters or recordings. |
| 6. Precise research gap | Fail | The current formulation repeats established correction, error detection and copying approaches without a demonstrated unanswered failure. This rejects the current wording, not all Sinhala OCR research. |
| 7. Beyond application assembly | Pass | The research is tested through comparisons and removal tests; the interface is supporting work. |
| 8. Objective evaluation | Pass | Existing reference text and document IDs support the specified objective comparisons. |
| 9. 6–8 month feasibility | Unknown | A small OCR/correction run must establish workload and whether useful errors remain. |
| 10. Three connected contributions | Pass | Three connected questions have separate comparisons and results using a shared unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | The bounded plan uses CPU baselines and occasional modest GPU access, with no special hardware. |
| 12. Manageable data reuse | Unknown | Dataset CC BY 4.0 is documented; exact baseline checkpoint and code reuse terms still need checking. |
| 13. Useful negative findings | Pass | Simple baselines winning or a proposed method failing still answers the stated questions. |

**Next decision:** Keep X43 parked. Reopen it with the supervisor only after a baseline comparison identifies a specific unresolved failure and a defensible contribution beyond existing correction methods.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source checks](../../metadata/sri-lanka-practical-checks.json)
