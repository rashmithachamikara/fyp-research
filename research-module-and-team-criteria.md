# Research Module and Team Criteria — Agent Handoff

Updated: 27 October 2026

## 1. Module and Project Context

### Confirmed or strongly established

- Institution: University of Moratuwa.
- Degree: BSc (Hons) in Information Technology.
- Academic level: final-year undergraduate research project.
- Team size: three students.
- Overall duration: no more than one year.
- Existing workspace planning assumes a 6–8 month research and implementation window inside that year.
- The project must address a significant real-world problem.
- AI/ML must be central to the research, not an optional application feature.
- Models must be trained, fine-tuned, adapted, or otherwise investigated empirically using existing datasets.
- The work must contain a clear research contribution; building an application around an existing model is insufficient.
- Each team member must have a substantial, independently assessable research contribution.
- The three contributions must form one coherent project rather than three unrelated mini-projects.
- Questionnaires and data collection of that sort should be avoided for training or primary evaluation.
- Deployment is not compulsory, but a usable prototype is preferred.
- Publication is preferred.
- Public datasets and reproducible evaluation are strongly preferred.
- No department-defined threshold for what counts as “advanced AI/ML” has been provided.
- No stated department restriction currently prohibits pretrained models, transfer learning, generative AI, external APIs, or synthetic data. Pretrained models and transfer learning are assumed permissible but should be confirmed.
- No formal ethics-review process is known to the team. This does not remove the obligation to manage privacy, licensing, fairness, safety, and misuse risks.

### Important module detail to verify

The existing workspace brief states that each member is expected to undertake a distinct project under a shared focus and produce a separate paper, for a total of three papers. The current chat confirmed independent assessment but did not independently reconfirm the three-paper rule. A future agent should verify this when the official module documentation becomes available.

### Information not yet provided

- Proposal, interim-review, implementation, and final-submission dates.
- Mandatory proposal sections and official assessment rubric.
- Exact individual-versus-group marking rules.
- Whether deployment or a demonstration is eventually required.
- Formal rules concerning pretrained models and external datasets.

## 2. Team Profile

### Current technical level

- The team has introductory ML knowledge, including material comparable to Andrew Ng’s introductory Stanford ML course.
- The team has completed small competition-style projects, such as training a weather-prediction model on a provided dataset.
- Only one member has previously trained or fine-tuned a deep-learning model.
- Backend development is the team’s strongest shared engineering capability.
- Familiar languages and platforms include Python, JavaScript, and .NET.
- The team is still developing specialist skills in computer vision, NLP, audio, time series, MLOps, and advanced modelling.

### Research interests

- Primary current preference: computer vision.
- Broader interests recorded in the workspace: machine learning, deep learning, reinforcement learning, recommender systems, image processing, signal processing, and speech processing.
- The team is open to other areas when the problem, data, and research contribution are stronger.
- Low-resource or resource-efficient research is attractive, although local-language research is not a priority.
- Crime-related topics may make the team uncomfortable. Avoid crime prediction, intrusive surveillance, and projects requiring direct work with criminal cases. Defensive cybersecurity may still be considered.
- Health related topics might be bad if dataset access is difficult

### Supervisor situation

- A possible supervisor has knowledge of statistics, ML, data science and computer vision.
- The supervisor may be changed depending on the selected topic.
- Topics requiring deep clinical, ecological, legal, or hardware-systems expertise should not assume that expert supervision is available.

## 3. Available Resources

- Internet connection: approximately 100 Mbps.
- Storage: approximately 1 TB.
- Devices: ordinary phones are available; cameras, drones, sensor platforms, edge boards, medical equipment, and specialised measurement hardware are not reliably available.
- University compute: uncertain. Some higher-performance computing access may be possible, but continuous access to server-grade GPUs must not be assumed.
- Existing workspace notes indicate occasional shared GPU access; the exact model, VRAM, queue availability, and job-duration limits remain unknown.
- Paid cloud-computing budget: unknown.
- Specialised university software, laboratories, and institutional datasets: unknown.

