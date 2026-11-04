[← Research candidates](../research-candidates.md)

# Reliable classification of ancient Sri Lankan coins from scarce and incomplete images

**ID:** X46 · **Area:** Computer vision — ancient numismatics

**Status:** Provisional research opportunity; not qualified · **Checked:** 30 October 2026

**Score:** 51.8/100, provisional. The low score reflects unresolved data and novelty, not the cultural importance of the topic. No dataset archive was downloaded and no model was trained or timed.

**Track:** General empirical research, confirmed by the team. **Phase:** 1, convergence and data feasibility; nearest-neighbour checks inform later refinement. **Verdict:** Back to the worksheet until the existing-data route is established.

**What's working:** This is a concrete computer-vision application with heritage value. Compact pretrained models could support objective experiments within the team's compute budget.

**The issues that matter:** (1) a usable ancient Sri Lankan training/test corpus is unverified; (2) few-shot matching, two-sided fusion and rejecting other coins already have prior work; (3) independent specimen counts and reliable labels may be too limited for three assessable contributions. These correspond to the convergence, duplication and execution-feasibility checks.

## 1. Problem

The proposed task is to assign a photographed ancient coin to an existing catalogue type, or return a shortlist or an undecided result when the evidence is insufficient. The intended users are people cataloguing existing collections. Time saved and expert-level performance have not been measured.

