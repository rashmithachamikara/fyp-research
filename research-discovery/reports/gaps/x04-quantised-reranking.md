[← Research candidates](../research-candidates.md)

# Preserving search relevance when compact rerankers are quantised

**ID:** X04 · **Area:** NLP / information retrieval / efficiency · **Status:** Further validation needed

**Evidence and scoring reviewed:** 28 October 2026

## 1. Problem

Quantisation can change which document a search system returns even when ordinary accuracy appears stable. A September 2026 paper demonstrates this for a MiniLM cross-encoder as well as embedding models, so discovering ranking flips is already occupied.

**Potential stakeholders:** Developers operating search and document-retrieval systems under latency constraints.

## 2. Research gap and question

**Tentative gap:** Investigate training that preserves relevance-bearing pairwise margins under activation-and-weight quantisation and domain transfer. The neighbour explicitly leaves activation quantisation untested and asks whether training can improve useful margins. This supports an opportunity, not certified originality for a particular loss.

**Research question:** Can margin-preserving training reduce relevance loss from an INT8 compact reranker under held-out-domain testing at matched candidate depth and actual latency?

**Hypothesis and rival explanation:** Quantisation-aware pairwise consistency will preserve judged relevance better than ordinary fine-tuning followed by quantisation. Rival explanation: gains come from the loss/negative pool alone, or INT8 causes negligible damage and needs no special method.

**Novelty status:** provisional. The documented search boundary does not establish that no prior work exists. These are AI-assisted candidate ideas for team and supervisor discussion.

## 3. Evidence from closest work