### Resource-design rule

Design around a single modest GPU, occasional shared GPU access, or cached pretrained features. Larger compute resources may be an optional extension, never a critical dependency. Prefer compact models, bounded experiments, and CPU baselines.

## 4. Data Constraints

- The team cannot undertake primary data collection for the project.
- The project must rely on existing datasets.
- Publicly downloadable datasets are preferred.
- Credentialed or restricted academic datasets may be considered only when access is predictable, legal, and obtainable early.
- There are no established partnerships with hospitals, government agencies, companies, schools, NGOs, or other data-owning organisations.
- Do not rely on questionnaires, interviews, recruited participants, user studies, expert panels, or clinician annotations.
- Do not assume access to private operational logs, bank transactions, hospital registries, security-operation-centre records, enforcement outcomes, or proprietary platform data.
- Dataset suitability must include access, licence, size, labels, metadata, representativeness, storage requirements, and reproducible splits.
- A fallback dataset or reduced-compute dataset configuration is strongly preferred.

## 5. Mandatory Topic Gates

A candidate should be rejected or substantially redesigned if any answer below is “No.”

1. Does it address a specific, evidence-supported real-world problem?
2. Is AI/ML essential to the research question?
3. Can the team train, fine-tune, or systematically adapt models rather than only call an external API?
4. Is a suitable existing dataset genuinely accessible?
5. Can the central claim be evaluated without questionnaires, participant recruitment, or unavailable experts?
6. Is there a precise research gap rather than a broad application area?
7. Does the intended contribution go beyond combining standard components into an application?
8. Can the claim be tested using objective baselines, metrics, splits, and ablations?
9. Is the work feasible within one year and preferably within a 6–8 month implementation window?
10. Can three substantial and connected individual research contributions be defined?
11. Can the core experiments run without specialised hardware or continuous server-grade GPU access?
12. Are privacy, licensing, safety, bias, and misuse risks manageable?
13. Would the project still produce academically useful findings if the proposed method does not beat the strongest baseline?

## 6. Automatic or Strong Rejection Patterns

Reject or heavily penalise topics that:

- Require inaccessible private or institutional data.
- Depend mainly on questionnaires, interviews, subjective satisfaction, or user studies.
- Require clinicians, auditors, SOC analysts, or other unavailable experts to produce ground truth.
- Require specialised hardware, a multi-GPU cluster, power meters, drones, sensors, laboratory equipment, or a real edge/cloud testbed.
- Cannot be objectively evaluated.
- Are primarily software-development, dashboard, MLOps, or integration projects.
- Are so broad that several independent research projects are hidden inside one problem statement.
- Lack a realistic training dataset or use a benchmark that does not support the real-world claim.
- Depend on live external APIs or paid services as the core model.
- Require training a foundation model from scratch.
- Use random train/test splits when the claim concerns time, geography, institution, user, device, sensor, or domain generalisation.
- Claim real-world safety or operational benefit using only a laboratory benchmark.

## 7. Preferred Shape of a Strong Proposal

- Focused real-world failure mode rather than a broad domain.
- Public, documented dataset available before proposal approval.
- Reproducible baseline can be run early on available hardware.
- Pretrained model or established architecture used as a starting point.
- Research contribution targets robustness, generalisation, efficiency, uncertainty, interpretability, or learning from limited labels.
- At least one independent or shifted test setting is available.
- Clear baseline, ablation, error analysis, and statistical comparison plan.
- A practical prototype demonstrates the research without being presented as the contribution.
- A fallback result remains publishable even if the method does not improve raw accuracy.

### Recommended default research posture

These are working assumptions, not confirmed team decisions:

