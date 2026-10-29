[← Research candidates](../research-candidates.md)

# Finding AI-edited words in otherwise genuine Sinhala speech

**ID:** X32 · **Area:** Audio ML — partial deepfake detection · **Status:** Provisional opportunity; not qualified  
**Checked:** 29 October 2026 · **Provisional score:** 62.0/100 · **No model has been trained or timed.**

**Quick explanation:** Most of a voice recording may be genuine while a few words are replaced using AI. This project would try to find those replacements and mark their time ranges. The broad idea already exists; the narrower Sinhala question still needs suitable data and a defensible contribution.

## 1. Problem

Imagine a genuine recording saying, “Transfer five thousand rupees.” Someone replaces “five” with an AI-generated “fifty” in a similar voice. This is an illustrative example, not a documented incident.

A single “real/fake” label does not tell the listener where the replacement occurred. We want an output such as **“possible generated speech from 2.1 to 2.6 seconds.”** Those example times are illustrative.

Published work shows that short replacements, unfamiliar generation tools and changed recording conditions can challenge detectors. Sinhala performance has not been demonstrated by the studies checked here. A useful result would help researchers understand these failures; it would not establish that an app can prevent fraud.

## 2. Research gap and question

### What we would investigate

**Question:** With a small amount of labelled Sinhala data, can a compact model find short AI-replaced segments after audio compression, including replacements made by a tool excluded from training, while keeping false alarms on human speech and human-only edits low?

**Working hypothesis:** Training on labelled partial edits and compressed examples will help more than training only on completely generated recordings.

**Other possible explanations:** The model may simply learn the generation tool, speaker, recording quality or cut-and-paste seam. Standard fine-tuning may perform just as well as a more complicated method.

### Is this actually a new gap?

**The failure is supported; the proposed research contribution is not yet verified.** Multilingual partial-edit detection, unfamiliar generators, ordinary editing controls and limited-language adaptation already have close precedents. “It is Sinhala” is not enough to establish novelty.

The next literature comparison must identify something specific beyond these studies, such as an experimentally demonstrated failure that a particular training change addresses. If standard methods already handle it, narrow or replace the topic.