| Existing work | Already covers | Proposed distinction | Evidence read |
|---|---|---|---|
| [The Undetected Damage of Quantization, September 2026](https://arxiv.org/html/2609.24322v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2609.24322) | Ranking damage, cross-encoder tests, gap sensitivity and mixed-precision fixes. | Conclusion asks about training; limitations restrict experiments to weight-only 3/4-bit quantisation and same-distribution calibration. | Full text; cross-encoder results and limitations; Sections 5.3, 7 and Limitations (X04-L1) |
| [Quantize by Drift, October 2026](https://arxiv.org/html/2610.09227v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2610.09227) | Behaviour-based mixed-precision post-training quantisation of text embedders. | A training objective for rerankers is different, but must beat simple allocation and uniform quantisation controls. | Full text; setup and limitations; Sections 3–4 and 8 (X04-L2) |
| [Reproducing and Comparing Distillation Techniques for Cross-Encoders, 2026](https://arxiv.org/html/2603.03010v1) · [Zotero](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2603.03010) | MarginMSE/other objectives, multiple backbones and negative-source confounding. | Control loss and negative pools before attributing a gain to quantisation-aware training. | Full text; controlled framework and limitations; Sections 3–5 and 7 (X04-L3) |

[Import these 3 literature records](https://literature.researchfasttrack.com/zotero?ids=10.48550%2FarXiv.2609.24322,10.48550%2FarXiv.2610.09227,10.48550%2FarXiv.2603.03010). Source-specific claims and access limits are in the [evidence ledger](../../metadata/evidence-ledger.csv).

## 4. Proposed approach

Keep a BM25 top-100 candidate set fixed. Fine-tune a small cross-encoder with quantisation-aware pairwise consistency, then investigate a bounded full-precision fallback policy. Count both models and fallback calls in memory/latency. Begin with a real INT8 CPU backend; simulated low-bit arithmetic is not evidence of a speedup.

## 5. Data and resources

| Item | Current position |
|---|---|
| Primary sources | [BEIR author framework](https://github.com/beir-cellar/beir) and its [NFCorpus](https://huggingface.co/datasets/BeIR/nfcorpus) and [SciFact](https://huggingface.co/datasets/BeIR/scifact) releases. |
| Access and labels | Official BEIR ZIP/loading example inspected; dataset cards show roughly 3,633 NFCorpus and 5,183 SciFact documents. Use public query relevance judgments, not model-generated relevance. |
| Licence and limitations | BEIR release cards declare CC BY-SA 4.0 for these datasets; framework/model licences are separate. Unjudged documents are not guaranteed irrelevant. |
| Training and transfer | Use NFCorpus training queries and source validation; hold SciFact evaluation queries out of adaptation and calibration. Check query/document duplicates. No new clinical annotations are needed. |
| Resources, estimated | Small corpora and CPU INT8 inference; 8–16 GB RAM, under 10 GB disk, occasional 8 GB GPU for fine-tuning. Actual speed, RAM and training time unmeasured. |
| Fallback / prototype | Top-20 candidates or a frozen encoder plus trained head; state the narrower scope. Local ranked-search demo with relevance and latency comparisons. |

All resource estimates are planning assumptions unless explicitly labelled as a source measurement or local data check. No model training, timing or benchmark reproduction was performed in this discovery pass.

## 6. Three-member contributions

| Member | Question and hypothesis | Method investigation | Baseline and ablation | Assessable result |
|---|---|---|---|---|
| A: training pairs | Do matched hard-negative curricula help robustness after compression? H: A learned negative curriculum preserves useful margins after compression. | Learn a margin-sensitive curriculum using source relevance. | Random/fixed hard negatives; equal pairs and updates. | Relevance versus margin distribution and negative difficulty. |
| B: quantisation | Does paired FP/INT8 consistency protect useful ranking margins? H: Paired quantisation consistency reduces relevance loss. | Train a quantisation-aware consistency objective. | Ordinary QAT and MarginMSE; remove consistency. | nDCG loss at matched model and bit budget. |
| C: fallback policy | Can source-trained routing recover relevance within a fixed compute budget? H: Learned fallback improves relevance at the same measured latency. | Learn selective FP fallback from source-validation features. | Always INT8, always FP, random fallback and fixed thresholds. | Quality–latency frontier including router and FP cost. |

All three address one shared problem and may share datasets, features, models and evaluation code. Test each intervention on the unchanged common baseline so a member can obtain findings even if another proposed method fails. Combine them only after individual effects are interpretable. Separate projects and papers are not required; paper writing is optional.

## 7. Evaluation

- **Primary metric:** Held-out-domain nDCG@10 at a predefined measured reranking-latency budget; freeze candidate depth before testing.
- **Split:** Source train/selection/calibration queries disjoint; target-domain judgments used only for final evaluation. Record checkpoint pretraining and exclude target-fine-tuned checkpoints.
- **Baselines and code:** BM25; FP and INT8 [MiniLM-L6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2); ordinary QAT, MarginMSE and the published gap-sensitive PTQ idea. Use [Sentence Transformers training code](https://github.com/huggingface/sentence-transformers).
- **Ablations:** Curriculum, paired consistency and routing separately; same teacher, candidate list, negatives, token limits and seeds. Report weight-only versus activation-plus-weight quantisation distinctly.
- **Uncertainty and errors:** Paired query bootstrap and repeated training seeds; latency distributions under fixed threads/batch size with warm-up. Analyse low margins, document length, domain and partial relevance judgments.
- **Useful result without winning:** If INT8 has negligible quality loss or routing costs erase savings, demonstrate when ordinary INT8 is sufficient. FP ranking changes alone do not prove relevance harm.
- **Interpretation limit:** Relevance judgments support retrieval-quality claims, not factual correctness of generated answers or energy savings.

## 8. Score and next decision

**Provisional score: 79.2/100.** This is a comparative proposal score, not a measured model result or topic qualification. Novelty is 3/5; the required rating is 4/5. The design gates pass at proposal level, but the novelty threshold is unmet.

### Weighted rubric

The nine relative weights total 98. Weighted points below are out of 98; the final total is normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | **3** | 9.6 | Medium: a precise training/activation-quantisation opening is documented, but MarginMSE/QAT/routing combinations still need a sharper original method. |
| Public dataset quality/accessibility | 15 | 4 | 12.0 | Medium-high: author loading route, small corpora, judgments and release licences inspected; payload not downloaded. |
| Feasibility and learning curve | 14 | 4 | 11.2 | Medium: compact reranking and capped query lists fit the timeline; QAT and backend measurement are the main learning costs. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium-high for design: curriculum, quantisation-aware objectives and learned routing are empirical research contributions. |
| Evaluation/reproducibility | 12 | 5 | 12.0 | Medium-high for design: fixed candidates, matched negatives, paired judgments and actual backend costs directly test the claim. |
| Three-member structure | 12 | 4 | 9.6 | Medium: pair curriculum, QAT objective and fallback policy can each be tested against the same baseline. |
| Real-world significance | 9 | 4 | 7.2 | Medium: documented relevance instability matters for search; downstream answer reliability is outside the claim. |
| Compute/storage | 5 | 4 | 4.0 | Medium: small corpora and CPU inference fit; training and routing-memory estimates need profiling. |
| Prototype | 3 | 4 | 2.4 | Medium-high: a local search comparison is a bounded prototype. |
| **Normalised total / 100** | **98** |  | **79.2** | **Not qualified; category thresholds and gate status still control.** |

### Mandatory gates

Pass means the bounded proposal is supported at design level; it does not mean a successful experiment. Unknown gates prevent qualification even when a provisional comparison score is given. No gate was waived to increase the candidate count.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 and the closest-work evidence support a concrete failure mode; the new method's benefit is untested. |
| 2. ML essential | Pass | Learning, adaptation or systematic model evaluation is central to the question. |
| 3. Train/adapt models | Pass | Section 4 defines trainable objectives, heads or policies; no paid inference API is required. |
| 4. Existing data accessible | Pass | Section 5 records an original public release or author-documented loading route, existing labels and the access-check limit. |
| 5. No unavailable human evaluation | Pass | Evaluation uses existing annotations or observed values; no new participants, questionnaires or expert labels. |
| 6. Precise research gap | Pass | Section 2 defines a bounded question; Section 3 distinguishes the documented limitation from the inferred method opportunity. |
| 7. Beyond application assembly | Pass | Section 6 investigates learned interventions with baseline comparisons and ablations, rather than application assembly. |
| 8. Objective evaluation | Pass | Section 7 defines objective outcomes, grouping, controls and uncertainty treatment. |
| 9. 6–8 month feasibility | Pass | The bounded core and fallback in Section 5 are plausible within the team window; training costs remain estimates. |
| 10. Three connected contributions | Pass | Three contributions share one problem and infrastructure but can each be assessed against the unchanged baseline. |
| 11. No specialised/continuous high-end compute | Pass | Core design uses CPU work or an occasional modest GPU; no specialised sensor, paid service or continuous server GPU. |
| 12. Manageable responsible use | Pass | Section 5 records source terms and a bounded offline use; no deployment or high-stakes benefit is assumed. |
| 13. Useful negative findings | Pass | Section 7 identifies an interpretable negative result if the proposed method does not outperform the baseline. |

**Decision:** One of the strongest additional directions to investigate; novelty remains 3/5 and the score is a proposal assessment.

**Next decision point:** Run a small real-backend FP-versus-INT8 relevance pilot. If there is no material loss, narrow to a demonstrated lower-precision failure before developing a new objective. Discuss the resulting evidence and contribution boundaries with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) | [Search and comparison records](../../metadata/expansion-records.json).