- Risk: moderate — use an established task and datasets, but investigate a real methodological or evaluation gap.
- Mathematical depth: moderate — architecture, loss, training, calibration, or evaluation changes are acceptable; new theoretical proofs are not required.
- Preferred contribution dimensions: robustness, generalisation, efficiency, uncertainty, and limited-data performance.
- Preferred implementation: Python model pipeline with a lightweight web prototype where useful.
- Minimum success: competitive predictive performance plus a defensible improvement or finding in at least one targeted dimension.

## 8. Evaluation Rubric

Apply hard gates first. Score only candidates that pass.

Rate each category from 0 to 5 and calculate:

`weighted score = (rating / 5) × weight`

| Category | Weight | Meaning of a strong score |
|---|---:|---|
| Research gap and defensible novelty | 16 | Precise gap supported by literature; original and testable contribution |
| Public dataset quality and accessibility | 15 | Accessible, licensed, sufficiently large, representative, and documented |
| One-year feasibility and learning curve | 14 | Realistic scope, dependencies, skills, and contingency plan |
| Technical AI/ML depth | 12 | Substantial model-level or evaluation research rather than routine model use |
| Evaluation quality and reproducibility | 12 | Strong baselines, metrics, splits, ablations, and uncertainty analysis |
| Three-member contribution structure | 12 | Three individually assessable research questions forming one coherent project |
| Real-world significance | 9 | Important, specific, evidence-supported problem with clear stakeholders |
| Compute and storage feasibility | 5 | Fits available or predictably obtainable resources |
| Prototype feasibility | 3 | Research can be demonstrated through a bounded usable prototype |
| Ethics and responsible use | 2 | Risks are limited and can be credibly managed |
| **Total** | **100** | |

### Rating guide

- 0: absent, impossible, or incompatible.
- 1: very weak; major unresolved barriers.
- 2: weak; requires substantial redesign.
- 3: adequate but ordinary or moderately risky.
- 4: strong with manageable weaknesses.
- 5: exceptional, well supported, and low in unresolved risk.

### Suggested decision thresholds

- 85–100: excellent proposal candidate.
- 75–84: strong candidate; refine weaknesses.
- 65–74: potentially viable but needs meaningful redesign.
- Below 65: do not shortlist.
- Any failed hard gate: reject regardless of score.

A shortlisted option should normally score at least 4/5 for novelty, dataset suitability, feasibility, and three-member structure, and at least 3/5 everywhere else.

## 9. Required Experimental Standards

Every proposed project should plan for:

- Literature-backed research question and explicit hypotheses.
- At least one simple conventional baseline and one strong modern baseline.
- Leakage-safe dataset splits.
- Temporal splits for drift or forecasting claims.
- Geographic splits for remote-sensing generalisation claims.
- Institution/site splits for medical or industrial transfer claims.
- User/item cold-start splits for recommender claims.
- Cross-device or cross-capture splits for cybersecurity claims.
- Ablation studies isolating each claimed contribution.
- Error analysis by relevant condition, subgroup, object size, data quality, or domain.
- Confidence intervals, repeated runs, or another appropriate treatment of uncertainty.
- Compute, memory, and inference-cost reporting when efficiency is claimed.
- Honest limitations that distinguish benchmark evidence from deployment evidence.

## 10. Three-Person Research Structure

The project must not be divided only as “model, backend, frontend.” Each person needs a research question, method, experiment set, and defensible result.

## 12. Known Questions Still Requiring Team Input

1. Exact module dates and deliverables.
2. Whether three separate papers are formally required.
3. Exact GPU model, VRAM, access frequency, and maximum job duration.
4. Cloud/API budget.
5. Whether the final preference is still computer-vision-first or has changed.
6. Preferred modality: images only, video, satellite time series, text, audio, or multimodal.
7. Risk appetite: incremental and safe versus higher-risk novelty.
8. Comfortable mathematical depth.
9. Preferred contribution dimensions: accuracy, robustness, efficiency, generalisation, interpretability, privacy, or limited-data learning.
10. Preferred prototype type: web, mobile, desktop, or no preference.
11. Supervisor availability and domain expertise after the topic is narrowed.

