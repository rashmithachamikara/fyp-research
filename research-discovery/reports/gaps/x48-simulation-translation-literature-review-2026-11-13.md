# X48: simulation and translation literature review

Review date: 13 November 2026. Scope: AIS-driven optical overhead vessel simulation, learned appearance translation, temporal consistency, annotation preservation, and suitability as one student's research contribution.

## 1. Verdict

**Building an AIS-driven renderer and adding GAN/diffusion translation is not, by itself, a defensible novelty claim.** Ship image simulation, remote-sensing ship translation, maritime synthetic video, temporal translation, and simulator-guided geometry preservation all have substantial precedents. Training several translators for different sensors does not automatically add a research contribution.

**A narrower individual research package is plausible:** investigate whether translation corrupts small-vessel motion evidence, then adapt a bounded translation method to reduce that corruption at an acceptable appearance and compute cost. This is an evidence-bounded candidate, not a demonstrated first-ever gap. Its strongest competitors include general video methods, not only ship papers.

The recommended first step is a comparative pilot, not a commitment to invent a new video generator. The original behaviour project remains simulation-first, as approved by the supervisor. Real satellite video is optional. Real still imagery can support appearance and detection evaluation but cannot establish real motion-behaviour performance.

This review supplements, rather than silently replaces, the current [main proposal](x48-satellite-vessel-behaviour-from-synthetic-sequences.md) and [simulation-first review brief](x48-simulation-first-workload-and-review-brief.md). The proposed replacement workload below has not yet been adopted by the team or supervisor.

## 2. Search approach and limits

The requested Consensus Deep review was attempted with the complete research brief. It returned an insufficient-monthly-allowance error before producing research. **No findings in this report are attributed to Consensus.** Research continued through live searches of publisher records, arXiv, conference proceedings, author repositories and dataset records. No models were executed and no large datasets were downloaded.

Search families included:

- Synthetic aerial/remote-sensing ship imagery: UnityShip, MarSyn, RedNavi, Syn2Real, RSSA-12, SPAM-ControlNet and ShipGAN.
- Temporal sim-to-real: Video ControlNet, Recycle-GAN, semantic/temporal video translation, synthetic optical flow, 3D-guided neural rendering and Cosmos Transfer.
- Maritime image/video augmentation: SafeSea, MariData, visible-to-SWIR translation and maritime image-to-video generation.
- Candidate-gap challenges: ship trajectory/kinematic preservation, label preservation, small-object omission, misaligned paired translation, adaptive simulator sampling and sensor-conditioned generation.
- Data access: public repositories and Sentinel-2/AIS dataset landing pages.

Representative queries were `satellite ship synthetic video translation temporal consistency AIS`, `remote sensing ship progressive translation RSSA-12`, `ship simulation translation temporal`, `remote sensing image translation misaligned paired`, `ship trajectory preservation generation`, and `satellite ship temporally consistent generation`. Exact-title searches and selected references in retrieved papers expanded the search. The search is a targeted critical review, **not a registered systematic review or an exhaustive database export**. No defensible PRISMA screening count or citation-impact ranking is claimed.

Evidence codes in the tables: **M** = relevant methods/results sections inspected in accessible full text; **A** = publisher/author abstract or indexed primary-source excerpts only; **R** = official repository/project page inspected. M does not mean every supplementary file was reviewed. Lack of a reported feature is not proof that the feature is absent. Conference versions are distinguished from preprints. Recent web-index dates were not treated as publication dates.

Exclude anatomical blood-vessel papers as maritime evidence; images of spacecraft are also different from Earth-observation images. Street-view video generated from satellite photos is not satellite-view video. Vessel-type classification is not movement-behaviour classification.

## 3. Closest maritime and remote-sensing precedents

