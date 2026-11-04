# Small-boat detection for maritime security: literature review and candidate systematic-review gap

**Date:** 2 November 2026. **Requested track:** systematic literature review. **Status:** preliminary, source-linked literature synthesis and review proposal; not a completed systematic review or a certification of novelty.

## Recommendation

This is a viable research area, but “detecting illegal small boats using AI” is too broad and conflates two tasks. Detecting a vessel establishes its presence; classifying an activity as unlawful requires additional contextual and independently verified evidence. A vessel missing from AIS is not, on that basis, an illegal vessel.

The strongest candidate for your **systematic review** is:

> **Reliability of satellite-based small-boat detection in coastal waters: a systematic review of independent validation, size-specific detection performance, and false alarms.**

The proposed contribution is an evidence audit of what operational claims the published evaluations support. It is not another catalogue of YOLO variants or sensors. This recommendation is an inference from the sources below. The underlying limitations are already recognised; whether a sufficiently distinct review remains to be done requires a full comparison with the nearest reviews and their supplements.

## 1. What was searched and what was actually reviewed

The live **FastTrack Literature connector** was accessed through its locally configured MCP endpoint. Ten discovery searches, five duplication tests in systematic-review mode, two saturation checks, and twenty individual-paper retrievals were completed. Raw responses and exact queries are saved in [the search directory](../metadata/maritime-review-2026-11-02/). Primary publisher, proceedings, institutional, and author-hosted pages were checked where accessible.

Searches covered small-boat detection, maritime radar sea clutter, optical/infrared detection, satellite SAR, AIS anomaly detection, existing systematic reviews, and validation. Long, multi-concept queries sometimes returned irrelevant medical-vessel and cybersecurity papers. Shorter queries were therefore added. This retrieval weakness matters: an empty `existing_reviews` field did not establish originality, and known relevant reviews were retained regardless of that field.

The discovery searches returned **200 result occurrences**. This is a retrieval count, not 200 eligible studies. The twenty selected records include reviews, original studies, a dataset/benchmark paper, a demonstration paper, and adjacent context. No exhaustive database export, independent dual screening, complete full-text extraction, PRISMA flow, or meta-analysis was performed. Publication-year metadata alone cannot exclude every record dated later within 2026; exact dates must be checked during formal screening.

Full-text sections were inspected for selected sources, including the Nature study's limitations and the recent ocean-aware review. Other assessments rely on original abstracts or indexed publisher passages; the tables identify those limits. A statement that something was not reported in an abstract is not evidence that the authors did not do it.

The saturation instruments estimated 57 records for “small vessel detection maritime surveillance” and 21 for “small boat detection validation”. These are query-dependent estimates, not eligible-study counts or evidence that a gap exists. The individual studies establish a plausible evidence base, but the number meeting the proposed coastal, size-specific, independent-validation criteria remains unknown.

## 2. Separate the research tasks

| Task | What the output establishes | What it does not establish |
|---|---|---|
| Boat detection | An image/signal contains a vessel-like target at a location | Identity, authorisation, intent, or unlawful activity |
| Tracking and association | Observations likely correspond to the same vessel or AIS identity | That an unmatched vessel deliberately stopped transmitting |
| Behaviour analysis | A trajectory or activity differs from an expected pattern | That the deviation is unlawful rather than benign |
| Violation assessment | A defined activity conflicts with applicable rules, supported by appropriate evidence | Something that can be inferred solely from a bounding box |

