[← Research candidates](../research-candidates.md)

# Will landslide-risk models transfer to another region?

**ID:** X37 · **Area:** Geospatial ML — landslide susceptibility

**Status:** Provisional; Investigate; dated inventories and transfer gap unresolved; not qualified · **Imported:** 30 October 2026

**Provisional score:** 65.3/100 · No model training or timing performed.

**In plain language:** Test AlphaEarth features across regions while using only imagery from before the landslide period.

**Origin:** supplied shortlist, rank 4, page(s) 5. Its source verdict was “GO with reframing”. This brief uses the team’s current criteria; the source rank and verdict are not our qualification decision. [Import record](../../metadata/pdf-shortlist-import.json).

## 1. Problem

A model may recognise where landslides already happened instead of estimating where future landslides are more likely. It may also learn one region’s terrain or reporting patterns and fail elsewhere. Planning requires a careful distinction between future susceptibility and post-event scar mapping.

## 2. Research gap and question

**Question:** With strictly pre-event AlphaEarth features, how much landslide-susceptibility performance transfers across regions, and can small-model adaptation improve it without target test labels?

**What is still uncertain:** The cited AlphaEarth study already evaluates three regions. That does not establish that it trains in one and tests in another. The proposed gap concerns region-to-region transfer with time-safe features, not merely using AlphaEarth or adding Sri Lanka. Cross-region training details and newer neighbours remain unchecked.

**Hypothesis and alternative:** A small feature-alignment model will improve held-out-region prediction over direct transfer. Alternatives are that terrain-only predictors transfer better or that any apparent gain disappears after removing post-event information.

## 3. Evidence from closest work

This is a bounded import check, not a complete novelty audit. “Checked” below refers to the stated abstract or source page, not a reproduction of the study. The supplied PDF’s wider search and verification claims are not independently certified.

