[← Research candidates](../research-candidates.md)

# Transcribing Sinhala speech that includes English words

**ID:** X38 · **Area:** Speech ML — Sinhala–English transcription

**Status:** Provisional; Reject as written; natural mixed-speech test labels missing; not qualified · **Imported:** 30 October 2026

**Provisional score:** 53.3/100 · No model training or timing performed.

**In plain language:** Test whether synthetic mixed-language training improves real Sinhala–English transcription without new recordings.

**Origin:** supplied shortlist, rank 5, page(s) 5–6. Its source verdict was “GO with reframing”. This brief uses the team’s current criteria; the source rank and verdict are not our qualification decision. [Import record](../../metadata/pdf-shortlist-import.json).

## 1. Problem

A person may speak Sinhala but use an English product name or technical phrase. A transcription model can miss the English words or change the surrounding Sinhala. Ordinary Sinhala-only test results do not show whether it handles these switches.

## 2. Research gap and question

**Question:** Can permitted synthetic Sinhala–English training examples improve transcription on an existing, independently transcribed natural mixed-speech test set?

**What is still uncertain:** Synthetic code-switching and ASR adaptation already exist. The PDF correctly treats routine LoRA fine-tuning as an ablation, not novelty. A distinct Sinhala failure and a reusable natural mixed-speech test set have not been verified.

**Hypothesis and alternative:** Training on well-placed language switches will reduce errors around switches on real speech. An alternative is that gains are limited to synthetic voices or reflect repeated source sentences.

## 3. Evidence from closest work

This is a bounded import check, not a complete novelty audit. “Checked” below refers to the stated abstract or source page, not a reproduction of the study. The supplied PDF’s wider search and verification claims are not independently certified.

