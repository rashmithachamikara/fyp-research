[← Research candidates](../research-candidates.md)

# Reading Sinhala documents without introducing new mistakes

**ID:** X43 · **Area:** Computer vision and NLP — Sinhala document reading

**Status:** Provisional research opportunity; not qualified · **Checked:** 30 October 2026

**Score:** 76.7/100, provisional · **No model has been trained or timed.**

**The idea:** Improve text read from a scanned Sinhala page, while avoiding unnecessary changes to correct words and numbers.

## 1. Problem

Libraries, publishers and public offices may need searchable copies of printed Sinhala documents. OCR means reading text from an image. A second model can try to repair OCR mistakes, but it might also change text that was already correct.

**Example:** A date or section number is read correctly, but an automatic “correction” changes it. This is an example of the risk, not an observed result from our own experiment.

## 2. Research gap and question

**Question:** Can a small correction model fix remaining Sinhala OCR errors while making fewer unnecessary edits, especially to numbers?

**Already done:** Recent Sinhala page-level OCR already performs strongly on legislative documents. Simply fine-tuning another OCR model, or adding a language-model corrector, is not a new contribution.

**What to investigate:** Investigate the trade-off between fixing errors and damaging correct text. Train a model to propose corrections, and a separate small model to estimate whether a proposed change helps. Compare this with simple rules and existing constrained editing. Whether this is a new Sinhala OCR contribution remains unverified.

**Prediction to test:** A correction rule trained on actual OCR mistakes will make fewer harmful changes than unrestricted text rewriting. It may instead turn out that leaving the strong OCR output unchanged is best.

## 3. Evidence from closest work

