[← Research candidates](../research-candidates.md)

# Knowing when to decide: Sinhala deepfake speech detection as audio arrives

**ID:** X33 · **Area:** Audio ML — streaming deepfake detection  
**Status:** Provisional opportunity; not qualified · **Checked:** 29 October 2026  
**Provisional score:** 62.0/100 · **No model has been trained or timed.**

**Quick explanation:** A detector hears a little speech, then chooses whether to decide or wait for more. We would test whether it can make fewer rushed mistakes on Sinhala speech while staying small enough for an ordinary phone.

## 1. Problem

Waiting for a whole recording can make a warning arrive late. Deciding after a very short sound can cause mistakes. Telephone compression can also remove clues that the model uses.

The useful question is: **how much speech does the detector need before its answer is reliable?**

For example, a system might show “not enough evidence yet” after half a second, then decide after hearing more. This is an illustration, not a measured result.

The target is generated or voice-converted speech. Detecting it does not establish fraud, lack of consent or who is speaking.

## 2. Research gap and question

**Question:** With little labelled Sinhala audio, can a small model learn when to decide and when to wait, while handling unfamiliar voice-generation tools and telephone compression?

Here, **streaming** means processing speech as it arrives. A **generator** is a tool that creates synthetic speech. A **codec** compresses audio for transmission.

**Possible contribution:** Train a small waiting policy that uses the detector's past scores to decide whether more speech is needed.

**Hypothesis:** This policy can warn sooner at comparable error rates and decision coverage, meaning the share of recordings it actually decides.

**Alternative explanation:** A simple confidence threshold or fixed waiting time works just as well. Any apparent gain might come from leaving more difficult recordings undecided.

**Novelty is unverified.** Short-input detection, small models, limited-language adaptation and streaming confidence rules already exist. Using Sinhala or combining those features does not by itself establish a new contribution. We need a specific failure of existing methods and evidence that the proposed change addresses it.

This is different from [X32](x32-sinhala-partial-audio-deepfakes.md), which asks where words were replaced inside a recording.

## 3. Evidence from closest work