[P16](https://doi.org/10.3390/s24175623) explicitly combines behaviour models and expert rules, using real and synthetic AIS-derived data. Its evaluation is not a validation of detecting arbitrary non-AIS small boats from images. [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/s24175623)

The same small-boat detection evidence can serve maritime security, fisheries monitoring, environmental management, and search and rescue. The InflateSAR and Argo papers have humanitarian purposes; they provide sensing evidence and do not label the people or boats being detected as illegal.

## 3. Existing reviews: the duplication test

| Record and document type | What it already covers | Consequence for your review |
|---|---|---|
| **P01, Zucchetta et al., 2025**, [Satellite-Based Monitoring of Small Boat for Environmental Studies](https://doi.org/10.3390/jmse13030390), systematic review. [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/jmse13030390) | 133 studies from 1992–2024; satellite sensors, methods, small boats, applications, and validation. Search/screening method and selected results inspected through publisher text. | A generic satellite-small-boat review would overlap directly. The proposed review must add detailed assessment of reference-standard independence and operational error denominators. |
| **P07, Alexandre et al., 2024**, [Ship Detection With SAR C-Band Satellite Images](https://doi.org/10.1109/jstars.2024.3437187), systematic review. [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/jstars.2024.3437187) | Reviews 2015–2022 methods and explicitly distinguishes physical vessel size from pixel-based size. Original abstract retrieved; full methods not inspected. | The metres-versus-pixels observation is already published. A new review must quantify its consequences and extend the evidence assessment, not claim to discover it. |
| **P08, He et al., 2026**, [Satellite Remote Sensing for Fishing Vessel Identification and Monitoring](https://doi.org/10.3390/rs18173000), systematic review. [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/rs18173000) | PRISMA-described search of modalities and datasets; qualitative comparison of detection sensitivity, robustness, resolution, and continuity. Original abstract and indexed comparison-method passages inspected. | A sensor comparison or fishing-dataset catalogue is already occupied. Any additional contribution needs study-level validation extraction. |
| **P02, Rekavandi et al., 2025**, [Guide to Image- and Video-Based Small Object Detection](https://doi.org/10.1109/tits.2025.3530678), survey. [Cite](https://literature.researchfasttrack.com/cite?id=10.1109/tits.2025.3530678) | Methods, datasets, metrics, and maritime applications; abstract describes over 160 papers from 2017–2022. Published abstract and 2022 author-preprint abstract inspected. | A generic small-object architecture taxonomy adds little. Systematic screening status was not established from the material read. |
| **P03, Alsaaq, 2026**, [Ocean-aware deep learning](https://doi.org/10.3389/fmars.2026.1929278), comprehensive review. [Cite](https://literature.researchfasttrack.com/cite?id=10.3389/fmars.2026.1929278) | Environmental conditions, sensor fusion, detection/tracking, false alarms, sea-state evaluation, and operational validation. Relevant full-text sections inspected. | “Evaluate weather/domain shift” is already a stated research direction. No reproducible systematic-search method was established in the inspected sections. |
| **P04, Bal Şahin et al., 2026**, [Multi-sensor data fusion in maritime surveillance](https://doi.org/10.7717/peerj-cs.3765), structured review. [Cite](https://literature.researchfasttrack.com/cite?id=10.7717/peerj-cs.3765) | Sensor-fusion methods and applications spanning detection, tracking and anomalies. Original abstract retrieved; publisher full text inaccessible. | “Combine radar, cameras and AIS” is not a new review topic by itself. Detailed duplication remains to be assessed from full text. |
| **P05, Ryu and Han, 2025**, [Environment-Aware Multi-Sensor Fusion](https://doi.org/10.7780/kjrs.2025.41.6.21), comprehensive review. [Cite](https://literature.researchfasttrack.com/cite?id=10.7780/kjrs.2025.41.6.21) | Environmental effects on sensor confidence and maritime fusion. Original abstract retrieved; full screening method unverified. | Environment-aware fusion is already discussed; the candidate contribution must be a specific evidence synthesis. |

**Duplication verdict:** narrow and update, with substantial overlap to resolve. None of the search outputs establishes that the proposed synthesis is the first of its kind.

## 4. Primary evidence and its limitations

| Study | What the evidence contributes | Boundary of the result / reading limit |
|---|---|---|
| **P09, Lanz et al., 2021**, [InflateSAR detector testing](https://doi.org/10.3390/rs13081487). [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/rs13081487) | Real SAR observations of an inflatable, comparison of detectors using ROC curves and different sensor settings. | Lake test conditions differ from open/coastal sea deployment. Original abstract and indexed experimental-setting passages inspected. |
| **P10, Lanz et al., 2023**, [InflateSAR polarimetric detection](https://doi.org/10.3390/rs15082008). [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/rs15082008) | A 12 m inflatable; detector combinations and environmental/sensor conditions. | Includes ocean-clutter emulation using separately collected sea imagery, not simply a boat trial in every real sea state. Abstract and indexed methods inspected. Group related campaign papers before counting independent evidence. |
| **P11, Moser et al., 2022**, [Argo](https://doi.org/10.24963/ijcai.2022/728), IJCAI demonstration paper. [Cite](https://literature.researchfasttrack.com/cite?id=10.24963/ijcai.2022/728) | Small-vessel classification dataset; reports 91% classification recall. | Classification recall is not full-scene detection recall or false alarms per monitored area. Proceedings abstract inspected; full paper retrieval failed. |
| **P12, Paolo et al., 2022**, [xView3-SAR](https://doi.org/10.52202/068431-2726), dataset/benchmark. [Cite](https://literature.researchfasttrack.com/cite?id=10.52202/068431-2726) | Nearly 1,000 SAR scenes with automated/manual annotations and wind/bathymetry information. | Labels and classes concern vessel detection/characterisation; “dark” does not supply verified illegality labels. Original abstracts inspected in this pass; label completeness needs full extraction. |
| **P13, Shin et al., 2024**, [Polarimetric Combination from Sentinel-1](https://doi.org/10.3390/rs16071198). [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/rs16071198) | Validation uses AIS and a small-fishing-vessel tracking system, V-Pass. Abstract reports 42.27% small-ship detection performance over the study's evaluation. | This is the study's tracking-match measure, not general accuracy. Its false-alarm ratio is based on unmatched detections; incomplete reference coverage can confound that interpretation. Original abstract and indexed metric definitions inspected. |
| **P14, Paolo et al., 2024**, [Satellite mapping reveals extensive industrial activity at sea](https://doi.org/10.1038/s41586-023-06825-8). [Cite](https://literature.researchfasttrack.com/cite?id=10.1038/s41586-023-06825-8) | Large-scale satellite/AIS analysis; explicit limitations state that recall drops rapidly for vessels 10–20 m long. | Strong evidence of a size-related limitation in this system, not a universal performance estimate for every sensor. Original full-text limitations inspected; industrial activity is not equivalent to unlawful activity. |
| **P06, Nasios and Vogklis, 2025**, [AI at Sea, Year Six / SatShipAI](https://doi.org/10.3390/electronics14183648). [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/electronics14183648) | Reports six years of operational monitoring and nearshore/infrastructure-related challenges. | Prevents claiming that operational validation does not exist. Classified here as an operational system evaluation from its abstract, despite the connector's “review” tag and title's “meta-analysis”. Full outcome audit not performed. |
| **P17, Hu et al., 2025**, [Cost-Sensitive Small Vessel Detection](https://doi.org/10.3390/rs17142471). [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/rs17142471) | Addresses foreground/background imbalance and small-object localisation through dataset and loss changes. | Cost sensitivity, small-target augmentation, and modified localisation objectives already have precedent. Abstract-level evidence only; physical size and external evaluation need extraction. |
| **P15, Chiappini et al., 2026**, [SAR/RGB small-scale fishing-vessel evaluation](https://doi.org/10.5194/isprs-archives-xlix-b1-2026-621-2026), proceedings study. [Cite](https://literature.researchfasttrack.com/cite?id=10.5194/isprs-archives-xlix-b1-2026-621-2026) | Adriatic coastal workflow with heterogeneous pretraining and local optical fine-tuning. Reports recall 0.846 and mAP50–95 0.306 for a selected model. | These are different metrics, not contradictory accuracies. Abstract alone cannot establish transfer to unseen coastlines or recall for a specific physical-length class. |
| **P18, Kanan et al., 2026**, [Boat Detection in the Venice Lagoon](https://doi.org/10.3390/rs18030421). [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/rs18030421) | Sentinel-2, thresholding and U-Net for traffic/recreation mapping; illustrates a difficult coastal environment. | Local activity mapping differs from detecting every small boat or validating unlawful activity. Original abstract and indexed methods inspected; full independent-reference audit pending. |
| **P19, Ruciński et al., 2023**, [Small Recreational Boat Detection](https://doi.org/10.3390/rs15071807). [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/rs15071807) | Boats under 10 m in lakes; 14 images and field comparison. Reports 88.17% detection accuracy in its setting. | A valuable counterexample to “small boats cannot be detected”, but lake results cannot be assumed to transfer to rough coastal water. Abstract-level extraction; denominator needs checking before any numerical comparison. |
| **P20, Corbane et al., 2008**, [SPOT-5 operational small-ship detection](https://doi.org/10.3390/s8052959). [Cite](https://literature.researchfasttrack.com/cite?id=10.3390/s8052959) | Early optical small-boat monitoring in a tropical setting; reports false-alarm difficulties with cloud and sea clutter. | Demonstrates the long history of the problem. Original abstract retrieved; retained as historical context rather than proof about current systems. |

**Do not rank these papers by their reported percentages.** Their targets, denominators, environments, sensors, reference standards, and tasks differ. Classification recall, track matching, pixel segmentation, object detection, and activity mapping answer different questions.

## 5. Evidence synthesis and the candidate gap

The sources support three conclusions. First, small-boat sensing is technically possible, with field studies and operational systems already published. Second, reliable performance is conditional on boat characteristics, sensor configuration, background and environmental conditions. Third, a detection benchmark cannot by itself establish reliable identification of unlawful activity.

The specific unresolved **evidence question** worth investigating is:

> **How well do satellite detection methods identify physically small boats in coastal waters when evaluated against reference observations that can include vessels absent from AIS, and how does the evidence vary with boat length, sea conditions, false-alarm definition, and external validation?**

This is not a claim that independent validation has never been performed. V-Pass validation, inflatable trials, field observations, and operational monitoring already exist. Nor is it a claim that every paper ignores size or environmental effects. The opportunity is to reconcile these heterogeneous evaluations and identify exactly which operational claims remain unsupported.

| Potential contribution | What would make it useful | What would make it duplicative or unsupported |
|---|---|---|
| Reference-standard audit | Distinguish AIS-only labels, other tracking systems, visual interpretation, co-temporal higher-resolution observations and controlled field trials; assess missing boats and matching errors. | Treating all “ground truth” as equally complete, or claiming AIS-free validation is new. |
| Physical-size synthesis | Extract hull length where measured, pixel extent separately, image resolution and sensor mode; report unknown size honestly. | Repeating the metres-versus-pixels criticism without new study-level extraction. |
| Operational error synthesis | Separate false alarms per area/time from unmatched-detection fractions, pixel false-positive rates and precision; retain original denominators. | Pooling incomparable metrics or treating all unmatched contacts as false alarms. |
| Transfer evidence | Distinguish random chip splits from held-out scenes, dates, sites and sensor configurations; map natural versus simulated adverse conditions. | Calling a random split “external validation”, or treating evaluation design alone as a new detection algorithm. |

**Gap confidence:** strong evidence that practical limitations remain; moderate support for a focused synthesis being useful; novelty of the exact review is **not yet established**. The closest systematic reviews and newer reviews must be compared at the extraction-table and supplement level before registration. A literature search cannot prove that a problem is globally unsolved.

## 6. Proposed systematic-review protocol

**Primary question:** Among physically small boats in coastal waters, what detection performance and false-alarm burden do satellite SAR and optical methods demonstrate under independent validation, and how do results vary by size and operating conditions?

PICO adapted to this engineering question:

- **Population:** Small surface boats in coastal/nearshore waters. Extract each author's physical-size definition; do not substitute pixel size for hull length. A prespecified working threshold such as under 25 m is a protocol choice, not a universal legal definition; retain author-defined groups and finer strata where available.
- **Intervention/index method:** Satellite SAR or optical detection, including traditional statistical, machine-learning and deep-learning methods.
- **Comparison:** Within-study baseline detectors and matched comparisons of validation settings. Absence of a baseline need not exclude a valid field evaluation.
- **Outcomes:** Object-level recall/sensitivity, precision and false alarms with explicit denominators; size-specific performance; external performance changes; usable coverage and processing latency when reported. Illegality classification is outside the primary outcome.

**Scope:** Satellite SAR and optical methods are the manageable primary scope. Shore radar, thermal coastal cameras, UAVs, acoustic sensing and AIS-only anomaly models form a separate surrounding literature; mixing all of them into one pooled performance estimate would be misleading. Lakes and controlled test sites should be retained as a clearly labelled transfer-evidence stratum, not quietly mixed with coastal deployments. Include direct hull detection; keep wake-only and night-light activity proxies separate if retained.

**Search:** An inception-to-2-November-2026 search is preferable to an arbitrary recent-year cutoff because older field campaigns surfaced. Use FastTrack for discovery, but supplement with reproducible IEEE Xplore and Scopus/Web of Science searches where institutional access permits, plus backward/forward citation searching. These additional database searches have not been executed here. Search public engineering review protocols, OSF and preprints for concurrent work; PROSPERO is generally not the appropriate primary registry for this non-health engineering question.

Illustrative database string, to adapt and test in each platform:

```text
(boat* OR vessel* OR ship* OR inflatable* OR "small craft")
AND (detect* OR surveillance OR monitoring)
AND (satellite OR "synthetic aperture radar" OR SAR OR "optical remote sensing")
```

Run supplementary searches with `small`, `coastal`, `nearshore`, `validation`, `ground truth`, `sea state`, and `false alarm`. Do not require all those terms in every search, because relevant evaluations may discuss them only in the methods. Do not require “illegal”; it would exclude relevant sensing studies without establishing unlawful-activity labels.

**Screening and extraction:** Deduplicate DOI/title variants and link reports from the same campaign/dataset. Use a second reviewer for independent eligibility decisions and verification of key extraction, with disagreements recorded. Retrieve full texts before inclusion. Classify empirical studies separately from reviews, preprints, demonstrations and technical reports. Record exact publication dates, corrections, missing reporting, full-text exclusions and reasons.

For every study extract: sensor/platform/band; resolution and pixel spacing; physical and pixel vessel sizes; boat material if known; scene count and unique vessel count; region/date/sea state; reference source and temporal alignment; reference completeness; train/test grouping; natural/simulated data; detector/comparator; matching rule; threshold selection; TP/FP/FN where available; false-alarm denominator; uncertainty intervals; runtime hardware; and source page/table for each claim.

**Appraisal:** Use explicit engineering domains rather than applying a clinical trial tool wholesale: target representativeness, label/reference completeness, temporal matching, train/test leakage, external validation, threshold selection on test data, metric denominator clarity, and reproducibility. Distinguish missing reporting from demonstrated methodological flaws. Do not collapse these domains into an arbitrary quality score.

**Synthesis:** Begin with a structured narrative synthesis and evidence map. Pool only outcomes with compatible tasks, length definitions, reference standards, matching rules and denominators. Keep SAR and optical strata separate unless a justified common estimand exists. Multiple images of the same boat or repeated dataset reuse do not create independent studies. A meta-analysis may be infeasible; do not promise one before extraction.

**Feasibility:** The pilot found enough relevant leads to justify protocol development, but not a verified minimum of independent, eligible coastal studies. The strict subset combining measured physical length, non-AIS-capable references, and external testing may be thin. Count it after screening, and prespecify whether a systematic evidence map is the fallback. Timeframe and library access remain unconfirmed; no radar, boat or GPU is required for a literature-only review.

## 7. Topic-validation decision

**Track:** Systematic review, as selected by the user.

**Phase:** Phase 2, preliminary duplication and feasibility testing. Detailed extraction and scope confirmation remain.

**Verdict:** Adjust before proceeding.

**What's working:** Direct small-boat field studies, operational evaluations and recent reviews provide a credible literature base. The practical performance limitations are documented rather than inferred solely from sparse search results.

**The issues that matter:** (1) Broad small-boat, SAR and sensor-fusion reviews already exist, so the added synthesis must be explicit. (2) Physical-size and independent-validation eligibility may reduce the usable corpus substantially. (3) Detecting a boat or an anomaly does not establish unlawful activity, so the review outcome must be defined precisely.

**Your next step:** Take this title, question and duplication matrix to your supervisor or a maritime remote-sensing researcher for a scope decision before registering the protocol. This supplies the method's Phase 3 human validation; a FastTrack workshop is an optional alternative, not a requirement.

## 8. Provenance and supporting material

- [Twenty selected FastTrack records, paper links and citation helpers](maritime-small-boats-selected-records-2026-11-02.md).
- [Raw FastTrack queries and responses](../metadata/maritime-review-2026-11-02/).
- Existing workspace maritime notes were used only as leads; the present recommendation relies on the live records and original-source checks described above.
- AI-assisted source retrieval, synthesis and appraisal were used. No detector was trained or evaluated and no numerical results were independently reproduced.
- The Scientific Critical Thinking skill informed the appraisal structure. Its procedural source is acknowledged separately from the maritime evidence: Kassis, T., Agarwal, V., He, Y., Patel, D., and Brueckner, A. M. (2026), [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://arxiv.org/abs/2609.00065). Author/year metadata were checked against the arXiv record. This is not evidence for a maritime research gap.