| Study and publication | Input and method | Still or temporal? | What it establishes; limit for X48 | Evidence |
| --- | --- | --- | --- | --- |
| [UnityShip: A Large-Scale Synthetic Dataset for Ship Recognition in Aerial Images, He et al., 2021, Remote Sensing](https://doi.org/10.3390/rs13244999) | Unity scenes, 79 vessel models; automatic boxes, categories and instance metadata | Published benchmark is still imagery | 105,086 images; synthetic pretraining/augmentation evaluated on real detection datasets. Rendering and exact synthetic annotations already exist; no movement-labelled video claim established here. | M, R |
| [Remote Sensing Fine-Grained Ship Data Augmentation Pipeline With Local-Aware Progressive Image-to-Image Translation, 2022, IEEE TGRS](https://doi.org/10.1109/TGRS.2022.3211517) | Imaging simulation, local-aware CycleGAN translation and foreground/background harmonisation | Still images | A particularly close rival: the simulation-plus-translation architecture existed in 2022. RSSA-12 contains 3,831 images across 12 ship categories. Task is ship-type classification. Full implementation and temporal details not verified. | A |
| [Real-Time Ship Segmentation in Maritime Surveillance Videos Using Automatically Annotated Synthetic Datasets, Ribeiro et al., 2022, Sensors](https://doi.org/10.3390/s22218090) | Blender-generated MarSyn data and segmentation models | Actual synthetic sequences; temporal filtering belongs to segmentation | 25 sequences of 1,000 frames; UAV camera at 150–1,000 m; ship lengths 3–125 m. Synthetic maritime video already exists. It is not a validated satellite sensor simulator or learned video translator. | M, R |
| [RedNavi: Building a 3D Scene of the Current Sea from AIS Data, Liu and Wakabayashi, 2022, Sustainability](https://doi.org/10.3390/su141912572) | AIS-driven Three.js scene construction and interactive maritime visualisation | Dynamic scenes | AIS-to-3D scene reconstruction already exists. Purpose is navigational representation, not an optical satellite behaviour benchmark. | M |
| [ShipGAN: Generative Adversarial Network based simulation-to-real image translation for ships, Dong et al., 2023, Applied Ocean Research](https://doi.org/10.1016/j.apor.2022.103456) | Unity ship scenes and CycleGAN-based translation | Image translation; explicit temporal mechanism not verified | Ship simulation followed by learned realism is established. Detection/segmentation used in evaluation. Author PDF retrieval timed out; do not categorically claim the entire method is temporally unaware. | A |
| [Syn2Real Detection in the Sky: Generation and Adaptation of Synthetic Aerial Ship Images, Wu et al., 2024, Applied Sciences](https://doi.org/10.3390/app14114558) | Unity and generative-image datasets; detector domain adaptation | Still images | SASI-UNITY has 10,000 images; experiments use six detectors and three real datasets. The paper distinguishes generation from feature/domain adaptation. Merely comparing engine and diffusion data is not new. | M |
| [Optical remote-sensing ship sample simulation using GANs, Ji et al., 2024, Acta Scientiarum Naturalium Universitatis Pekinensis](https://doi.org/10.13209/j.0479-8023.2024.067) | 3D models, GAN appearance transfer and real sea-background compositing | Still images | Direct remote-sensing simulation/translation precedent. Reported detection improvements are specific to its test protocol, not proof of motion fidelity. English title here is a descriptive translation of the Chinese title. | M |
| [SafeSea: Synthetic Data Generation for Adverse & Low Probability Maritime Conditions, Tran et al., 2024, WACV workshop](https://openaccess.thecvf.com/content/WACV2024W/MaCVi/papers/Tran_SafeSea_Synthetic_Data_Generation_for_Adverse__Low_Probability_Maritime_WACVW_2024_paper.pdf) | Masked diffusion changes sea backgrounds; filters check sea state and retained objects | Still-image editing | Background editing with object-preservation checks already exists in maritime work. Not an AIS-constrained overhead sequence study. | A, R |
| [Sim-to-real image to image translation for remote sensing fine-grained ship images using generative diffusion models, Deng et al., 2026, IJAEOG](https://doi.org/10.1016/j.jag.2025.104996) | Optical imaging simulation, SPAM-ControlNet and wake inpainting | Still-image generation in the inspected description | Closest diffusion rival. Wake regions use vessel parameters including speed, length and heading. Adding physically informed wake appearance is therefore not an untouched idea. No sequence-level behaviour-preservation experiment verified. | A, R |
| [MariData: One-Step Unpaired Image Translation for Maritime Environments, Henriksson et al., 2026, preprint](https://arxiv.org/abs/2606.03246) | CycleGAN-Turbo; 7,000 maritime images; day-to-fog/sunset/night | Still-image translation | Explicitly targets preservation of small maritime objects. Evidence inspected is mainly qualitative; hallucinations are acknowledged. Do not claim that small-object preservation or lightweight maritime translation is new. | M |
| [From visible imagery to synthetic short-wave infrared for maritime ship detection, 2026, Image and Vision Computing](https://www.sciencedirect.com/science/article/pii/S0262885626001204) | Unpaired real VIS/SWIR training, CycleGAN-Turbo/LoRA and structural losses; translator applied to Unity frames | Image translation; no temporal mechanism established in excerpts | Cross-sensor maritime synthetic augmentation and downstream detection already exist. Surface/shore camera domain, not satellite. Publisher-indexed methods inspected; direct page fetch blocked. | A |
| [Enhanced Text-Driven Directional Editing for Marine Dynamic Data Generation, Xue et al., 2026, JMSE](https://doi.org/10.3390/jmse14121139) | Prompt enhancement, masked sea/sky editing, then Cinemo image animation | Explicit image-to-video generation | Corrects any broad claim that maritime generative work is all still-image-only. The inspected methods use pretrained models without fine-tuning; the authors acknowledge lack of hydrodynamic validation. No AIS-path preservation established. Publisher record says published 22 June 2026 despite its December issue numbering; check metadata before formal submission. | A, indexed methods |
| [SatSAM2 / MatrixCity Video Object Tracking, Fan et al., 2025 preprint, revised 2026](https://arxiv.org/abs/2511.18264) | Synthetic satellite-style urban tracking benchmark; motion-constrained tracker | Synthetic video | MVOT has 1,500+ sequences and 157,900 annotated frames on the current project page. This is precedent for a synthetic overhead tracking benchmark, not evidence of maritime behaviour labels. | A, R |

## 4. General methods that also constrain novelty

| Study | Relevant contribution | Consequence for a proposed claim | Evidence |
| --- | --- | --- | --- |
| [SimGAN: Learning From Simulated and Unsupervised Images Through Adversarial Training, Shrivastava et al., CVPR 2017](https://openaccess.thecvf.com/content_cvpr_2017/papers/Shrivastava_Learning_From_Simulated_CVPR_2017_paper.pdf) | Refines simulated images with unlabelled real images; self-regularisation seeks to preserve annotations | Synthetic-to-real refinement with label preservation is an old general objective. | M |
| [Recycle-GAN: Unsupervised Video Retargeting, Bansal et al., ECCV 2018](https://openaccess.thecvf.com/content_ECCV_2018/html/Aayush_Bansal_Recycle-GAN_Unsupervised_Video_ECCV_2018_paper.html) | Unpaired translation using spatial and temporal information | Adding a temporal objective to an image GAN is not sufficient novelty. | A |
| [Video-to-Video Synthesis, Wang et al., NeurIPS 2018](https://papers.nips.cc/paper_files/paper/2018/hash/d86ea612dec96096c5e0fcc8dd42ab6d-Abstract.html) | Structured input sequences converted into photorealistic video | Label-map/geometry-guided video synthesis is established. Official code is available but old dependencies need testing. | A, R |
| [Preserving Semantic and Temporal Consistency for Unpaired Video-to-Video Translation, Park et al., ACM MM 2019](https://doi.org/10.1145/3343031.3350864) | Content-preserving and temporal-consistency objectives | Semantic label preservation plus temporal consistency has direct precedent. | A |
| [Long-Term Temporally Consistent Unpaired Video Translation from Simulated Surgical 3D Data, Rivoir et al., ICCV 2021](https://arxiv.org/abs/2103.17204) | Global learnable textures and view-consistency loss exploit known 3D scene geometry | Using simulator geometry for long-term consistency is not unique, even though the application is different. | A, R |
| [Learning Temporally and Semantically Consistent Unpaired Video-to-video Translation Through Pseudo-Supervision From Synthetic Optical Flow, Wang et al., AAAI 2022](https://arxiv.org/abs/2201.05723) | Synthetic motion avoids errors from estimated optical flow when enforcing consistency | Known/synthetic motion as translation supervision is already studied. | A, R |
| [Video ControlNet, Chu et al., 2023, preprint](https://arxiv.org/abs/2305.19193) | Synthetic optical flow constrains joint noise optimisation in pretrained diffusion; evaluates optical flow and tracking | It already measures identity switches and fragmentation. Temporal translation plus tracker evaluation is not a fresh gap. | M |
| [One-Step Image Translation with Text-to-Image Models, Parmar et al., 2024, arXiv record](https://arxiv.org/abs/2403.12036) | CycleGAN-Turbo and pix2pix-Turbo adapt pretrained one-step diffusion with small trainable components | Efficient fine-tuning or one-step generation alone is not new; useful reproducible backbone candidate. | A, R |
| [Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control, NVIDIA, 2025, technical report](https://arxiv.org/abs/2503.14492) | Segmentation/depth/edge video controls with spatially varying conditioning | Simulator output to controlled realistic video is already a general framework capability. | A, R |
| [Interactive World Simulation with Cosmos for Physical AI, NVIDIA, 4 November 2026, preprint](https://arxiv.org/abs/2611.06627) | Generates visual observations while an external simulator maintains state | Current work further weakens a broad simulator-plus-neural-renderer novelty claim. The inspected demonstrations concern robotics/driving, not a validated ship behaviour benchmark. | A, R |
| [Breaking the Dilemma of Medical Image-to-image Translation / RegGAN, Kong et al., NeurIPS 2021](https://arxiv.org/abs/2110.06465) | Treats misaligned target images as noisy labels with a registration network | Robustness to imperfect pairing is established generally; AIS-specific uncertainty must add something beyond reuse. | A |
| [Learning to Simulate, Ruiz et al., ICLR 2019](https://cseweb.ucsd.edu/~mkchandraker/pdf/iclr19_learningtosimulate.pdf) | Learns simulator parameter distributions for downstream utility | Adaptive scenario selection is not inherently new. A vessel-specific sampling investigation needs a distinct failure mechanism and equal-budget evaluation. | A |

One important result from Video ControlNet is mixed rather than uniformly positive: its tracking experiment reduces identity switches/fragmentation, but some other metrics worsen; the authors discuss blur as a possible explanation. This supports testing competing objectives, not assuming smooth output is always better. Its reported main experiment used eight GPUs for about 80 hours; that is not a minimum hardware requirement, but **training-free does not mean inexpensive**. See its Sections 4.2–4.3. The unusual GPU model/VRAM wording in the paper should not be used as a hardware specification without clarification.

## 5. What is and is not novel

| Proposed claim | Assessment | Closest rivals / what must change |
| --- | --- | --- |
| Generate ships with Unity/Blender | Established | UnityShip, MarSyn, Syn2Real |
| Drive a 3D scene with AIS | Established | RedNavi |
| Translate synthetic ships into realistic overhead images | Established | 2022 LoPIT/RSSA-12, 2024 Ji et al., 2026 SPAM-ControlNet |
| Add wake generation | Established in still-image work | SPAM-ControlNet; wake dynamics would need separate evidence and validation |
| Generate maritime videos | Established broadly | MarSyn and Xue et al.; exact motion-constrained satellite setting remains a narrower question |
| Preserve objects while changing maritime weather | Established | SafeSea, MariData |
| Add temporal consistency using flow or geometry | Established | AAAI 2022, Rivoir et al., Video ControlNet, Cosmos |
| Evaluate generated video using tracking | Established | Video ControlNet |
| Train one translator per satellite | Mostly implementation breadth | Must demonstrate sensor-conditioned transfer or calibration rather than style variants |
| Train from AIS-matched Sentinel-2 approximate pairs | Potentially useful, novelty unproven | Matching and misalignment-aware translation already exist separately; identify the specific pairing error and measurable solution |
| Quantify and reduce translation-induced errors in small-vessel motion and behaviour labels | Best candidate in this review, still conditional | Must add beyond generic geometry/temporal losses and tracker evaluation; compare the nearest methods directly |

**No exact duplicate was verified for the full combination of AIS-driven overhead bursts, translation, instance-level motion-error budgets and downstream operational behaviour-label evaluation. This is search-limited non-identification, not proof of absence.** A unique combination of familiar tools is also not automatically a scientific contribution.

The defensible question is whether a particular failure exists, matters for the target task, and can be characterised or reduced beyond appropriate baselines. The review provides reasons to test that question, not evidence that the proposed method will succeed.

## 6. Ranked candidate contributions

These are possible refinements of the user's proposal, not confirmed discoveries. Choose one primary investigation. Rankings reflect fit to this team's constraints rather than predicted publication success.

### A. Translation-induced motion errors and a vessel-aware constraint

**Priority: first. Novelty potential: moderate and conditional. Feasibility: moderate.**

Measure whether translated tiny vessels exhibit centroid drift, size changes, missed frames or identity confusion that change turning/stopping/closing labels. Investigate a compact constraint using simulator instance masks and motion correspondences, with weights normalised per vessel so ocean pixels do not dominate. Handle occlusion explicitly. Evaluate both same-vessel displacement and pairwise separation changes.

The potential addition is a specific method and evidence about error propagation into movement decisions at small object scales. It is not the generic invention of mask losses, motion constraints or identity preservation. A simple equal-weight temporal method, a semantic-preservation baseline and the proposed instance-weighted variant must be compared.

**Novelty would weaken or fail if** a close study already evaluates these kinematic/behaviour errors in overhead ship translation, or a stock temporal method solves the problem at equal compute. If the latter occurs, a careful empirical benchmark may remain useful, but the team should not advertise a new algorithm.

### B. Learning from uncertain AIS–image pairs

**Priority: second if accurate matching metadata is available. Novelty potential: moderate and conditional. Feasibility: data-dependent.**

Measure how AIS timestamp offsets, interpolation uncertainty, antenna-versus-centroid offsets and crop registration errors affect paired translator training. Compare unpaired training, strict filtering, ordinary paired training and an uncertainty-aware adaptation. Keep any learned registration in the supervision alignment path rather than letting the generator move vessels to satisfy a bad target.

A useful contribution would be a measurable regime in which uncertain pairs help or harm, with calibrated pairing weights or bounded alignment. RegGAN means registration-aware learning itself is not new. A single aggregate image-quality score would be insufficient.

**Novelty would weaken or fail if** an existing AIS-conditioned synthesis paper already treats the same uncertainty, or if the contribution is merely running a standard registration network. **Feasibility fails** if the chosen release has only type-labelled crops and no usable timing/geometry metadata. Artificial shift experiments alone establish controlled sensitivity, not the actual distribution of AIS mismatch.

### C. How much realism is worth buying for motion analysis?

**Priority: first as the pilot; possible empirical contribution. Novelty potential: moderate only with rigorous task-specific evidence. Feasibility: relatively strongest.**

Compare parameter-randomised rendering, framewise translation and motion-constrained translation under equal source paths, data quantity and compute accounting. Test whether better appearance measures correspond to better track/behaviour performance or conceal harmful displacement/blur. Include changes in the trade-off by vessel pixel size, contrast, cadence and encounter distance.

The research result could be a reproducible benchmark and a decision rule for when translation is worthwhile, not necessarily a new network. Generic claims that realism and utility differ are already established; Learning to Simulate and Video ControlNet are direct cautions. The team should ask its supervisor whether an empirical contribution plus model adaptation meets the module's individual criteria.

**Novelty would weaken if** the same overhead motion failure analysis is already published, or if the study only presents attractive images and routine FID comparisons. This option complements A rather than becoming a separate fourth project.

### D. Efficient temporal adaptation or selective translation

**Priority: extension. Novelty potential: low-to-moderate. Feasibility: moderate.**

Test whether a small adapter or selective treatment of vessel/background regions can retain motion fidelity at lower generation cost. Compare against ordinary low-rank adaptation, one-step translation, and simple temporal stabilisation. Video ControlNet already studies keyframe acceleration; CycleGAN-Turbo and MariData already cover efficient translation. A new efficiency claim needs comparable quality, motion retention and complete training/inference costs, not just fewer trainable parameters.

### E. Multiple sensors or learned scenario selection

**Priority: defer.** Both could support larger projects but create additional data and validation requirements. Sensor-conditioned generation requires genuine sensor metadata and held-out sensor evaluation, while adaptive sampling must beat stratified/random sampling at equal rendered-frame and training budgets. Do not expand from optical RGB into SAR merely by changing image style. Generic methods for both controllable generation and learned simulator sampling already exist.

## 7. Data and implementation access audit

Landing-page/repository inspection is not a successful download or reproduction. Model checkpoints, assets and dataset licences must be checked independently of repository code licences.

| Resource | Observed access and relevant content | Decision |
| --- | --- | --- |
| [SPAM-ControlNet repository](https://github.com/Slimyer/SPAM-Controlnet) | README marks training scripts, pretrained models and dataset resources as **to be released**. It still says under review, whereas the publisher has a journal record. | Correct the earlier optimistic assumption: do not make this implementation a critical dependency. Repository documentation may be stale. |
| [img2img-turbo](https://github.com/GaParmar/img2img-turbo) | Source directories, environment files and paired/unpaired training instructions visible; base-model licence separately referenced. | More practical starting point for an adaptation pilot; not executed here. |
| [Unsup_Recycle_GAN](https://github.com/wangkaihong/Unsup_Recycle_GAN) | Author repository for the AAAI temporal method is reachable. | Candidate temporal comparator; environment and model availability still need reproduction testing. |
| [SafeSea repository](https://github.com/martin-3240/SafeSea) | Author repository reachable. | Relevant object-retention baseline/design reference; not a satellite target dataset by default. |
| [UnityShip repository](https://github.com/heboyong/UnityShip-dataset) | Dataset landing repository reachable. | Do not assume the original Unity project/assets or unrestricted redistribution rights are supplied. |
| [MarSyn](https://vislab.isr.tecnico.ulisboa.pt/marsyn-dataset/) | Page directs users to contact the authors; paper describes availability upon request. | Useful precedent, but access is conditional and not a guaranteed public-download dependency. |
| Syn2Real/SASI | Paper's data availability statement says available on request. | Same access caution. |
| [MVOT/SatSAM2 project](https://fanrj3.github.io/SatSAM2/) | Dataset link visible; tracker code marked coming soon on inspected page. | Optional general overhead tracking data, not a maritime behaviour source. |
| [Finnish Sentinel-2 vessel dataset](https://zenodo.org/records/15019034) | Open Zenodo record; product metadata and annotations. Boxes can include wake pixels. | Good candidate for held-out still-image detection evaluation; not exact hull masks or sequence labels. |
| [AIS-Associated Sentinel-2 Image Patch Dataset](https://zenodo.org/records/20179706) | Open record with file listing, total 39.1 GB; bands B2/B3/B4/B8, class and acquisition/location metadata; South Florida package included. | Promising for appearance data and pairing inspection. Raw full AIS tracks and accurate geometry should not be assumed from the title. |
| [Ship-S2-AIS](https://zenodo.org/records/7229756) | Public description but **restricted files**. Describes 13k tiles from 29 Sentinel-2 products. | Do not list as assured freely downloadable paired training data. |

Use the existing Brest/AIS plan for source movement only after the task-specific cadence audit. No archive was parsed in this review. Do not infer adequate manoeuvre or encounter coverage from the number of AIS messages.

## 8. Sentinel-2 suitability and scope

Sentinel-2 RGB bands are 10 m, and repeat coverage occurs over days rather than continuous video. [Official mission documentation](https://sentiwiki.copernicus.eu/web/s2-mission). A 20 m hull spans roughly two pixels along its length before orientation and blur, which is a serious setting for preserving motion evidence, not grounds to claim that all small boats are undetectable.

AIS matching can support approximate scene pairs, but it does not recover the true ship mesh, sea texture, wake, atmospheric state or illumination. Acquisition timing and alignment must be checked; local observation time can differ from the product filename's reference time. [Heiselberg, Aircraft and Ship Velocity Determination in Sentinel-2 Multispectral Images](https://doi.org/10.3390/s19132873).

If the translator learns Sentinel-2 appearance, frequent generated frames represent a **hypothetical frequent sensor with Sentinel-2-like appearance**. They do not validate high-resolution SkySat-style video or a 2 m sensor. Choose either a distinct 10 m experiment or appropriately sourced high-resolution optical target imagery. Avoid training one blended style from incompatible sensors and calling the result sensor-faithful.

Real still-image datasets can test appearance statistics and detection on independent images. They cannot confirm the generated sea's temporal dynamics, true vessel motion or behaviour classification on real sequences. This limitation does not invalidate the supervisor-approved simulation-first study; it bounds the conclusions.

## 9. Recommended one-person package

Working description: **Motion-preserving translation of synthetic optical vessel sequences: methods and evaluation.**

Core hypothesis to investigate: instance-aware motion constraints reduce translation-induced localisation and behaviour errors compared with equally tuned framewise and generic temporal translation, without unacceptable loss of appearance similarity or excessive cost. This is a proposed hypothesis, not an empirical finding.

The student owns:

1. A reproducible rendering/translation interface exporting frames, masks, persistent IDs, positions, timestamps, camera mapping, motion correspondences and occlusion masks.
2. Reproduction/adaptation of one manageable image translator and one temporal comparator.
3. One clearly specified methodological change, conditional on finding a baseline failure.
4. Independent evaluation of object retention, kinematic distortion and resource cost; integration experiments with the team's behaviour models.
5. Ablations, failure analysis and a released benchmark subset if licences permit.

Shared responsibilities remain AIS cleaning, behaviour definitions, splitting, baseline renderer support and common evaluation tools. The student must not become the sole infrastructure bottleneck. The other students can start from rendered observations and coordinate-level corruption while the translator develops.

Potential revised team allocation: one student on translation fidelity, one on individual motion, one on pair interactions. This could replace the previous conditional repeated-pattern package; it should not simply add a fourth major workstream. Final allocation requires supervisor agreement.

## 10. Experimental design

### Comparisons

- **B0:** plain renderer with a declared optical observation model.
- **B1:** tuned domain randomisation and inexpensive colour/contrast matching.
- **B2:** an adapted framewise translator.
- **B3:** a credible generic temporal/semantic translator on a bounded common subset.
- **P:** the proposed vessel-aware variant of the same manageable backbone.

Keep source paths, scene/asset distributions, sample counts, detector inputs and tuning budgets comparable. Report compute differences instead of hiding them. If a large model cannot be reproduced, mark the comparison missing and narrow the claim; do not label a weak smoothing filter as the strongest temporal baseline.

### Three separate evaluation questions

**Translation fidelity:** With the detector/tracker fixed, does changing only the image transformation alter the measured path? This is a test of visual evidence and evaluator response, not a test of downstream training benefit.

**Training utility:** Train equivalent downstream models with each data regime, then test all of them on the same independent test distributions. Testing each model only on its own translator's output rewards style matching and cannot establish general utility.

**Real still-image transfer:** Where data permit, evaluate detection on held-out real acquisition scenes. Keep that result separate from simulation-only behaviour results. No claim of real-video behaviour accuracy follows.

### Measures and safeguards

| Dimension | Measures | Interpretation limit |
| --- | --- | --- |
| Object retention | Missing/extra vessels, mask/box agreement, centroid/size errors | Simulator masks say where objects should be; they do not prove what is visible after translation. Use independent visual audits or separately evaluated estimators. |
| Motion | Displacement error, speed/turn-rate error, relative-distance error, ID switches and track fragmentation | Estimate only where support permits; count missing tracks separately and in end-to-end outcomes. |
| Appearance | Distribution measures and vessel/background-specific summaries against held-out real stills | FID/KID can be dominated by ocean/background and sample size; no single score proves sensor realism. |
| Temporal | Occlusion-aware flow-warp error, vessel appearance stability, long-sequence drift | Static, copied or blurred videos can score well on simplistic consistency measures. |
| Behaviour | Per-class precision/recall, macro-F1, false event alerts, coverage and insufficient-evidence rate | Motion labels remain operational simulation labels, not verified intent or illegal activity. |
| Cost | Peak VRAM, training time, seconds/frame, failure/retry and rejected-sample rates | No low-GPU claim until measured on available hardware. |

Do not use the identical frozen detector both as the sole training constraint and sole evaluator: it can create an artificial success specific to that detector. Include a second evaluator and a small documented manual audit of generated outputs where permitted; this does not require collecting new real footage or recruiting domain experts. If manual auditing is unavailable, acknowledge estimator dependence.

Measure distortion relative to the plain-render baseline as well as against simulator truth. A detector's failure on both images is not necessarily caused by the translator. Identity loss in an image GAN often means an appearance reconstruction objective, not preservation of tracking IDs; keep these definitions distinct.

A useful analytical illustration: if a translation moves successive detected centroids by opposite one-pixel errors, displacement error can reach two pixels. At 10 m/pixel and a one-second interval, that is a 20 m/s apparent velocity error; at 2 m/pixel, 4 m/s. These are worst-case arithmetic examples, not measured error rates. Longer-interval differences and smoothing change the effect. They explain why attractive single frames are inadequate evidence.

Separate true occlusion/resolution loss from hallucinated object removal. The method must preserve the declared sensor observation, not artificially force every ground-truth ship to be brightly visible. Similarly, preserving rigid hull motion does not guarantee physically correct specular water or wake motion. Whole-ocean flow consistency may be inappropriate for view-dependent reflections.

### Splits and uncertainty

Use the current brief's vessel-disjoint partitions and dependency-component resampling for AIS-derived scenes. All repeated windows/renders/translations of a source episode stay together. Real translator training and evaluation must additionally be separated by acquisition scene/date/region; adjacent patches from the same Sentinel product are not independent test samples. Keep translated versions, crops and originals in the same group. Check pretrained-model data overlap where disclosed; otherwise state it is unknown.

Freeze the proposed change and primary comparison after pilot development. Use paired differences over source groups, with confidence intervals and practical effect thresholds. Report independent-group counts; overlapping frames do not create independent samples. No published percentages from different datasets should be treated as a common leaderboard.

## 11. Bounded feasibility pilot and decision rules

Proposed two-to-four-week pilot, conditional on actual hardware and data access:

1. Obtain a small licensed target-image sample and inspect metadata. Decide whether Sentinel-2 scale or a higher-resolution optical domain is the actual target.
2. Render a modest set of independent transit, turn and two-vessel approach scenes with exact masks and motion. Include short diagnostic clips before rendering 60–120-second sequences. Do not silently shorten the eventual behaviour observation window to fit a video model.
3. Run plain/randomised rendering, one framewise translator and one temporal baseline on the same diagnostic scenes. Test the smallest meaningful vessel sizes, not only large easy ships.
4. Measure motion error, object loss, quality trade-offs, throughput and memory. Use procedurally controlled cases as well as supported AIS excerpts, with separate provenance.
5. Select one failure mechanism and one adaptation. Estimate the full experimental workload from measured cost rather than pretrained-model parameter count.

**Proceed with a method contribution** if the data/compute are accessible, a practically relevant failure remains under tuned baselines, and the proposed change can be isolated with suitable evidence.

**Reframe as an empirical benchmark** if existing methods are competitive but the controlled comparison reveals a reproducible, useful trade-off or failure envelope. Supervisor acceptance of that contribution type matters.

**Reduce or replace the package** if access is only promised, baseline translation cannot run within the available budget, or there is no identifiable question beyond routine integration. Do not expand to more sensors to compensate for a missing research question.

A negative result can be useful: translation might offer no downstream benefit beyond domain randomisation, or improve appearance while worsening small-vessel motion. A wide uncertainty interval is inconclusive, not evidence of equivalence. Real-video availability is not a mandatory pilot gate under the agreed project scope.

## 12. Corrections to the earlier discussion and remaining unknowns

- The 2022 remote-sensing simulation/LoPIT pipeline is an important earlier direct rival that was missing from the short answers.
- Temporal consistency and downstream tracking evaluation are both established; combining them is not enough by itself.
- Maritime video generation is not absent: distinguish procedural MarSyn video, generic video translation and maritime image animation.
- SPAM-ControlNet's repository currently does not establish that the promised training resources are downloadable. A paper's availability sentence is insufficient.
- Preserving small maritime objects is already explicit in SafeSea/MariData-related work. The possible contribution must be more specific than that phrase.
- Matched AIS and real satellite photos are approximate supervision, not exact paired render ground truth.
- No exact matching maritime study was verified for the proposed full motion/behaviour-label audit, but indexing, inaccessible full texts and terminology limit this conclusion. The follow-up search should target the selected mechanism once the pilot makes it concrete.
- No defensible forecast of publication success, no measured class support, no demonstrated GPU fit and no operational dark-vessel performance claim follow from this review.

The supervisor-facing verdict is: **retain the simulation/translation member only with a bounded hypothesis, strong temporal baselines, independent motion/label evaluation and a feasible pilot. Treat the simulation framework as the experimental apparatus; the research contribution is the tested method or finding.**

## 13. Methodological assistance

The scientific-critical-thinking skill informed distinctions between observed evidence, missing reporting and extrapolation, as well as the proposed controls and uncertainty treatment. Methodological acknowledgement, not maritime evidence: Kassis, T., Agarwal, V., He, Y., Patel, D., and Brueckner, A. M. (2026), [Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents](https://doi.org/10.48550/arXiv.2609.00065). The current arXiv record was checked. Consensus was attempted but quota-blocked; this report is not a Consensus-generated review.