| Source | Why it matters | What was checked |
|---|---|---|
| [Sinhala legislative OCR dataset](https://huggingface.co/datasets/avishadilhara/sinhala-ocr-lk-acts-1010) | The official card lists a real-page dataset, licence and source-document fields. File listing and a row preview were checked. | Dataset card, manifest and bounded preview; no image inspection. |
| [Cross-Temporal Sinhala OCR](https://arxiv.org/html/2606.29378) | The paper already adapts page-level OCR and limits its claims to legislative documents. Another generic Sinhala OCR fine-tune would overlap. | Dataset, experiments and limitations sections inspected; no reproduction. |
| [Confident but Wrong](https://arxiv.org/html/2609.29680) | This studies translation post-editing, not OCR. It already diagnoses harmful edits and unreliable confidence, so confidence-based editing itself is not new. | Abstract and methods outline inspected; adjacent-task comparison. |
| [Existing Sinhala OCR post-processing](https://www.theekshana.lk/project/optical-character-recognition-for-sinhala/) | UCSC/Theekshana already describes a Sinhala OCR post-processing engine. Do not claim to introduce Sinhala post-processing. | Original project description checked. |

The problem evidence and the proposed solution are different things. No baseline failure or improvement has been demonstrated by this project. The searches do not prove novelty. [Search and data-check record](../../metadata/sri-lanka-practical-checks.json).

## 4. Proposed approach

Choose one fixed OCR engine first. On training pages only, align its output with the released correct text to create correction examples. Train a small corrector and an edit-selection head. Keep the original output available so that a proposed edit can be rejected. Do not assume the model’s confidence is reliable.

**Simple prototype:** show a held-out example, the baseline answer, the proposed answer and any uncertainty. Building the screen is supporting work, not a member’s research contribution.

## 5. Data and resources

**Existing data:** The public sinhala-ocr-lk-acts-1010 release contains 1,010 legislative pages with reference text. Its card states CC BY 4.0 and about 872 MB. A bounded preview returned 45 rows and confirmed image, text, year, doc_id and page_num fields. The file listing contains four Parquet files. Images were not downloaded for visual inspection and no OCR baseline was run.

**What the team needs:** Estimate: cached OCR output, small correction models and an occasional modest GPU. Start with 100 training pages to measure time and memory. A larger OCR model is a comparison, not a requirement for every experiment.

**Fallback:** Keep the OCR engine frozen and train only the correction/selection models. If the starting engine makes too few useful errors, report that correction is unnecessary on this dataset instead of manufacturing an improvement.

Costs and training times are estimates until measured. No paid services, new participants or guaranteed university GPU are assumed.

## 6. Three-member contributions

One shared problem, three testable contributions. Each can start from the same unchanged baseline; another member’s proposed method does not have to succeed first.

| Member | Question and prediction | Method, baseline and removal test | Separate result |
|---|---|---|---|
| A: Better correction examples | Does learning actual OCR confusions beat generic text rewriting? H: real error patterns help. | Train a compact corrector; compare dictionary rules and equal-sized synthetic-error training; remove real-error examples. | Character errors fixed versus new errors introduced. |
| B: Choosing when to edit | Can a model predict whether an edit helps? H: a trained edit selector beats a fixed confidence threshold. | Train against reference text; compare no selection, edit-distance limits and confidence thresholds; remove image/OCR features. | Useful corrections at matched numbers of harmful edits. |
| C: A smaller corrector | Can compression preserve careful copying and number accuracy? H: copy-aware training helps the smaller model. | Compare a compact student, ordinary teacher imitation and copy-weighted training; remove copy/number weighting. | Error rate, exact numeric-token matches, memory and measured processing time. |

All members share data and evaluation code. Papers are optional. “Removal test” means taking out the proposed change to see whether it actually helped.

## 7. Evaluation

- **Main measures:** Character error rate: the share of characters that are inserted, deleted or read wrongly. Also count harmful edits that turn correct text into wrong text, and exact matches for digit-containing tokens. Do not claim to protect all personal names without name labels.
- **Fair data split:** Keep pages from the same legislative document together using doc_id. Publish a document-grouped split and report the released split separately for comparison. Keep test documents out of the error examples and tuning process.
- **Comparisons:** Unchanged Tesseract/Surya output, simple dictionary or edit-distance correction, a small ordinary text corrector, and a strong Sinhala-adapted OCR model such as the published LightOnOCR baseline. Check exact checkpoint/code licences before reuse.
- **Removal tests:** use the member-specific comparisons above and keep training/tuning budgets matched.
- **Uncertainty and useful failures:** Repeat trainable methods with three seeds. Use document-level confidence intervals, not independent characters. Analyse old/new pages, numbers and initially correct words. A useful result is that a simple edit limit or no correction performs best.
- **What the results cannot prove:** The verified dataset contains legislative pages. It cannot establish reliable handwriting recognition, arbitrary phone-photo reading or automatic form processing.

## 8. Score and next decision

**Provisional score: 76.7/100; not qualified.** This is a promising practical direction, not a verified new gap. The score describes the plan; unknown gates still prevent selection.

### Weighted rubric

The existing nine weights total 98 and are normalised to 100. Ratings use the project’s provisional comparison policy. Decimal totals are arithmetic, not scientific certainty.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: careful editing is established generally; the added Sinhala OCR question needs a deeper comparison. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium: real Sinhala images, references and document identifiers have a verified public route; full quality audit remains. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: frozen OCR and small correctors offer a bounded 6–8 month plan; no timing measured. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: correction, edit selection and compact-model training are empirical ML work. |
| Evaluation/reproducibility | 12 | 4 | 9.6 | Medium: reference text supports character errors and harmful-edit counts without new raters. |
| Three-member structure | 12 | 4 | 9.6 | Medium: three investigations can use the same unchanged OCR output independently. |
| Real-world significance | 9 | 4 | 7.2 | Medium: searchable Sinhala documents are a direct local use; savings have not been measured. |
| Compute/storage | 5 | 4 | 4.0 | Medium: cached outputs reduce repeated GPU work; resource figures are estimates. |
| Prototype | 3 | 4 | 2.4 | Medium: a page, original text and highlighted edits make a simple prototype. |
| **Normalised total / 100** | **98** | | **76.7** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan. Unknown means evidence is still needed.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | A specific local task and evidence-backed limitation are described in sections 1–3. |
| 2. ML essential | Pass | The question tests learned predictions and model errors, not only an application. |
| 3. Train/adapt models | Pass | All three investigations train or systematically adapt models. |
| 4. Existing data accessible | Pass | The official release and a bounded preview expose images, reference text and document-group fields. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing reference labels or aggregate counts; no new raters or recordings. |
| 6. Precise research gap | Unknown | OCR post-processing and confidence-constrained editing already exist; the specific added contribution is not established. |
| 7. Beyond application assembly | Pass | The research is tested through comparisons and removal tests; the interface is supporting work. |
| 8. Objective evaluation | Pass | Existing reference text and document IDs support the specified objective comparisons. |
| 9. 6–8 month feasibility | Unknown | A small OCR/correction run must establish workload and whether useful errors remain. |
| 10. Three connected contributions | Pass | Three connected questions have separate comparisons and results using a shared unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | The bounded plan uses CPU baselines and occasional modest GPU access, with no special hardware. |
| 12. Manageable data reuse | Unknown | Dataset CC BY 4.0 is documented; exact baseline checkpoint and code reuse terms still need checking. |
| 13. Useful negative findings | Pass | Simple baselines winning or a proposed method failing still answers the stated questions. |

**Next decision:** Run one fixed OCR baseline on a small document-grouped subset. Check that enough correctable errors remain, then review the precise editing contribution with the supervisor.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source checks](../../metadata/sri-lanka-practical-checks.json)