| Source | What it supports | Reading limit |
|---|---|---|
| [OpenSLR SLR52](https://openslr.org/52/) | Official source lists about 185K Sinhala utterances, transcripts, audio archives and CC BY-SA 4.0. Mixed-language test suitability is not established. | Official dataset page checked; media not downloaded. |
| [CS-FLEURS](https://arxiv.org/abs/2509.14161) | The abstract describes multilingual code-switched read and synthetic speech. A natural conversational Sinhala test subset is not verified. | Primary abstract checked; methods not reviewed. |

## 4. Proposed approach

First verify a natural labelled test set. Generate permitted training variants from existing text or speech with known transcripts, then adapt a small ASR model. Audit whether the chosen synthesis model actually pronounces both languages before producing a large dataset.

**Prototype:** demonstrate the same research pipeline on held-out existing examples, showing its output, errors and uncertainty. The interface is supporting work, not an individual research contribution.

## 5. Data and resources

**Data and access:** OpenSLR SLR52 officially provides about 185K Sinhala utterances under CC BY-SA 4.0 and links transcripts and audio archives. This does not establish natural Sinhala–English test coverage. CS-FLEURS provides several synthetic/read code-switched settings, but Sinhala subset availability and its naturalness need inspection. The PDF’s proposed new natural recordings and transcription violate the current no-primary-data constraint.

**Resources:** Estimate only: select a small existing audio subset and adapt a compact recogniser with occasional GPU use. The licence and pronunciation quality of the proposed SinhalaVITS checkpoint are not verified. Do not assume a large paid speech API budget.

**Fallback:** Use an already released, licensed Sinhala–English test set if found. Testing only synthetic speech supports a synthetic benchmark claim, not improved real call transcription. Otherwise park the current scope.

These are feasibility estimates, not demonstrated training costs. The PDF’s resource allowance does not establish this team’s actual GPU or paid-service access.

## 6. Three-member contributions

All members address the shared question in section 2. Each investigation starts from the same unchanged baseline so that another member’s proposed improvement is not a prerequisite.

| Member | Question and hypothesis | Method, comparison and removal test | Independently assessable result |
|---|---|---|---|
| A: Synthetic training quality | Which switch placement transfers best? H: phrase-level switches beat arbitrary word replacement. | Train identical ASR adapters on equal-sized data variants; remove switch-aware generation. | Natural-test WER near switch points versus an unchanged recogniser. |
| B: Adaptation balance | Can adaptation improve English words without damaging Sinhala? H: mixed rehearsal helps. | Compare ordinary adaptation, Sinhala rehearsal and mixed rehearsal; remove rehearsal. | English-word recall and Sinhala WER on held-out speakers. |
| C: Confidence and compactness | Can a small confidence model identify unreliable mixed phrases? H: switch-aware confidence improves error ranking. | Train on unchanged ASR outputs; compare raw decoder confidence and a head without switch features. | Error-detection precision/recall and WER at matched retained coverage, with measured latency. |

Shared data access is a common prerequisite. A failed proposed method can still produce an interpretable comparison. Papers are optional; the work must remain attributable through experiments and removal tests. Where the gate table marks the team structure Unknown, the shared data barrier prevents treating this as an execution-ready split.

## 7. Evaluation

- **Primary measure:** Word error rate (WER), with separate Sinhala/English errors and error rate near switch points. Fix script, number and spelling normalisation rules before testing and publish both raw and normalised results.
- **Keep data separate:** Hold out speakers, recordings and source text before generating variants. Keep generated descendants with their originals. The final real-speech test set must be independent of synthesis and training.
- **Baselines:** An unchanged multilingual Whisper model, an ordinary Sinhala-adapted recogniser and matched-budget mixed-language adaptation; a conventional small CTC recogniser is the simpler comparison if usable code permits.
- **Removal tests:** use the member-specific tests above; keep data, tuning effort and inference budgets comparable.
- **Uncertainty, error analysis and useful negative findings:** Analyse switch type, accent, noise and English word frequency. Bootstrap by speaker and repeat adaptation with three seeds. A useful negative result could show no synthetic-to-natural transfer or Sinhala regression.
- **Claim limit:** benchmark findings support the stated task and conditions. They do not establish reliable real-world deployment or a guaranteed benefit for users.

## 8. Score and next decision

**Provisional score: 53.3/100; not qualified.** Reject as written; natural mixed-speech test labels missing. Ratings assess the imported proposal and access risks, not achieved results. Unknown gates block qualification; failed gates reject the current design regardless of score.

### Weighted rubric

The existing nine weights total 98. Scores are normalised to 100; decimals reflect arithmetic, not certainty. These comparison scores follow the existing provisional-scoring policy and do not override the gates.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | Low: code-switch synthesis and ordinary ASR adaptation already have close prior work. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: Sinhala speech exists, but the required independent natural mixed-language labels do not. |
| Feasibility and learning curve | 14 | 2 | 5.6 | Low: removing new recording and labelling needs a different data route. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: adaptation and confidence learning provide ML research. |
| Evaluation/reproducibility | 12 | 2 | 4.8 | Low: the real-speech reference test is not secured. |
| Three-member structure | 12 | 3 | 7.2 | Medium-low: all three studies depend on the same missing mixed-speech labels. |
| Real-world significance | 9 | 4 | 7.2 | Medium: mixed-language transcription has a clear practical use. |
| Compute/storage | 5 | 3 | 3.0 | Low-medium: bounded adaptation is plausible; model size and GPU time are unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: a replay-and-transcript demo is straightforward once data exist. |
| **Normalised total / 100** | **98** | | **53.3** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 defines a concrete failure and affected users; its local magnitude is not measured. |
| 2. ML essential | Pass | The shared question concerns learned predictions rather than only an interface. |
| 3. Train/adapt models | Pass | The bounded design includes training or systematic model adaptation. |
| 4. Existing data accessible | Unknown | No suitable independently transcribed natural Sinhala–English test set was verified. |
| 5. No unavailable human evaluation | Fail | The supplied natural test-set plan requires new recordings/transcription; current criteria exclude primary collection. |
| 6. Precise research gap | Unknown | A distinct Sinhala failure beyond established code-switch synthesis is unverified. |
| 7. Beyond application assembly | Pass | The proposal specifies learning experiments, comparisons and removal tests. |
| 8. Objective evaluation | Unknown | Natural speech labels, speaker groups and switch annotations are not secured. |
| 9. 6–8 month feasibility | Unknown | A no-new-recordings data route must be established. |
| 10. Three connected contributions | Unknown | Each investigation needs the same unavailable natural test reference. |
| 11. No specialised/continuous high-end compute | Pass | The retained scope starts with small models or cached features and no dedicated hardware. |
| 12. Manageable data reuse | Unknown | The exact combination of data, model and derivative-output reuse terms is not verified. |
| 13. Useful negative findings | Pass | Section 7 identifies useful findings even if the proposed method does not improve performance. |

**Next decision:** Resolve existing natural Sinhala–English test data with the supervisor; do not select a real-speech claim based only on synthetic labels.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source and import limits](../../metadata/pdf-shortlist-import.json)
