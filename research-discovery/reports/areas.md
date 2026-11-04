# Research areas

Evidence reviewed: **27–30 October 2026**. Based on the [team and module criteria](../../research-module-and-team-criteria.md).

These are starting areas, not validated research gaps. Priorities reflect team fit and available benchmark leads.

The aim is one shared problem with three independently assessable research contributions. Contributions may share data and models; writing papers and publication are optional.

| Research area | Directions worth exploring | Starting data | Priority |
|---|---|---|---|
| **Sinhala document reading** | Correct OCR mistakes without changing correct text or numbers | [Real legislative pages](https://huggingface.co/datasets/avishadilhara/sinhala-ocr-lk-acts-1010); manifest and row schema checked | X43 parked: current correction gap overlaps prior work |
| **Mixed-language customer feedback** | Retain rare mixed opinions in a small model | [NLPC-UOM comments](https://huggingface.co/datasets/NLPC-UOM/Sinhala-English-Code-Mixed-Code-Switched-Dataset); CSV parsed; rare labels need care | Practical Sri Lankan lead; see X44 |
| **Reported dengue forecasting** | Use weather only when helpful; show forecast ranges | [Maintainer data package](https://github.com/thiyangt/denguedatahub); case CSV parsed; weather join unverified | Practical Sri Lankan lead; see X45 |
| **Ancient coin recognition** | Limited examples, missing/unreadable sides and reliable type decisions | [Lakdiva existing collection](https://coins.lakdiva.org.lk/); local corpus size, labels and reuse route unverified | Conditional; X46 requires an existing-data audit |
| **Industrial visual inspection** | Small defects, limited labels, changing imaging conditions | [VisA](https://github.com/amazon-science/spot-diff) | Start here |
| **Document AI** | Layout understanding, unfamiliar formats, efficient extraction | [DocLayNet](https://github.com/DS4SD/DocLayNet) | Start here |
| **Energy and demand forecasting** | Missing readings, changing patterns, prediction intervals | [UCI electricity](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014) | Start here |
| **Acoustic understanding** | Microphone differences, scarce labels, compact models | [DCASE](https://dcase.community/challenge2025/) | Start here |
| Agricultural image understanding | Background shortcuts, unfamiliar inputs, field transfer | [PlantVillage](https://github.com/spMohanty/PlantVillage-Dataset) | Explore next |
| Satellite image understanding | Land cover, limited labels, spectral information | [EuroSAT](https://github.com/phelber/eurosat) | Explore next |
| Machine condition monitoring | Rare faults, operating-condition changes, false alarms | [DCASE](https://dcase.community/challenge2025/); [AI4I, synthetic](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset) | Explore next |
| Sensor-based activity recognition | Sampling loss, short transitions, subject transfer | [UCI HAPT raw streams](https://archive.ics.uci.edu/dataset/341/smartphone+based+recognition+of+human+activities+and+postural+transitions) | Explore next |
| Transparent-object perception | Glass boundaries, misleading reflections, segmentation reliability | [Trans10K author release](https://xieenze.github.io/projects/TransLAB/TransLAB.html); image terms need clarification | Explore next |
| Wildlife image understanding | Crop reliability, unfamiliar cameras, background shortcuts | [CCT20](https://lila.science/datasets/caltech-camera-traps) | Explore next |
| Waste-material segmentation | Clutter, rare materials, limited mask labels | [ZeroWaste](https://ai.bu.edu/zerowaste/) | Explore next |
| Elephant movement and human–elephant conflict | Seasonal passage, recorded conflict, corridor/fence permeability and acoustic reliability | Existing Sri Lankan outcomes mostly request/licence-dependent; [LUCIS supplement](https://github.com/batlahiya/Supplementary-data-and-figures-for-the-LUCIS) has verified model/planning outputs | Conditional on data access |
| Satellite–AIS vessel association | Sparse reports, competing vessel identities, calibrated matching and rejection | [GR-PTA author subset](https://github.com/Du-Jinjin/GR-PTA); independent labels, scale and rights need verification | Conditional on paired data |
| Satellite maritime observation and vessel identity | SAR annotation gaps, nearshore failures, optical/SAR ReID, wake reliability and AIS reception drift | [HOSS: 82.9 MB, CC BY 4.0](https://doi.org/10.5281/zenodo.15860212); [UEIKAP: manifests checked](https://doi.org/10.5281/zenodo.18391027) | Explore HOSS first; other claims have data prerequisites |
| Recommender systems | Cold start, sparse feedback, popularity bias | [Stable MovieLens releases](https://www.grouplens.org/datasets/movielens/) | Explore next |
| Defensive cybersecurity ML | Cross-capture transfer, rare attacks, reliable detection | [UNSW-NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset) | Optional |

Dataset links are starting resources, not completed access audits. Field images need independent validation; AI4I is synthetic and UNSW-NB15 is laboratory traffic. Use a stable MovieLens release for research.

The 28 October passes add candidates in document layout, radar–optical land cover, road damage, quantised search, text disagreement, soft sound events, audio annotation views, sensor-detector selection, activity transitions and intermittent demand. Five further vision candidates cover plant-lesion crops, transparent-object boundaries, wildlife crop reliability, building-change alignment and rare-material pseudo-labels. Five elephant-related opportunities (X16–X20) were also assessed using the supplied review and selected original sources. Their local outcome-data access is unresolved. These are candidate research opportunities; the linked briefs distinguish established findings from proposed gaps.

Ten further maritime candidates (X22–X31) investigate specific failure modes beyond generic dark-vessel detection. HOSS visual re-identification is the clearest bounded data route; encounter duration and intentional-disabling claims require different reference evidence. These are proposed questions, not verified novelty.

[View all research candidates and scores](research-candidates.md).

The three local directions added on 30 October use existing Sinhala documents, mixed-language comments and reported dengue counts. They have separate gap briefs, simple examples and the same project scoring rules. X43 is now parked because its current correction proposal overlaps prior work. X44 and X45 remain provisional; neither is a certified novel topic.