| Study | What already exists | Implication for this project |
|---|---|---|
| [Sinhala AI-generated voice framework, ICAC 2025](https://doi.org/10.1109/ICAC69156.2025.11361479) · [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/icac69156.2025.11361479) | Separate Sinhala, Tamil and English human/synthetic classifiers using CNN–LSTM models. | A generic Sinhala detector already has direct precedent. The supplied full paper does not report a learned streaming waiting policy. Sections III–V read. |
| [Are audio DeepFake detection models polyglots?](https://www.isca-archive.org/spsc_2025/marek25_spsc.pdf) · [Cite](https://literature.researchfasttrack.com/cite?id=10.21437/spsc.2025-8) | Adapts detectors using limited target-language data. Sinhala is not tested. | Small-data language adaptation is an established comparison, not the novelty. Full paper inspected. |
| [Detection at the First Greeting, ICASSP 2026](https://arxiv.org/html/2601.19573v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/icassp55912.2026.11463587) | Lightweight detection from 0.5–2-second clips under communication degradation. | Short input and low model cost are already studied. Fixed clips do not settle how to decide repeatedly as speech arrives. Methods inspected. |
| [How Fast, How Sure, and Where It Breaks, 2026 preprint](https://doi.org/10.21203/rs.3.rs-10257178/v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.21203/rs.3.rs-10257178/v1) | Uses a frozen detector, growing audio prefixes, confidence adjustment and early decisions under telephone codecs. Confidence transfer can fail across channels. | The closest overlap. Our learned waiting policy must add value beyond its confidence-threshold rule. Full manuscript sections 3–5 read through a ResearchGate copy; direct publisher access failed. Results were not reproduced. |
| [RTCFake, ACL Findings 2026](https://arxiv.org/html/2604.23742v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.18653/v1/2026.findings-acl.285) | Studies speech detection after communication-platform processing and proposes training for better platform transfer. | Channel robustness also has direct prior work. Selected full-text methods and results inspected. |

The possible gap is the **added value of a learned waiting policy with little Sinhala data**, not the first streaming or telephone-robust detector. The search does not establish that no similar policy exists.

## 4. Proposed approach

1. Reproduce an existing detector and the simple streaming threshold rule.
2. Feed the model only the audio available at each moment. It must never hear later speech before making an earlier decision.
3. Train the waiting policy using past scores and elapsed time.
4. Compare it with fixed waiting times and tuned confidence thresholds.
5. Train a smaller detector and check whether early decisions survive the size reduction.

**Prototype:** Replay existing audio in small chunks and display “possible synthetic speech,” “human speech so far” or “not enough evidence.” An early human decision cannot certify the rest of a conversation.

Begin with controlled single-speaker recordings that are wholly human or wholly generated. Mixed human/AI recordings and live calls need additional data and separate evaluation.

## 5. Data and resources

| Source | What is available or documented | Limitation |
|---|---|---|
| [OpenSLR SLR52](https://openslr.org/52/) | About 185,000 Sinhala utterances, speaker/text metadata and public audio downloads; CC BY-SA 4.0. | Human speech only. It does not supply generated examples or actual telephone conversations. |
| Sinhala ICAC dataset, above | Paper describes 4,000 human and 4,000 generated Sinhala samples. | No public release or reuse licence was verified. Speaker and generator records also need checking. |
| [ASVspoof 2019](https://datashare.ed.ac.uk/handle/10283/3336) | English benchmark used by the closest streaming study and [AASIST author implementation](https://github.com/clovaai/aasist). AASIST provides code and pretrained models. | Proposed baseline/fallback only. The dataset page timed out in this check; verify download, licence and source records before use. English results cannot establish Sinhala performance. |
| [RTCFake challenge release](https://huggingface.co/datasets/JunXueTech/RTCFake) | English/Chinese, approximately 400 hours; CC BY-NC 4.0. Access requires team registration and some evaluation data are withheld. | No Sinhala. Access was not requested; it is an optional later test, not a secured dependency. |

**Data blocker:** A reusable Sinhala real/fake dataset with several speakers and generation tools is still missing. Human audio alone is insufficient. A permitted route for creating derivatives from existing data could help, but tool licences, speaker reuse terms and module rules must first be verified. No new recordings are assumed.

**Estimated resources:** A selected 5–10-hour dataset, 16–32 GB RAM and roughly 30–100 GB working storage for audio, models and experiments. A modest GPU should be sufficient for small-model experiments; a larger teacher is optional. These are planning estimates, not measurements.

Use an ordinary phone for measured inference tests after a baseline works. Do not assume an installed app can capture both sides of a call: [Android documents privileged access requirements](https://developer.android.com/media/platform/sharing-audio-input). Replaying existing files avoids making live call capture a project dependency.

## 6. Three-member contributions

### Member A: learn from little Sinhala data

**Question and expectation:** Does a small amount of Sinhala training improve detection on a generator excluded from training?

Train a small adaptation layer at several fixed data budgets. Compare no adaptation and ordinary fine-tuning. Remove the extra training objective to check its effect.

**Separate result:** Detection errors versus labelled minutes and distinct speakers.

### Member B: decide or wait

**Question and expectation:** Can a learned waiting policy reduce delay while keeping errors and the share of decided recordings comparable?

Train a small policy using past scores. Compare fixed-duration decisions and the closest study's threshold rule. Remove score history to test whether it helps.

**Separate result:** The relationship between warning delay, errors and undecided recordings. This is the central proposed gap.

### Member C: preserve early decisions in a small model

**Question and expectation:** Can a small model learn from a larger model without losing the evidence needed for early decisions?

Compare training from the larger model's early-prefix outputs with ordinary training and learning only from its final answer. Then test lower-precision model storage.

**Separate result:** Detection quality versus model size, measured memory and speed on a named device.

All members use the same shared data and unchanged starting model. Each can obtain findings even if another member's proposed method fails. Data access is their shared prerequisite. Building the interface is supporting work; papers are optional.

## 7. Evaluation

- **Primary measure:** Mean time to a correct synthetic-speech warning, compared at matched fake-detection rates and decision coverage. Show delay only alongside the missed and undecided cases below. Choose thresholds on validation data with a target of at most 1% of genuine clips receiving any false alert; this is a planning target, not an achieved guarantee. Report the actual false-alert rate on every test condition.
- **Count all outcomes:** Report missed fakes, wrong human decisions, false alerts and undecided clips alongside delay. Show a curve across waiting times. Fast decisions on only easy examples do not establish an improvement.
- **Keep data separate:** Split by speaker and original recording before making compressed versions. Keep linked source/donor examples together. Hold out a generation-tool family and separately a codec setting. Use the same test recordings for every method.
- **Fair baselines:** Simple audio features with a classifier; AASIST or AASIST-L; a strong pretrained speech detector; ordinary Sinhala fine-tuning; fixed waiting times; and the published streaming threshold rule. Audit input padding because repeating short audio can change results.
- **Removal tests:** Remove adaptation, score history and early-prefix imitation separately. Keep training examples and tuning effort comparable.
- **Uncertainty and errors:** Use three training seeds and 95% confidence intervals grouped by speaker/source. Analyse short speech, unfamiliar generators, compression and noise. Overlapping checks are not independent recordings.
- **Full timing:** Count waiting for audio, feature extraction, prediction and policy processing. For example, 1 second of audio plus 50 ms of processing means at least 1.05 seconds to decide. Measure peak memory and whether repeated updates keep up on the phone.
- **Useful negative findings:** A threshold may be enough; language adaptation may stop helping on new generators; compression may make early decisions unreliable; a smaller model may need more speech.
- **Claim limits:** Short recorded clips cannot establish false alarms per real call or protection throughout a conversation. Those claims need existing representative long-call data and repeated-decision tests. This study does not determine malicious intent.

## 8. Score and next decision

**Verdict: adjust before proceeding. Provisional score: 62.0/100; not qualified.** Five gates remain Unknown. This is a separate assessment from X32; the equal total reflects similar unresolved data and novelty risks.

### Weighted rubric

The nine existing weights total 98 and are normalised to 100. Ratings describe the current plan, not achieved performance.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | Low: A close streaming study already exists; the added value of learning when to wait is unverified. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: Suitable reusable Sinhala human and generated speech has not been secured. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Low-medium: A bounded study is plausible once data and the first baseline work. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: The plan trains adaptation, a waiting policy and a compact model. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: Comparisons are defined, but suitable Sinhala test data and phone timings are missing. |
| Three-member structure | 12 | 4 | 9.6 | Medium: Each member can test a separate idea against the same unchanged starting model. |
| Real-world significance | 9 | 4 | 7.2 | Medium: Quick, reliable speech checks matter; protection during actual calls remains untested. |
| Compute/storage | 5 | 4 | 4.0 | Medium-low: Small selected datasets and compact models should fit; resource use is not measured. |
| Prototype | 3 | 4 | 2.4 | Medium: Existing audio can be replayed in small chunks without access to private calls. |
| **Normalised total / 100** | **98** | | **62.0** | **Not qualified.** |

### Mandatory gates

Unknown gates must be resolved before selection. Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Studies in section 3 show that short input and telephone processing affect detection and confidence. |
| 2. ML essential | Pass | The question concerns a learned detector and when it has enough evidence to decide. |
| 3. Train/adapt models | Pass | All three contributions train or adapt models rather than only call an API. |
| 4. Existing data accessible | Unknown | No suitable reusable Sinhala real/fake dataset with speaker and generator records has been secured. |
| 5. No unavailable human evaluation | Pass | The bounded study uses existing labels. New callers, recordings and expert labelling are excluded. |
| 6. Precise research gap | Unknown | Streaming, short-input and limited-language detection already exist; the extra contribution needs checking. |
| 7. Beyond application assembly | Pass | Training and comparison experiments are central; the app only demonstrates the result. |
| 8. Objective evaluation | Unknown | Metrics are defined, but suitable Sinhala data, source groups and clip lengths are not verified. |
| 9. 6–8 month feasibility | Unknown | Data access and baseline reproduction must be resolved before the schedule is credible. |
| 10. Three connected contributions | Pass | Section 6 gives separate questions, methods, comparisons and results for one shared problem. |
| 11. No specialised/continuous high-end compute | Pass | The core uses selected audio and compact models; large-model training is optional. |
| 12. Manageable data reuse | Unknown | Rights for the actual Sinhala fake audio and any generated derivatives remain unresolved. |
| 13. Useful negative findings | Pass | Standard methods may suffice; waiting may not help; compression may damage early detection. |

**Next decision:** Review the proposed waiting-policy contribution and existing-data route with the supervisor before committing to this topic.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Searches and source checks](../../metadata/source-checks/sinhala-streaming-gap-validation.json)

[Import these 5 papers into Zotero or EndNote](https://literature.researchfasttrack.com/zotero?ids=10.1109/icac69156.2025.11361479,10.21437/spsc.2025-8,10.1109/icassp55912.2026.11463587,10.21203/rs.3.rs-10257178/v1,10.18653/v1/2026.findings-acl.285).