The [Sri Lankan Department of Archaeology](https://archaeology.gov.lk/index.php/ancient-coins) distinguishes coins of local and foreign origin. Accordingly, choose whether the project covers **coins minted in Sri Lanka** or **coins found/circulated in Sri Lanka**. Those populations require different labels.

Also define the historical scope. Lakdiva's [collection index](https://coins.lakdiva.org.lk/main.html) separates ancient and medieval material. A project using Polonnaruwa-period coins should state that it includes medieval coinage. Do not silently mix ancient, medieval, colonial and modern coins into one task.

**Illustrative failure:** An image supports an elephant motif but not the smaller symbols needed to distinguish two catalogue types. The system should not turn that partial evidence into a confident exact attribution. This is a proposed failure scenario, not a measured model result.

## 2. Research gap and question

**The broad topic is not itself a gap.** Building a CNN classifier or switching from CNNs to transformers would substantially overlap existing coin-recognition research. The Sri Lankan setting alone does not establish a methodological contribution.

These are **four candidate gaps to test**, not four verified discoveries or four projects to combine.

| Candidate gap | Narrow question worth investigating | Existing overlap and required distinction | Priority for this team |
|---|---|---|---|
| **G1. Few-example recognition across coinage traditions** | Does training on other ancient coinages help recognise local catalogue types when only a few labelled specimens per type are available? | Siamese matching already addresses unseen issues [S1]. A defensible addition requires demonstrated negative transfer or another specific failure, followed by an adaptation that beats frozen features, nearest prototypes and ordinary fine-tuning. | Conditional; useful shared baseline, high overlap risk. |
| **G2. Two-sided decisions when one side carries little usable evidence** | Can a learned fusion rule use the informative side without losing accuracy when the other side is missing, worn or poorly photographed? | Two-sided fusion already exists [S1, S2]. Test a narrower interaction between unequal side information and missing views. Compare single-side predictions, averaging, concatenation and simple side dropout before proposing complexity. | Best initial methodological lead **if paired local data exists**. |
| **G3. Distinguishing an unfamiliar type from a difficult familiar type** | Can the model leave an unfamiliar type undecided while retaining difficult known types? | Other-coin negatives already appear in a coin system [S4], and rejection is established ML. The proposed distinction is selective type attribution under both type novelty and reduced visual evidence. Generic confidence thresholding is a baseline. | Strong companion investigation **if enough held-out types exist**. |
| **G4. Recognition across collections and image sources** | Does accuracy survive a change from one collection's imaging style to another's? | Cross-collection testing is explicitly identified as future work in [S5]. A split alone is evaluation practice; a research contribution needs a measured failure and a tested training/adaptation remedy. | Important evaluation setting, but currently the hardest local data dependency. |

**Preferred conditional scope:** investigate G2, supported by G1 baselines and G3 reliability experiments. Treat G4 as an external test only if suitable independent existing collections can be verified. Do not promise all four as novel contributions.

**Working question for team revision:** Among the selected ancient Sri Lankan catalogue types, can a compact model trained with limited labelled specimens make more reliable type decisions from one or two available sides than strong single-side and fixed-fusion baselines?

Here, “more reliable” means lower error among accepted predictions at matched decision coverage, without hiding rare-class failures. Specify the catalogue, label budget and population after the data audit. This is a predictive question, not a causal or historical-origin claim.

**Rival explanation:** most apparent improvement may come from detecting duplicated specimens, removing backgrounds or tuning thresholds. If these simple controls explain the gain, report that finding and withdraw the more elaborate method claim.

## 3. Evidence from closest work

The sources below are primary papers, author-hosted manuscripts or dataset records. Reading depth is explicit; search absence does not prove originality.

| ID and source | Relevant established work | What was checked |
|---|---|---|
| **S1. Guo et al. (2023), [A Siamese Transformer Network for Zero-Shot Ancient Coin Classification](https://research-repository.st-andrews.ac.uk/handle/10023/27673)** | Pairwise issue matching and joint use of obverse/reverse already address scarce exemplars and unseen issues. This is the key duplication rival for G1 and G2. | Institutional abstract and indexed primary methods excerpts; experiments not reproduced. “Zero-shot” here concerns issues unseen during training, with reference specimens for matching, not identification without any reference evidence. |
| **S2. Aslan, Vascon and Pelillo (2020), [Two sides of the same coin](https://www.unive.it/pag/fileadmin/user_upload/centri/ECLT/documenti/publications/aslan2020_PRL.pdf)** | Semi-supervised graph methods already integrate both sides under limited labels. | Author-hosted full manuscript, abstract and method description inspected; no reproduction. |
| **S3. Anwar et al. (2021), [Deep ancient Roman Republican coin classification via feature fusion and attention](https://doi.org/10.1016/j.patcog.2021.107871)** | CoinNet already learns coin motifs with feature fusion and attention. Motif recognition, attention and feature fusion are not new by themselves. | Publisher abstract and contribution statement. |
| **S4. Melnykov and Kapeleshchuk (2024), [A CNN-assisted decision support system for ancient world coin classification](https://doi.org/10.31891/csit-2024-1-12)** | Training includes other coins as negatives. A generic “reject other coins” claim is therefore unsafe. | Publisher abstract only; this does not establish a rigorous unseen-type or shifted-domain rejection benchmark. |
| **S5. [Comparative Evaluation of Deep Transfer Learning Models for Ancient Coin Classification](https://doi.org/10.3390/app16168271) (2026)** | The indexed primary text describes physical-coin-grouped splits and a single-collection limitation. Leakage-safe splitting is already good practice; coarse classification performance does not establish exact-type performance. | Publisher search excerpts, including methods and limitations. Direct page fetch failed; full paper not independently read. |
| **S6. Reid and Arandjelovic (2026), [Do Transformers Understand Ancient Roman Coin Motifs Better than CNNs?](https://arxiv.org/abs/2601.09433)** | Image/text learning of semantic elements and transformer comparisons already exist. | Author preprint abstract; peer-review status not established. |
| **S7. Anwar (2026), [Reading Legends on Ancient Coins](https://arxiv.org/abs/2607.25455)** | Character detection on Roman coin legends already exists, as does earlier legend-and-image fusion discussed by the paper. | Author preprint abstract and HTML introduction, related work and dataset sections; no dataset download. |

**Directions not promoted:** local-script OCR needs existing coin-level character/word ground truth, not just stone-inscription or modern handwritten-character datasets. Symbol localisation needs existing spatial annotations. Restoration needs validation that reconstructed details preserve the true type. None of these local data routes was established. A heatmap alone cannot validate a numismatic explanation, and type classification does not establish authenticity or an exact minting date.

No citation trajectory or quantitative demand analysis was verified. Practical relevance is plausible; publication impact remains unassessed.

## 4. Proposed approach

Start with a reproducible specimen-grouped classifier and frozen-image-feature retrieval. Use existing catalogue labels, avoiding new expert annotation. A catalogue type is the target; the individual physical coin is the independent sampling unit.

If G2 survives the baseline and data checks, train a small fusion model using embeddings from the two sides, with explicit missing-side indicators. Side dropout and generated image corruptions can provide controlled training conditions without human quality labels. A learned gate is only a candidate mechanism, not novelty by itself.

For G3, train or calibrate a small acceptance model using held-out validation predictions. Evaluate known-type errors separately from unknown-type rejection. Begin with maximum probability, nearest-reference distance and simple calibrated thresholds.

The prototype can display existing test images, a type shortlist, reference examples and an undecided output. It is supporting engineering; it is not a member's research contribution.

## 5. Data and resources

**The mandatory existing-data gate is unresolved.** This bounded search did not establish a downloadable, adequately labelled ancient Sri Lankan benchmark with sufficient independent specimens and usable terms. That is an access finding, not proof that no dataset exists.

| Existing source | What the source actually supports | Fit and remaining checks |
|---|---|---|
| [SerendibCoins](https://arxiv.org/html/2505.18634v1) | Its methods describe current Rs. 1, 2, 5 and 10 coins in old/new design versions. | **Modern currency**, unsuitable as the main ancient-coin benchmark. The word “old” does not mean ancient. |
| [Lakdiva collection](https://coins.lakdiva.org.lk/) | Existing ancient images and descriptions are available. The site states conditional educational/nonprofit reuse permissions, attribution/source-link requirements and separate Wikipedia image terms. | A promising source, not a verified ML corpus. Do not treat the whole mixed-period site's image count as ancient training size or assume a blanket CC licence. Record applicable terms before any bulk reuse or redistribution. |
| [Lakdiva elephant-and-svastika specimen](https://coins.lakdiva.org.lk/ancient/ele%2Bsva/OBRW_H7_ele%2Bsva_struck.html) and [punch-marked examples](https://coins.lakdiva.org.lk/punch/) | Individual pages pair images with descriptions and measurements. The punch-mark page also contains incomplete or alternative attributions. | Page structure inspected, not pixels. Copy existing uncertainty into the manifest; do not silently turn ambiguous descriptions into exact labels. Images of both sides are one specimen, not two independent samples. |
| [Department of Archaeology portal](https://archaeology.gov.lk/coins/query/) | A public numismatic search interface exists. | Landing page read; advanced search timed out. Counts, exports, image rights, specimen IDs and usable labels remain unverified. |
| [Ancient Bangal Numismatic](https://data.mendeley.com/datasets/hpcxjy2z4v/1), released July 2026 | Maintainers report 2,704 images, 52 classes, annotation files and CC BY 4.0. | Potential South Asian pretraining or **explicitly re-scoped** benchmark. It is Bengal data, not Sri Lankan ground truth. Manifest, independent specimen counts and pairing not checked. The record says low-quality/damaged or uncertain material was removed, limiting natural-degradation claims. |
| [Corpus Nummorum release](https://zenodo.org/records/13748799) | Greek/Roman data with NLP-derived motif memberships, side/coin/type identifiers and source metadata described by the maintainer. Files are listed as about 3 GB. | Potential auxiliary data. Folder copies can repeat an image under several motif labels; approximately 179,000 entries do not mean that many independent coins. Motif memberships are not bounding boxes. Licence field was not populated in the retrieved record; verify terms. Not local evaluation evidence. |

**Data acceptance audit:** before selection, produce an existing-data manifest with source URL, applicable terms, physical specimen ID, side/pair ID, catalogue/type label, attribution certainty and collection/source. Count unique specimens per type after deduplication. Quarantine ambiguous exact-type labels without new expert adjudication. Confirm enough remaining specimens for separate training, calibration and test sets, and enough types for the planned unknown-type experiment. Do not invent a universal minimum from image totals.

If the project's ban on primary collection also excludes assembling already-published images into a corpus, this route requires an already released dataset. Confirm that interpretation with the supervisor as part of the data decision; do not replace it with new photography or expert labelling.

**Estimated resources:** CPU feature baselines, cached embeddings and occasional fine-tuning of a compact encoder on one modest GPU. Actual GPU memory, training time and archive size are unmeasured. No special cameras or coin acquisition are required by the plan.

**Fallback:** an existing non-Sri-Lankan ancient-coin dataset could support a revised general ancient-coin project, after its files and terms pass the audit. Such results would not validate recognition of Sri Lankan coins. If the local requirement is fixed and the data gate cannot be met, park X46.

## 6. Three-member contributions

One shared type-attribution problem. Each investigation can begin from the same unchanged baseline; another member's proposed model need not succeed first. This division is conditional on adequate data and supervisor agreement.

| Member | Research question and prediction | Comparison and removal test | Individually assessable result |
|---|---|---|---|
| A: Limited-label adaptation | Does source training transfer to local types? H: a small adapted encoder improves macro-F1 or retrieval recall under fixed specimen-label budgets. | Frozen pretrained features, nearest prototypes, linear head and ordinary fine-tuning; remove auxiliary coin training. | Label-budget curves, rare-type performance and any negative transfer. |
| B: Incomplete-side fusion | Can two-sided inference avoid harm from an uninformative side? H: missingness-aware fusion outperforms fixed fusion at matched label and compute budgets. | Single-side models, averaging, concatenation and side dropout; remove learned gating and missing-side indicators separately. | Paired/single-side results and controlled unequal-quality tests. |
| C: Reliable acceptance | Can wrong exact-type assignments be flagged? H: a trained acceptance model reduces error at matched coverage relative to raw confidence or distance. | Fixed classifier plus simple thresholds, calibration and trained error predictor; remove side-disagreement features. | Risk–coverage curves and unknown-type false acceptance, including rare known types. |

These are established method families with proposed investigations, not three proven innovations. If the data only supports a handful of reference images, this team structure is not justified.

## 7. Evaluation

- **Independent units:** group all views, crops, augmentations and repeated listings of a physical coin together before splitting. Cluster obvious duplicates conservatively. Report residual identity uncertainty. A new auction listing is not necessarily a new coin.
- **Separate tasks:** (a) new specimens from known types; (b) reference matching for types absent from training; (c) types absent from both training and the reference catalogue. Success on (b) does not establish rejection on (c). Keep unknown validation and final unknown test types separate.
- **Collection transfer:** claim G4 only with a compatible label taxonomy and an independent existing collection; source-specific class coverage must not explain the result. Do not substitute synthetic backgrounds for an external collection.
- **Baselines:** conventional local image features with SVM or reference matching; frozen pretrained embeddings; compact CNN fine-tuning; prototype/metric learning; single-side and fixed two-side fusion; simple acceptance thresholds. Compare with the closest published method when data and code access permit, otherwise state the reproduction limit.
- **Main outcomes:** type-level macro-F1, balanced accuracy, per-type recall and top-k retrieval recall. Report accepted-prediction error at predeclared coverage levels, coverage by type, risk–coverage area and unknown-type false acceptance. Confidence calibration measures are secondary to actual accepted errors.
- **Controls:** identical specimen budgets and tuning budgets; background masking baseline; natural missing-side subset when available; controlled side removal/blur/occlusion at recorded severities. Controlled corruption results do not prove robustness to archaeological wear. Do not assume a deliberately blank side is an acquisition defect.
- **Uncertainty:** use three seeds for trained models where feasible and specimen-level bootstrap intervals. Report class/test counts. Pairwise comparisons must not treat all image pairs as statistically independent.
- **Useful negative result:** strong frozen features or fixed fusion may match the proposed model, auxiliary training may harm local recognition, or abstention may disproportionately reject rare known types. These answer bounded questions even without a new best score.
- **Limits:** no demonstrated phone-photo, museum-workflow or expert-equivalence claim; no authenticity, valuation or historical-origin inference from type labels. No newly recruited users or expert raters are assumed.

## 8. Score and next decision

**Provisional score: 51.8/100; defer selection.** Dataset, novelty and feasibility ratings are below the team's required minima. No weighted score overrides the hard gates.

### Weighted rubric

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 2 | 6.4 | Low: strong overlap in matching and fusion; a distinct residual failure is unverified. |
| Public dataset quality/accessibility | 15 | 1 | 3.0 | Low: local pages exist, but no adequate labelled local corpus has passed an audit. |
| Feasibility and learning curve | 14 | 2 | 5.6 | Low: corpus assembly and label ambiguity threaten the 6–8 month window. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: adaptation, learned fusion and acceptance modelling support empirical ML. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Low-medium: objective protocol proposed; specimen identity and source coverage unresolved. |
| Three-member structure | 12 | 3 | 7.2 | Low-medium: connected investigations exist, but sufficient data and distinct contributions are unverified. |
| Real-world significance | 9 | 3 | 5.4 | Medium: heritage cataloguing is relevant; local workflow demand and benefit are unmeasured. |
| Compute/storage | 5 | 4 | 4.0 | Medium: bounded compact-model route appears practical; runtime unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: image/reference shortlist and undecided output are straightforward to demonstrate. |
| **Normalised total / 100** | **98** | | **51.8** | **Not qualified.** |

### Mandatory gates

Unknown denotes missing evidence, not a confirmed failure.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Bounded catalogue-type attribution with incomplete visual evidence. |
| 2. ML essential | Pass | The proposed questions concern learned recognition and decision errors. |
| 3. Train/adapt models | Pass | Adaptation, fusion and acceptance heads can be trained. |
| 4. Existing data accessible | Unknown | No adequate existing local training/test corpus verified. |
| 5. No unavailable human evaluation | Unknown | Existing exact-type labels may be too ambiguous without expert adjudication. |
| 6. Precise research gap | Unknown | Narrow hypotheses proposed; novelty and baseline failure unverified. |
| 7. Beyond application assembly | Pass | The conditional plan includes model comparisons and ablations. |
| 8. Objective evaluation | Unknown | Specimen IDs, label coverage and held-out type counts require a data audit. |
| 9. 6–8 month feasibility | Unknown | Data dependencies and baseline stability unresolved. |
| 10. Three connected contributions | Unknown | Proposed divisions need sufficient paired specimens and distinct empirical findings. |
| 11. No specialised/continuous high-end compute | Pass | Compact encoders and cached features avoid a high-end compute dependency. |
| 12. Manageable data reuse | Unknown | Source-specific terms exist; a permitted reproducible corpus has not been established. |
| 13. Useful negative findings | Pass | Transfer failure, fixed-fusion parity and rare-type rejection are useful bounded results. |

**Your next step:** take an existing-data feasibility manifest and this overlap assessment to the supervisor or a numismatics-informed mentor for a scope decision before selecting the topic. This research pass is not final topic approval.

[Team scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source checks and search record](../../metadata/ancient-sri-lankan-coin-checks.json)
