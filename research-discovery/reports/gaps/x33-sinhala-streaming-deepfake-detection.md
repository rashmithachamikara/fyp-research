[← Research candidates](../research-candidates.md)

# Knowing when to decide: Sinhala deepfake speech detection as audio arrives

**ID:** X33 · **Area:** Audio ML — streaming deepfake detection  
**Status:** Provisional; needs redesign; not qualified · **Checked:** 29 October 2026
**Provisional score:** 62.0/100 · **No model has been trained or timed.**

**Quick explanation:** A detector hears a little speech, then chooses whether to decide or wait for more. The problem is real, but learning this choice already exists. We have not yet shown a new Sinhala-specific failure or contribution.

## 1. Problem

Waiting for a whole recording can make a warning arrive late. Deciding after a very short sound can cause mistakes. Telephone compression can also remove clues that the model uses.

The useful question is: **how much speech does the detector need before its answer is reliable?**

For example, a system might show “not enough evidence yet” after half a second, then decide after hearing more. This is an illustration, not a measured result.

The target is generated or voice-converted speech. Detecting it does not establish fraud, lack of consent or who is speaking.

## 2. Research gap and question

**Question:** With little labelled Sinhala audio, can a small model learn when to decide and when to wait, while handling unfamiliar voice-generation tools and telephone compression?

Here, **streaming** means processing speech as it arrives. A **generator** is a tool that creates synthetic speech. A **codec** compresses audio for transmission.

**Earlier proposed contribution, now withdrawn as a novelty claim:** Train a small waiting policy using past scores and elapsed time. ALERT already learns a wait-or-decide rule using confidence, class information and time. EARLIEST also learns when to stop. These are necessary comparisons, not ideas we can claim as new.

**Hypothesis:** This policy can warn sooner at comparable error rates and decision coverage, meaning the share of recordings it actually decides.

**Alternative explanation:** A simple confidence threshold or fixed waiting time works just as well. Any apparent gain might come from leaving more difficult recordings undecided.

**Novelty check result:** The general detection problem is supported, but X33 is not yet a verified new research gap. Short-input detection, small models, limited-language adaptation and learned stopping already exist. Using Sinhala or combining those features is insufficient on its own.

What remains unknown is whether those methods make a particular early-decision mistake on Sinhala after fair source and recording-quality controls. That failure must first be measured. A targeted change that addresses it could become a contribution; no such change has been verified here.

A carefully documented Sinhala dataset and comparison could still be useful. Generating the dataset alone does not establish model novelty, and its originality and assessment value need separate review.

This is different from [X32](x32-sinhala-partial-audio-deepfakes.md), which asks where words were replaced inside a recording.

## 3. Evidence from closest work