| Source | What it supports | Reading limit |
|---|---|---|
| [AlphaEarth for Landslide Susceptibility Mapping](https://arxiv.org/abs/2601.07268) | The abstract evaluates AlphaEarth features across Taiwan, Hong Kong and Italy. Its abstract alone does not establish a train-one-region/test-another protocol. | Primary abstract checked; methods not reviewed. |
| [Google Satellite Embedding V1](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL) | Official catalogue: annual 64-dimensional 10 m features, coverage 2017–2024, CC BY 4.0 and an Earth Engine loading route. | Official catalogue checked; raster samples not downloaded. |
| [Hong Kong Enhanced Natural Terrain Landslide Inventory](https://data.gov.hk/en-data/dataset/hk-cedd-csu-cedd-entli) | An official inventory and dictionary route exist; event dates, completeness and reuse terms need inspection. | Official source page checked; inventory not downloaded. |

## 4. Proposed approach

Define one future observation period per inventory. Use only annual features whose entire calendar year ends before that period starts. Compare conventional terrain features with AlphaEarth features, then test a small adaptation method and probability calibration.

**Prototype:** demonstrate the same research pipeline on held-out existing examples, showing its output, errors and uncertainty. The interface is supporting work, not an individual research contribution.

## 5. Data and resources

**Data and access:** Google’s official catalogue lists 10 m, 64-dimensional annual embeddings for 2017–2024, with CC BY 4.0 terms and an Earth Engine loading route. Do not inherit the PDF’s 2025 coverage claim. Hong Kong ENTLI has an official inventory page and separate terms, but date completeness and a second compatible region are not verified. Sri Lankan NBRO data are not secured.

**Resources:** Estimate only: export a bounded area, cache embeddings and train random forests or small neural heads. Access to Earth Engine must be registered. Export quotas, raster volume and inventory preparation could dominate the work; avoid global downloads.

**Fallback:** Start with time-separated, spatially blocked Hong Kong data if dates permit. That tests local transfer only. Do not retain a cross-country claim without a second usable inventory.

These are feasibility estimates, not demonstrated training costs. The PDF’s resource allowance does not establish this team’s actual GPU or paid-service access.

## 6. Three-member contributions

All members address the shared question in section 2. Each investigation starts from the same unchanged baseline so that another member’s proposed improvement is not a prerequisite.

| Member | Question and hypothesis | Method, comparison and removal test | Independently assessable result |
|---|---|---|---|
| A: Leakage and representation | Does using pre-event features change the ranking of methods? H: same-year features inflate apparent predictive skill. | Compare terrain-only and embedding heads under matched samples; remove same-year imagery from the diagnostic comparison. | Transfer PR-AUC and the size of the time-leakage effect. |
| B: Region adaptation | Does small-model adaptation help an unseen region? H: source-trained alignment improves direct transfer. | Compare direct transfer, simple feature normalisation and learned alignment; remove alignment losses. | Held-out-region PR-AUC without target test labels. |
| C: Probability reliability | Do predicted probabilities remain meaningful elsewhere? H: source-only calibration can identify unreliable areas. | Compare raw scores, logistic calibration and a small uncertainty head; remove spatial/context features. | Brier score and risk–coverage curves, alongside discrimination. |

Shared data access is a common prerequisite. A failed proposed method can still produce an interpretable comparison. Papers are optional; the work must remain attributable through experiments and removal tests. Where the gate table marks the team structure Unknown, the shared data barrier prevents treating this as an execution-ready split.

## 7. Evaluation

- **Primary measure:** PR-AUC under a fixed and documented background-sampling scheme, with ROC-AUC, recall, Brier score and calibration plots. Inventory absence is not proof that a location is safe.
- **Keep data separate:** Hold out whole regions and future periods; use spatial blocks within training regions. Keep neighbouring pixels and all representations of one event together. Explain background sampling and inventory reporting bias.
- **Baselines:** Logistic regression and random forest on terrain factors, an AlphaEarth feature classifier and the cited deep-learning formulation if reproducible. Match labels and training budgets.
- **Removal tests:** use the member-specific tests above; keep data, tuning effort and inference budgets comparable.
- **Uncertainty, error analysis and useful negative findings:** Analyse terrain, region, event date and distance to known slides. Bootstrap by spatial block/event and repeat trained heads with three seeds. Useful findings include weaker transfer after time-safe evaluation or no advantage over terrain factors.
- **Claim limit:** benchmark findings support the stated task and conditions. They do not establish reliable real-world deployment or a guaranteed benefit for users.

## 8. Score and next decision

**Provisional score: 65.3/100; not qualified.** Investigate; dated inventories and transfer gap unresolved. Ratings assess the imported proposal and access risks, not achieved results. Unknown gates block qualification; failed gates reject the current design regardless of score.

### Weighted rubric

The existing nine weights total 98. Scores are normalised to 100; decimals reflect arithmetic, not certainty. These comparison scores follow the existing provisional-scoring policy and do not override the gates.

| Category | Weight | Rating / 5 | Weighted points | Confidence and reason |
|---|---|---|---|---|
| Research gap and defensible novelty | 16 | 3 | 9.6 | Low-medium: time-safe transfer is testable; a multi-region predecessor already exists. |
| Public dataset quality/accessibility | 15 | 2 | 6.0 | Low: embeddings are documented, but two compatible dated inventories are not secured. |
| Feasibility and learning curve | 14 | 3 | 8.4 | Low-medium: compact heads are manageable; geospatial preparation is a dependency. |
| Technical AI/ML depth | 12 | 4 | 9.6 | Medium: representation, adaptation and calibration include model-level work. |
| Evaluation/reproducibility | 12 | 3 | 7.2 | Medium-low: proposed splits are appropriate but outcome timing and negatives are unverified. |
| Three-member structure | 12 | 4 | 9.6 | Medium: leakage, transfer learning and probability reliability give attributable results. |
| Real-world significance | 9 | 4 | 7.2 | Medium: landslide susceptibility is consequential; no operational warning benefit is demonstrated. |
| Compute/storage | 5 | 4 | 4.0 | Medium: bounded cached features should fit; export and storage remain unmeasured. |
| Prototype | 3 | 4 | 2.4 | Medium: a research map viewer can show probabilities and limitations. |
| **Normalised total / 100** | **98** | | **65.3** | **Not qualified.** |

### Mandatory gates

Pass describes the bounded plan, not a completed experiment.

| Gate | Decision | Evidence |
|---|---|---|
| 1. Specific real problem | Pass | Section 1 defines a concrete failure and affected users; its local magnitude is not measured. |
| 2. ML essential | Pass | The shared question concerns learned predictions rather than only an interface. |
| 3. Train/adapt models | Pass | The bounded design includes training or systematic model adaptation. |
| 4. Existing data accessible | Unknown | Two dated compatible inventories with usable observation periods are not secured. |
| 5. No unavailable human evaluation | Pass | The retained plan uses existing labels and excludes new participants or expert labelling. |
| 6. Precise research gap | Unknown | The predecessor already covers three regions; the distinct transfer contribution needs methods review. |
| 7. Beyond application assembly | Pass | The proposal specifies learning experiments, comparisons and removal tests. |
| 8. Objective evaluation | Unknown | Pre-event timing, inventory completeness and background sampling are not verified. |
| 9. 6–8 month feasibility | Unknown | Inventory preparation and export feasibility must be tested. |
| 10. Three connected contributions | Pass | Three connected research questions have separate comparisons and attributable results. |
| 11. No specialised/continuous high-end compute | Pass | The retained scope starts with small models or cached features and no dedicated hardware. |
| 12. Manageable data reuse | Unknown | The exact combination of data, model and derivative-output reuse terms is not verified. |
| 13. Useful negative findings | Pass | Section 7 identifies useful findings even if the proposed method does not improve performance. |

**Next decision:** Secure two dated, reusable inventories and inspect the cited study’s cross-region protocol before presenting this as a new transfer gap.

[Scoring criteria](../../../research-module-and-team-criteria.md#8-evaluation-rubric) · [Source and import limits](../../metadata/pdf-shortlist-import.json)