Using a little target-language data is also an established approach: [Are audio DeepFake detection models polyglots?](https://www.isca-archive.org/spsc_2025/marek25_spsc.pdf) tests it for whole-recording detection. It does not test Sinhala or locate partial edits. [Cite](https://literature.researchfasttrack.com/cite?id=10.21437/spsc.2025-8)

### Why this option rather than identifying a cloned caller?

[The SASV challenge](https://arxiv.org/abs/2203.14732) already combines speaker verification with spoof detection. [Cite](https://literature.researchfasttrack.com/cite?id=10.48550/arxiv.2203.14732) That option needs trusted recordings of the claimed person and labelled impersonations. We have not verified suitable Sinhala data for it, so it is parked as an alternative rather than added as a second project.

This brief studies **where generated replacements occur**. It does not identify a caller, prove a statement false, detect every kind of audio editing, or infer malicious intent. Authorised synthetic edits are also positive examples for this technical task.

## 3. Evidence from closest work

| Study | What was already done | What this means for us |
|---|---|---|
| [A General Classification Framework for Detecting AI-Generated Voices (ICAC 2025)](https://doi.org/10.1109/ICAC69156.2025.11361479) · [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/icac69156.2025.11361479) | Separate Sinhala, Tamil and English CNN–LSTM models classify recordings as human or synthetic. The Sinhala real speech came from eight speakers; synthetic data used Google Translate and Resemble AI. | Direct Sinhala precedent. It does not report edit-location evaluation, unseen-generator testing or a speaker-separated split. Its reported Sinhala accuracy of 97.88% does not answer our question. Supplied full paper read, especially sections III–V. |
| [Robust Localization of Partially Fake Speech (APSIPA 2025)](https://arxiv.org/html/2507.03468v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/apsipaasc65261.2025.11249067) | Evaluates a detector across PartialSpoof, LlamaPartialSpoof and Half-Truth. Strong performance on the familiar dataset does not carry over reliably. Tests thresholds and additional training data. | Testing unfamiliar datasets and reporting false alarms are established practices, not our novelty. Full-text methods and results inspected. |
| [SPADE (September 2026 preprint)](https://arxiv.org/html/2609.25197v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.48550/arxiv.2609.25197) | Partial edits across 12 languages and up to five generators. Tests unfamiliar languages, generators and acoustic conditions using BAM localisers. Sinhala is not among its listed languages. | The strongest overlap with the proposed generalisation question. Sinhala alone does not distinguish the method. Full-text data design and experiments inspected. |
| [MIST / Fine-Grained Speech Inpainting Forensics (May 2026 preprint)](https://arxiv.org/html/2605.02223v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.48550/arxiv.2605.02223) | Replaces one to three words in six languages and uses repeated window-based checks to locate them. Sinhala is not listed. | Finding short or multiple replacements with sliding windows is already addressed. Preprint methods inspected; the dataset card links a later IEEE version whose full methods were not checked. |
| [Temporal Anchors and Editing Sensitivity (October 2026 preprint)](https://arxiv.org/html/2610.04479v1) · [Cite](https://literature.researchfasttrack.com/cite?id=10.48550/arxiv.2610.04479) | Compares genuine-only edits with generated insertions. Reducing editing false alarms can come with missed synthetic content; results depend on test conditions and thresholds. | Simply adding “ignore ordinary edits” or a consistency loss is also insufficient novelty. Full-text protocol, findings and limits inspected; results do not establish Sinhala behaviour. |

A further close neighbour, [Boundary and Intra-Segment Learning (September 2026 preprint)](https://arxiv.org/html/2609.25822v1), already trains on both edit boundaries and the insides of speech segments. Its text promises code upon acceptance; availability was not verified. [Cite](https://literature.researchfasttrack.com/cite?id=10.48550/arxiv.2609.25822)

**Search limits:** Eight new scholarly searches and four duplication searches were run, followed by original papers and dataset pages. Some Sinhala-heavy searches returned unrelated work, so searches were repeated using “partial spoof” and “localisation.” No matching Sinhala partial-edit benchmark was verified. That is a search result, not proof that none exists. The earlier limited-language adaptation search is retained in metadata.

## 4. Proposed approach

1. Start with a pretrained speech model and train a small layer that scores short time intervals.
2. Compare no Sinhala adaptation with small, fixed Sinhala training budgets. Count both labelled minutes and distinct speakers.
3. Test whether learning from partial edits and matched compression helps on a generator excluded from training.
4. Include unedited human speech and human-only cut-and-paste edits. Check whether the detector is finding generated speech or merely spotting seams.
5. Compare a compact model with its larger starting model.

Use separate tests for language, generator and compression changes before combining them. Otherwise, a poor result would not reveal which change caused the failure.

**Prototype:** Upload an existing audio file and see suspected intervals on a timeline. Begin offline. Live call access, speaker authentication and fraud prevention are outside the core claim. Mobile testing is an extension only after the audio model works.

## 5. Data and resources

| Source | Checked availability | What it can support |
|---|---|---|
| [OpenSLR SLR52](https://openslr.org/52/) | About 185,000 Sinhala utterances, transcripts and speaker information; CC BY-SA 4.0. Public download route inspected. | Human read-speech source. It has no fake class or edit timestamps and does not represent phone conversations. |
| ICAC Sinhala data, above | Paper describes 4,000 human and 4,000 synthetic Sinhala samples. No public download, reuse licence or source-level split was verified. | A lead, not an available benchmark. Whole-recording labels would still be insufficient for location accuracy. |
| [PartialSpoof v1.2](https://zenodo.org/records/5766198) | Public English benchmark, approximately 10 GB compressed; training/development/test files and interval labels listed. Downloadable README inspected. It states CC BY 4.0 and identifies the underlying ASVspoof data's ODC-By terms. | First baseline and fallback method study. It cannot establish Sinhala results. [Foundational paper](https://arxiv.org/abs/2204.05177) · [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/taslp.2022.3233236). |
| [SPADE release](https://huggingface.co/datasets/rogertseng/spade) | Requires accepting access conditions; 211 GB shown. Original and edited files link by ID and have interval labels. English, Japanese and Korean subsets are pending release on the inspected card. Exact reuse terms were not verified. | Possible selected multilingual data after access and licence checks. Access was not requested or accepted. |
| [MIST release](https://huggingface.co/datasets/tung2308/MIST_SpeechInpaintingDataset) | Card says sample subset only; 71.5 GB shown. Raw README says research-only; linked licence could not be read. Viewer reports a loading error. | An additional lead, not a verified ready-to-use fallback. Published dataset totals must not be confused with released files. |

**Main blocker:** No existing Sinhala dataset with reusable generated replacements, exact edit times and enough independent speakers/generators was secured. We did not download or listen to audio samples.

Creating controlled derivatives from existing licensed audio might be an option, but permitted generators, reuse terms, automatic labels and module approval must first be established. This does not authorise new recordings or assume that YouTube audio is reusable. If those prerequisites cannot be met, stop the Sinhala claim.

**Baseline routes:** [PartialSpoof's author implementation](https://github.com/nii-yamagishilab/PartialSpoof) provides model and checkpoint download instructions. [BAM's author repository](https://github.com/media-sec-lab/BAM) provides training instructions and a checkpoint link. These routes were inspected, not executed or downloaded. BAM also builds preprocessing files from labels: audit its inference path to ensure evaluation labels cannot influence predictions.

**Planning estimates, not measurements:** Start with 5–10 hours of selected audio, frozen features and small heads; allow 16–32 GB RAM and roughly 30–100 GB working storage including models and caches. A modest GPU may be needed to extract features. Larger-model fine-tuning could need 8–16 GB VRAM or more depending on batch and duration; it is not a core dependency. Cache selected layers rather than every encoder layer. No training-time, phone-memory or battery claim is established.

## 6. Three-member contributions

**Shared problem:** Find short generated replacements without raising too many false alarms.

### Member A: learn from little Sinhala data

**Question:** How much Sinhala data helps on an unfamiliar generator? The expectation is that training on partial edits will help more than training only on whole-recording labels.

Train small detection heads at fixed label budgets. Compare no adaptation and ordinary fine-tuning, then remove interval labels while keeping audio exposure fixed. **Separate result:** performance versus labelled minutes and speakers, including cases where more data does not help.

### Member B: avoid editing shortcuts

**Question:** Can training reduce false alarms on human-only edits without hiding short generated inserts? The expectation is that paired examples can improve this balance, but the October 2026 study shows that this is not guaranteed.

Train with matched human-only and human-plus-generated edits. Compare standard augmentation, then remove paired examples and the extra learning objective separately. **Separate result:** how often each change reduces false alarms at the cost of missed edits. Explicitly compare the October study.

### Member C: keep the model small

**Question:** How much can model size fall before short-edit detection becomes unreliable? The expectation is that learning from a larger model helps a small model retain more accuracy than ordinary training.

Train a smaller model to imitate a fixed larger model, then test quantisation, which stores model numbers at lower precision. Compare the unchanged larger model and the same small model trained normally. Remove imitation training to measure its contribution. **Separate result:** detection quality versus measured size, memory and processing time. Report phone results only if measured on a named device.

Each member can use the same unchanged starting model and fixed dataset. A's method does not need to succeed before B or C can obtain results. The dataset is a shared prerequisite; a missing dataset blocks all three. Backend and frontend work are supporting tasks. Papers are optional.

## 7. Evaluation

- **Primary measure:** Segment F1 at temporal overlap of at least 0.5: a prediction counts as correct when it overlaps the labelled edited interval sufficiently. Match predictions to reference intervals one-to-one; extra predictions count as false alarms. Choose the decision threshold using validation data, aiming for no more than 1% of genuine speech time flagged there. Report the actual false-alarm rate on each test set.
- **Additional measures:** Percentage of generated speech found, genuine speech time incorrectly flagged, missed short edits, and start/end timing error with unmatched edits reported separately. Do not claim timing precision finer than the labels support.
- **Split:** Separate speakers and original source recordings before making any derivatives. Keep every source, donor, prompt and edited/compressed version in the same split; inspect donor-sharing links. Hold out a generator family and separately a compression setting. If source records cannot support this, do not claim generalisation.
- **Baselines:** A simple MFCC-based window classifier; frozen pretrained speech features with a small classifier; a public strong localiser such as BAM; and ordinary Sinhala fine-tuning. Use sliding-window output where necessary. Document deviations from author implementations.
- **Removal tests, also called ablations:** Remove partial-edit supervision, paired human-only edits, compression training and small-model imitation separately. Give compared models the same training examples and tuning budget where possible.
- **Uncertainty:** Repeat learned models with three random seeds and report 95% confidence intervals by resampling independent speakers/source groups. Do not treat thousands of overlapping windows as independent samples.
- **Error analysis:** Break results down by edit length, fraction of audio replaced, generator, speaker, compression and human-only editing. Keep genuine speech and ordinary edits as separate negative groups.
- **Efficiency:** Measure complete feature extraction plus prediction. Report model size, peak memory and processing time per second of input. Any streaming extension must count waiting for audio and future context, not just the final prediction operation.
- **Useful findings without winning:** Standard fine-tuning may be sufficient; compressed audio may erase useful cues; smaller models may miss the shortest edits; apparent gains may disappear after removing speaker or seam shortcuts.
- **Claim boundary:** Controlled file tests support claims about those files and conditions. They do not demonstrate live-call protection, all Sinhala accents, reliable speaker identity or whether an edit is deceptive.

## 8. Score and next decision

**Verdict: adjust before proceeding. Provisional score: 62.0/100; not qualified.** This compares the current proposal with other candidates, not achieved model performance. Five mandatory gates remain Unknown. It is below the shortlist threshold and novelty/data minimum ratings.

### Weighted rubric

The existing nine weights total 98 and are normalised to 100.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | Low: Similar questions are already studied; a distinct Sinhala contribution is not established. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: No reusable Sinhala set with labelled AI-edited segments was verified. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Low-medium: A small study could fit, but the data and first baseline must be secured early. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: The plan trains detection heads, tests learning objectives and studies model compression. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: The test plan is clear, but Sinhala labels and source-safe splits are missing. |
| Three-member structure | 12 | 4 | 9.6 | Medium: Each member has a separate experiment using the same unchanged starting model. |
| Real-world significance | 9 | 4 | 7.2 | Medium: A short altered phrase can matter; benefits on real calls remain untested. |
| Compute/storage | 5 | 4 | 4.0 | Medium-low: Selected data and frozen features should fit; training and phone costs are estimates. |
| Prototype | 3 | 4 | 2.4 | Medium: A file-based viewer can highlight suspected edits without live call access. |
| **Normalised total / 100** | **98** | | **62.0** | **Not qualified.** |

### Mandatory gates

Pass means the bounded plan meets the requirement in principle. Unknown means the evidence is insufficient; it is not approval to proceed.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Partial-edit studies show that whole-recording labels can hide short generated replacements; see sections 1 and 3. |
| 2. ML essential | Pass | The shared question tests learned detection of short speech segments. |
| 3. Train/adapt models | Pass | Members train small detection heads, learning objectives or a compressed model; no paid API is required. |
| 4. Existing data accessible | Unknown | SLR52 supplies human speech, not labelled partial deepfakes. No suitable existing Sinhala edited-speech release was verified. |
| 5. No unavailable human evaluation | Pass | The bounded study uses existing labels and permitted controlled derivatives. It stops if new recordings or expert labels become necessary. |
| 6. Precise research gap | Unknown | Multilingual transfer, unseen generators, editing controls and compression have close prior work; the added contribution needs validation. |
| 7. Beyond application assembly | Pass | Sections 4 and 6 specify learning and error-trade-off experiments; the viewer is only a demonstration. |
| 8. Objective evaluation | Unknown | Metrics can be defined, but Sinhala edit timestamps and speaker/source/generator records are not secured. |
| 9. 6–8 month feasibility | Unknown | Completion depends on early access to suitable data and a working baseline. |
| 10. Three connected contributions | Pass | Each member has a question, trained method, comparison, ablation and separate result using the same starting model. |
| 11. No specialised/continuous high-end compute | Pass | The core plan uses selected data, frozen features and small heads; full large-model training is optional. |
| 12. Manageable data reuse | Unknown | Reuse terms for the actual Sinhala fake data and any generated derivatives remain unresolved. |
| 13. Useful negative findings | Pass | Failure to transfer, editing false alarms and the accuracy-versus-size trade-off remain useful results. |

**Next decision:** Take this brief to the supervisor to confirm whether the proposed added contribution and a permitted existing-data route are acceptable. Do not commit to the Sinhala topic until the data, labels and reuse terms are verified. The English fallback would need its own narrowed question and reassessment.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Searches, source checks and parked formulations](../../metadata/source-checks/sinhala-partial-gap-validation.json)

[Import these 9 papers into Zotero or EndNote](https://literature.researchfasttrack.com/zotero?ids=10.1109/icac69156.2025.11361479,10.1109/apsipaasc65261.2025.11249067,10.48550/arxiv.2609.25197,10.48550/arxiv.2605.02223,10.48550/arxiv.2610.04479,10.48550/arxiv.2609.25822,10.1109/taslp.2022.3233236,10.48550/arxiv.2203.14732,10.21437/spsc.2025-8).