| Study | What already exists | Implication for this project |
|---|---|---|
| [Sinhala AI-generated voice framework, ICAC 2025](https://doi.org/10.1109/ICAC69156.2025.11361479) · [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/icac69156.2025.11361479) | Separate Sinhala, Tamil and English human/synthetic classifiers using CNN–LSTM models. | A generic Sinhala detector already has direct precedent. The supplied full paper does not report a learned streaming waiting policy. Sections III–V read. |
| [Are audio DeepFake detection models polyglots?](https://www.isca-archive.org/spsc_2025/marek25_spsc.pdf) · [Cite](https://literature.researchfasttrack.com/cite?id=10.21437/spsc.2025-8) | Adapts detectors using limited target-language data. Sinhala is not tested. | Small-data language adaptation is an established comparison, not the novelty. Full paper inspected. |
| [Detection at the First Greeting, ICASSP 2026](https://arxiv.org/html/2601.19573v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/icassp55912.2026.11463587) | Lightweight detection from 0.5–2-second clips under communication degradation. | Short input and low model cost are already studied. Fixed clips do not settle how to decide repeatedly as speech arrives. Methods inspected. |
| [How Fast, How Sure, and Where It Breaks, 2026 preprint](https://doi.org/10.21203/rs.3.rs-10257178/v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.21203/rs.3.rs-10257178/v1) | Uses a frozen detector, growing audio prefixes, confidence adjustment and early decisions under telephone codecs. Confidence transfer can fail across channels. | The closest overlap. Our learned waiting policy must add value beyond its confidence-threshold rule. Full manuscript sections 3–5 read through a ResearchGate copy; direct publisher access failed. Results were not reproduced. |
| [RTCFake, ACL Findings 2026](https://arxiv.org/html/2604.23742v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.18653/v1/2026.findings-acl.285) | Studies speech detection after communication-platform processing and proposes training for better platform transfer. | Channel robustness also has direct prior work. Selected full-text methods and results inspected. |
| [ALERT, 2025 preprint](https://arxiv.org/html/2502.06584v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.48550/arxiv.2502.06584) | Learns when to wait or decide using classifier confidence, predicted class and time. Compares learned rules with hand-written rules. | Closely matches the proposed waiting layer, although tested on general time series rather than Sinhala deepfakes. Full-text sections 5.2–5.4 and 6 inspected. |
| [RawSpectrogram, IEEE Access 2023](https://doi.org/10.1109/ACCESS.2023.3321919) · [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/access.2023.3321919) | Makes speech anti-spoofing models work with incoming chunks while reducing repeated computation. | Efficient streaming speech detection is established. The full manuscript's model and evaluation sections were inspected through a ResearchGate copy. This does not establish phone performance or Sinhala transfer. |
| [RealComm, October 2026 preprint](https://arxiv.org/pdf/2610.27459) · [Cite](https://literature.researchfasttrack.com/cite?id=10.48550/arxiv.2610.27459) | Shows large detection errors after real call transmission and tests adaptation. In its comparison, Teffic-Audio call EER falls from 37.94% to 22.37% with combined training changes; lower is better. | Supports a real channel-related problem, not a new Sinhala gap. English/Mandarin, same seven generators across splits, and whole-recording evaluation. Full PDF methods, results and scope inspected; results not reproduced. |

[EARLIEST, KDD 2019](https://web.cs.wpi.edu/~xkong/publications/papers/kdd19.pdf), already jointly learns classification and stopping through a small controller. Its author PDF, sections 3.3.2–3.3.4, and implementation were inspected. It is general early classification, not a Sinhala deepfake study. [Cite](https://literature.researchfasttrack.com/cite?id=10.1145/3292500.3330974)

**Finding:** Real audio degradation is documented. The exact Sinhala early-decision failure has not been demonstrated. A new waiting algorithm is not established by the current plan.

**Search scope:** Seven additional scholarly searches returned 130 result occurrences; three duplication searches followed general stopping methods, streaming deepfakes and Sinhala detection. Some results were unrelated. Earlier references were followed back to 2018–2019. No absent search hit was treated as proof of novelty. Preprints and unreplicated results are labelled above; further few-shot and changing-data comparisons are retained in metadata.

## 4. Proposed approach

1. Reproduce an existing detector, the published streaming threshold rule and a learned stopping baseline such as ALERT or EARLIEST.
2. Feed the model only the audio available at each moment. It must never hear later speech before making an earlier decision.
3. Measure their errors on a source-safe Sinhala test set, including unfamiliar generators and separate compression changes.
4. Identify a specific failure before proposing an additional training change. Applying an existing waiting policy is a comparison, not the new method.
5. Train a smaller detector and check whether early decisions survive the size reduction; this also needs comparison with existing compression methods.

**Prototype:** Replay existing audio in small chunks and display “possible synthetic speech,” “human speech so far” or “not enough evidence.” An early human decision cannot certify the rest of a conversation.

Begin with controlled single-speaker recordings that are wholly human or wholly generated. Mixed human/AI recordings and live calls need additional data and separate evaluation.

## 5. Data and resources

| Source | What is available or documented | Limitation |
|---|---|---|
| [OpenSLR SLR52](https://openslr.org/52/) | About 185,000 Sinhala utterances, speaker/text metadata and public audio downloads; CC BY-SA 4.0. | Human speech only. It does not supply generated examples or actual telephone conversations. |
| Sinhala ICAC dataset, above | Paper describes 4,000 human and 4,000 generated Sinhala samples. | No public release or reuse licence was verified. Speaker and generator records also need checking. |
| [ASVspoof 2019](https://datashare.ed.ac.uk/handle/10283/3336) | English benchmark used by the closest streaming study and [AASIST author implementation](https://github.com/clovaai/aasist). AASIST provides code and pretrained models. | Proposed baseline/fallback only. The dataset page timed out in this check; verify download, licence and source records before use. English results cannot establish Sinhala performance. |
| [RTCFake challenge release](https://huggingface.co/datasets/JunXueTech/RTCFake) | English/Chinese, approximately 400 hours; CC BY-NC 4.0. Access requires team registration and some evaluation data are withheld. | No Sinhala. Access was not requested; it is an optional later test, not a secured dependency. |

**Dataset route to verify:** A ready-made Sinhala real/fake dataset is optional. We can use existing reusable human speech and create synthetic examples with several permitted generation tools. The exact tools, Sinhala output quality, reuse terms and source/speaker records are not yet verified. Split speakers and source recordings before generation, retain all derived versions in the same split, and keep a generator family for testing. New recordings are not assumed. Completing this route would resolve a data concern; it would not by itself establish the research gap.

**Estimated resources:** A selected 5–10-hour dataset, 16–32 GB RAM and roughly 30–100 GB working storage for audio, models and experiments. A modest GPU should be sufficient for small-model experiments; a larger teacher is optional. These are planning estimates, not measurements.

Use an ordinary phone for measured inference tests after a baseline works. Do not assume an installed app can capture both sides of a call: [Android documents privileged access requirements](https://developer.android.com/media/platform/sharing-audio-input). Replaying existing files avoids making live call capture a project dependency.

## 6. Three-member contributions

### Member A: learn from little Sinhala data

**Question and expectation:** Does a small amount of Sinhala training improve detection on a generator excluded from training?

Train a small adaptation layer at several fixed data budgets. Compare no adaptation and ordinary fine-tuning. Remove the extra training objective to check its effect.

**Separate result:** Detection errors versus labelled minutes and distinct speakers.

### Member B: decide or wait

**Question and expectation:** Can a learned waiting policy reduce delay while keeping errors and the share of decided recordings comparable?

First compare ALERT or EARLIEST with fixed-duration decisions and the published streaming threshold rule. Any extra policy change must address a measured failure beyond those methods. Remove score history to test whether it helps.

**Separate result:** The relationship between warning delay, errors and undecided recordings. This is the central comparison; learning when to wait is already established.

### Member C: preserve early decisions in a small model

**Question and expectation:** Can a small model learn from a larger model without losing the evidence needed for early decisions?

Compare training from the larger model's early-prefix outputs with ordinary training and learning only from its final answer. Then test lower-precision model storage.

**Separate result:** Detection quality versus model size, measured memory and speed on a named device.

All members use the same shared data and unchanged starting model. Each can obtain findings even if another member's proposed method fails. Data access is their shared prerequisite. Building the interface is supporting work; papers are optional.

## 7. Evaluation

- **Primary measure:** Mean time to a correct synthetic-speech warning, compared at matched fake-detection rates and decision coverage. Show delay only alongside the missed and undecided cases below. Choose thresholds on validation data with a target of at most 1% of genuine clips receiving any false alert; this is a planning target, not an achieved guarantee. Report the actual false-alert rate on every test condition.
- **Count all outcomes:** Report missed fakes, wrong human decisions, false alerts and undecided clips alongside delay. Show a curve across waiting times. Fast decisions on only easy examples do not establish an improvement.
- **Keep data separate:** Split by speaker and original recording before making compressed versions. Keep linked source/donor examples together. Hold out a generation-tool family and separately a codec setting. Use the same test recordings for every method.
- **Fair baselines:** Simple audio features with a classifier; AASIST or AASIST-L; a strong pretrained speech detector; ordinary Sinhala fine-tuning; fixed waiting times; the published streaming threshold rule; and ALERT or EARLIEST. Audit input padding because repeating short audio can change results.
- **Removal tests:** Remove adaptation, score history and early-prefix imitation separately. Keep training examples and tuning effort comparable.
- **Uncertainty and errors:** Use three training seeds and 95% confidence intervals grouped by speaker/source. Analyse short speech, unfamiliar generators, compression and noise. Overlapping checks are not independent recordings.
- **Full timing:** Count waiting for audio, feature extraction, prediction and policy processing. For example, 1 second of audio plus 50 ms of processing means at least 1.05 seconds to decide. Measure peak memory and whether repeated updates keep up on the phone.
- **Useful negative findings:** A threshold may be enough; language adaptation may stop helping on new generators; compression may make early decisions unreliable; a smaller model may need more speech.
- **Claim limits:** Short recorded clips cannot establish false alarms per real call or protection throughout a conversation. Those claims need existing representative long-call data and repeated-decision tests. This study does not determine malicious intent.

## 8. Score and next decision

**Verdict: adjust before proceeding; redesign before selection. Provisional score: 62.0/100; not qualified.** The deeper check confirms a real general problem, but withdraws the generic learned-waiting idea as the novelty claim. The score remains low; five gates remain Unknown. X32 is a separate candidate.

### Weighted rubric

The nine existing weights total 98 and are normalised to 100. Ratings describe the current plan, not achieved performance.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | High confidence in overlap: ALERT and EARLIEST already learn stopping; a distinct Sinhala contribution is unverified. |
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
| 1. Specific real problem | Pass | RealComm and the streaming studies document channel-related detection failures; Sinhala-specific early-decision failure remains unmeasured. |
| 2. ML essential | Pass | The question concerns a learned detector and when it has enough evidence to decide. |
| 3. Train/adapt models | Pass | All three contributions train or adapt models rather than only call an API. |
| 4. Existing data accessible | Unknown | No suitable reusable Sinhala real/fake dataset with speaker and generator records has been secured. |
| 5. No unavailable human evaluation | Pass | The bounded study uses existing labels. New callers, recordings and expert labelling are excluded. |
| 6. Precise research gap | Unknown | Learned stopping already exists in ALERT and EARLIEST. No specific Sinhala baseline failure or distinct repair has been demonstrated. |
| 7. Beyond application assembly | Pass | Training and comparison experiments are central; the app only demonstrates the result. |
| 8. Objective evaluation | Unknown | Metrics are defined, but suitable Sinhala data, source groups and clip lengths are not verified. |
| 9. 6–8 month feasibility | Unknown | Data access and baseline reproduction must be resolved before the schedule is credible. |
| 10. Three connected contributions | Pass | Section 6 gives separate questions, methods, comparisons and results for one shared problem. |
| 11. No specialised/continuous high-end compute | Pass | The core uses selected audio and compact models; large-model training is optional. |
| 12. Manageable data reuse | Unknown | Rights for the actual Sinhala fake audio and any generated derivatives remain unresolved. |
| 13. Useful negative findings | Pass | Standard methods may suffice; waiting may not help; compression may damage early detection. |

**Next decision:** Review this overlap audit with the supervisor to decide whether a Sinhala dataset-and-comparison study is assessable or a more specific model contribution is needed. Do not present the current waiting-policy idea as verified novelty.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Searches and source checks](../../metadata/source-checks/sinhala-streaming-gap-validation.json)

[Import these 9 papers into Zotero or EndNote](https://literature.researchfasttrack.com/zotero?ids=10.1109/icac69156.2025.11361479,10.21437/spsc.2025-8,10.1109/icassp55912.2026.11463587,10.21203/rs.3.rs-10257178/v1,10.18653/v1/2026.findings-acl.285,10.48550/arxiv.2502.06584,10.1109/access.2023.3321919,10.48550/arxiv.2610.27459,10.1145/3292500.3330974).

