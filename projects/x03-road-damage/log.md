# X03 Road-Damage Project Log

**Project directory:** `projects/x03-road-damage/`  
**Time zone:** Asia/Colombo (UTC+05:30)

This is the ongoing record of project activity. New project files belong in this directory. Entries distinguish completed work, decisions, estimates and pending tasks; substantive research and implementation actions are recorded as they occur.

## 2026-11-07 14:52 — Project workspace initialised

**Request:** Create this log, record project activity and use this directory to store project files.

### Actions and outcomes

- Confirmed the project directory already existed and was empty before this setup.
- Created `log.md` with this initial entry.
- Created `AGENTS.md` to preserve the storage and logging instructions for future work in this directory.
- Established this directory as the root for new project notes, code, notebooks, configurations, manifests, experimental outputs and deliverables.
- Verified that both files exist and contain the requested initial setup.

### Starting research state

- The current plan is based on proposal v8: A investigates short-side-relative assignment and weighting; B investigates small/thin-object scale consistency; C trains a separate neural model to predict likely missed-damage locations.
- These are proposed studies. The need for the interventions and their benefits have not been demonstrated locally.
- The next research milestone is a source-only YOLO11 baseline pilot to diagnose remaining weaknesses and measure training time, memory and evaluation behaviour.
- The latest discovery report records unresolved novelty, compute and development-trial accounting issues. Previous compute figures are estimates, not hardware benchmarks.
- This setup performed no model training, dataset download or new literature verification.

### Existing reference material

- [Current X03 discovery report](../../research-discovery/reports/gaps/x03-road-damage.md)
- [Team and module criteria](../../research-module-and-team-criteria.md)
- [Proposal v8 text extraction](../../tmp/proposal/Road-Damage-Research-Proposal-v8.txt)

Earlier project documents remain at their existing locations. This initial entry summarises the starting state; it is not a reconstructed action-by-action history of earlier sessions.

### Next steps

- Store subsequent X03 project files beneath this directory and append activity entries to this log.
- When authorised to begin the pilot, record the data/split manifests, package versions, training settings, runtime measurements, saved outputs and interpretation.

## 2026-11-07 — Kaggle implementation started

- Execution authorised, including private Kaggle jobs and suitable local Git commits; no remote push requested.
- Verified Kaggle CLI 2.2.5 using `python -m kaggle`. PATH lacks a direct kaggle command. Restricted-network DNS failed previously; network-enabled CLI authenticated as rashmithachamikara.
- Git started clean at 76850dd. Inspected dataset mirrors; selected author-hosted country ZIPs rather than converted mirrors. Source: sekilab/RoadDamageDetector README, country-specific RDD2022 S3 URLs.
- Added CPU preparation and notebook builder: India/Czech/United States only; original XML conversion, checksums, quarantine, conservative duplicate grouping, frozen source splits and US holdout. Japan untouched.
- Duplicate candidates are grouped conservatively (dHash distance <=3); this is not certified duplicate detection. No reliable sequence metadata is assumed. VOC coordinate convention is recorded explicitly.
- Planned run order: CPU preparation, GPU smoke/recovery, full baseline, evaluation/diagnostics. No training result yet.

## 2026-11-07 — Preparation v1 failure and official-source recovery

- Preparation v1 ended with S3 HTTP 403. Its initial shell-style notebook cell did not propagate failure to Kaggle status; corrected all notebooks to checked subprocess calls. Inspected log rather than trusting COMPLETE alone.
- Verified official Figshare article 21431547/file 38030910 is reachable with HTTP 206 byte ranges. Changed preparation to read only the India/Czech/United States nested country ZIPs from the official archive; no Japan extraction or image access.
- Local validation: six focused metric/conversion unit tests passed with bundled Python; all Python modules compile. Added stock training, smoke interruption/recovery, matching/threshold/geometry evaluation, conservative group bootstrap, A/B/C diagnostics and README. GPU API compatibility remains to be checked by smoke.

## 2026-11-07 — Official ZIP member layout verified

- Local ranged ZIP inspection found nested members Czech.zip, India.zip and United_States.zip (without RDD2022_ prefixes). Corrected lookup and launched preparation v3 after v2 error. Neither failure used a GPU.
- Local bundled Python lacks requests; used system Python for the independent archive-layout check. This is environment validation, not an experiment result.

## 2026-11-07 — Figshare signature expiry corrected

- Preparation v3 reached the correct India ZIP but Figshare signed redirects expired after ten seconds. Changed range reader to obtain a fresh redirect for every range; v4 launched. All failed preparation jobs were CPU-only.
- Inspected pinned Ultralytics TaskAlignedAssigner source: forward accepts extra keyword tensors. Diagnostic wrapper now preserves them and explicitly moves the separate diagnostic model to CUDA.

- **2026-11-07 15:19:54 Asia/Colombo** — rashmithachamikara/x03-road-prepare has status "KernelWorkerStatus.RUNNING"


- **2026-11-07 15:21:05 Asia/Colombo** — Corrected hand-written implementation subsection headings to date-only: earlier clock times were inaccurate. Controller entries use actual system timestamps. Added source-learning-curve diagnostic to final report generation.

- **2026-11-07 15:22:24 Asia/Colombo** — Finalised A diagnostic sampling at 128 deterministic source-training images per country (up to 256), preserving original GT geometry before assignment. Report generation includes late source-selection mAP improvement; local tests and notebook JSON checks passed. Preparation v4 remains CPU-only and running.

- **2026-11-07 15:25:16 Asia/Colombo** — rashmithachamikara/x03-road-prepare has status "KernelWorkerStatus.COMPLETE"

- **2026-11-07 15:25:16 Asia/Colombo** — Command: `python -m kaggle kernels output rashmithachamikara/x03-road-prepare -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\artifacts\prepare --file-pattern .*(json|jpg|log|csv|yaml)$`

- **2026-11-07 15:25:24 Asia/Colombo** — Preparation audit: {"India": {"train": 5220, "selection": 653, "source_audit": 653, "excluded_overlap": 124}, "Czech": {"train": 2263, "source_audit": 283, "selection": 283}, "United_States": {"unseen": 4805}}

- **2026-11-07 15:25:24 Asia/Colombo** — Command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\kaggle\smoke --accelerator NvidiaTeslaT4 -t 43200`

- **2026-11-07 15:25:27 Asia/Colombo** — Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-road-smoke

- **2026-11-07 15:25:28 Asia/Colombo** — rashmithachamikara/x03-road-smoke has status "KernelWorkerStatus.QUEUED"

- **2026-11-07 15:26:02 Asia/Colombo** — rashmithachamikara/x03-road-smoke has status "KernelWorkerStatus.RUNNING"

- **2026-11-07 15:26:18 Asia/Colombo** — Inspected preparation v4 audit and India conversion overlay. Detected overly strict preprocessing: 1,056 Indian images containing out-of-scope D01/D11/D43/D44/D50 labels had been excluded. Corrected policy to retain images and their four target classes, treating genuine other classes as outside the task; malformed target-like spelling remains quarantined. Stopped only local pipeline controller to gate full training. Smoke v1 is execution-only and uses the earlier subset; it must not supply scientific results. Launching preparation v5.

- **2026-11-07 15:28:34 Asia/Colombo** — Smoke v1 passed on Tesla T4 (~14.56 GiB reported VRAM), YOLO11s batch16, Ultralytics8.4.192, torch2.11.0+cu130/Python3.13.16. Deliberate epoch-zero interruption resumed at epoch1 with 255 optimizer-state entries restored. No OOM fallback. This was the earlier filtered-data execution test, not a scientific result. Inspected India/Czech conversion sheets; boxes appear aligned with road damage at preview scale. Windows CLI live-log encoding required PYTHONIOENCODING=utf-8; controller now sets it. Corrected preparation v5 pending before repeat smoke/main.

- **2026-11-07 15:28:38 Asia/Colombo** — rashmithachamikara/x03-road-prepare has status "KernelWorkerStatus.RUNNING"

- **2026-11-07 15:31:03 Asia/Colombo** — Added paired per-GT 640/320 detection transition counts for all, small/thin and B-eligible populations; C feature probe asserts expected P3/P4 spatial sizes. Controller remains gated on corrected preparation, with scientific training not yet launched.

- **2026-11-07 15:35:27 Asia/Colombo** — Fixed all evaluation/prediction calls to square letterbox (rect=False), ensuring consistent 640/320 geometry and C grid coordinates across countries. Updated README with Figshare fallback and retained out-of-scope-label policy.

- **2026-11-07 15:36:32 Asia/Colombo** — Added explicit per-class precision/recall/sparse-support fields and reran six local tests (all passed), compile and whitespace checks. Moved A diagnostics into evaluation so diagnostic API failures cannot change the status of a successfully completed training job or trigger retraining.

- **2026-11-07 15:39:58 Asia/Colombo** — Preparation v5 log reports corrected counts: India train6001/selection751/audit750/excluded-overlap203; Czech train2263/selection283/audit283; US4805 unseen. Exactly one Indian image remains quarantined (unrecognised D0w0 spelling). Original archive hashes match v4; scientific pilot must use v5. Effective fit8264/selection1034/audit1033. No Japan image access.

- **2026-11-07 15:40:39 Asia/Colombo** — rashmithachamikara/x03-road-prepare has status "KernelWorkerStatus.COMPLETE"

- **2026-11-07 15:40:39 Asia/Colombo** — Command: `python -m kaggle kernels output rashmithachamikara/x03-road-prepare -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\artifacts\prepare --file-pattern .*(json|jpg|log|csv|yaml)$`

- **2026-11-07 15:40:53 Asia/Colombo** — Preparation audit: {"India": {"source_audit": 750, "selection": 751, "train": 6001, "excluded_overlap": 203}, "Czech": {"selection": 283, "train": 2263, "source_audit": 283}, "United_States": {"unseen": 4805}}

- **2026-11-07 15:40:53 Asia/Colombo** — Command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\kaggle\smoke --accelerator NvidiaTeslaT4 -t 43200`

- **2026-11-07 15:40:59 Asia/Colombo** — Kernel version 2 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-road-smoke

- **2026-11-07 15:41:03 Asia/Colombo** — rashmithachamikara/x03-road-smoke has status "KernelWorkerStatus.RUNNING"

- **2026-11-07 15:42:00 Asia/Colombo** — Independently validated v5 manifest locally: unique IDs, allowed countries/classes, normalized box bounds, group disjointness, split/country class and geometry counts; saved runs/manifest-validation.json with manifest SHA256. Repeat GPU smoke v2 running on corrected artifact.

- **2026-11-07 15:42:39 Asia/Colombo** — Inventory finding: fixed small/thin union has392 training labels,43 selection labels,70 source-audit labels and528 US labels. All union labels meet B's >=8px reference short-side visibility mask. Source audit India D10 has only3 labels. US contains no empty four-class annotations, while source splits have many; raw source/US metrics are confounded by prevalence/difficulty. Added class composition of small/thin labels to inventory; no geometry thresholds changed.

- **2026-11-07 15:43:50 Asia/Colombo** — Important support limitation:349/392 small/thin training boxes are potholes; only43 are cracks. Source-audit subgroup is63 potholes and7 longitudinal cracks, with no transverse/alligator instances. US subgroup has293 longitudinal/150 transverse/2 alligator/83 potholes. Added class-by-geometry recall/support to evaluation and explicit report caveat: aggregate small/thin performance cannot establish small-crack performance. No bins or training methods changed.

- **2026-11-07 15:44:24 Asia/Colombo** — rashmithachamikara/x03-road-smoke has status "KernelWorkerStatus.COMPLETE"

- **2026-11-07 15:44:24 Asia/Colombo** — Command: `python -m kaggle kernels output rashmithachamikara/x03-road-smoke -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\artifacts\smoke --file-pattern .*`

- **2026-11-07 15:45:05 Asia/Colombo** — Checked pinned loss API: a reloaded detector can have dict model.args, while loss hyperparameters use attribute access. Diagnostic converts arguments with the pinned get_cfg helper before loss construction. No detector weights or scientific training settings changed.

- **2026-11-07 15:48:59 Asia/Colombo** — Repeat smoke v2 completed successfully: YOLO11s batch16; optimizer recovery verified. Optional epoch0 optimizer checkpoint download stalled locally at zero bytes for several minutes after required JSON/CSV results downloaded. Stopped only controller/download processes; remote job unaffected. Restricted future smoke downloads to records, and full training downloads to records plus best/last checkpoints (periodic checkpoints remain on Kaggle). Independently inspected required smoke/manifest artifacts; preparing project-scoped implementation commit before starting full training.

- **2026-11-07 15:49:19 Asia/Colombo** — Created local implementation commit9c5096f after six passing tests, compile/whitespace checks, corrected preparation audit and successful GPU recovery smoke. No remote Git push. Starting private full baseline from COCO (not smoke weights), YOLO11s640 batch16 seed42 50epochs, source-only selection, preparationv5/smokev2.

- **2026-11-07 15:49:19 Asia/Colombo** — Command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\kaggle\train --accelerator NvidiaTeslaT4 -t 43200`

- **2026-11-07 15:49:24 Asia/Colombo** — Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-road-train

- **2026-11-07 15:49:27 Asia/Colombo** — rashmithachamikara/x03-road-train has status "KernelWorkerStatus.QUEUED"

- **2026-11-07 15:52:06 Asia/Colombo** — Full training v1 is queued. Live-log stream returned Kaggle HTTP500 before worker startup; status polling continues and no duplicate job was submitted. This is monitoring/backend availability, not a model-training failure.

- **2026-11-07 15:54:07 Asia/Colombo** — Added controller --monitor attachment mode and bounded transient status retries for future restarts, preventing duplicate remote runs if local monitoring/network fails. Existing controller remains attached to trainingv1; no resubmission. Compile check passed.

- **2026-11-07 15:57:51 Asia/Colombo** — Added exact integer LetterBox padding to C grid mapping (rather than fractional approximation) and a boundary/padding unit test. Seven tests pass. Trainingv1 is immutable and remains queued; this evaluation-only coordinate fix does not affect detector training or thresholds.

- **2026-11-07 16:01:03 Asia/Colombo** — Detailed Kaggle session API confirms trainingv1 status QUEUED with failure_message=None. No quota/failure reason reported. Retaining the single submitted run and continuing monitoring; queue time is not measured training time.

- **2026-11-07 16:04:31 Asia/Colombo** — Pipeline stopped: Cannot query train: HTTPSConnectionPool(host='api.kaggle.com', port=443): Max retries exceeded with url: /v1/kernels.KernelsApiService/GetKernelSessionStatus (Caused by NameResolutionError("HTTPSConnection(host='api.kaggle.com', port=443): Failed to resolve 'api.kaggle.com' ([Errno 11001] getaddrinfo failed)"))


- **2026-11-07 16:05:14 Asia/Colombo** — rashmithachamikara/x03-road-train has status "KernelWorkerStatus.RUNNING"

- **2026-11-07 16:05:35 Asia/Colombo** — Original controller stopped on transient DNS failure while trainingv1 remained remote. Reattached with run_pipeline.py train --monitor; session API now reports RUNNING. No new training version or duplicate run submitted.

- **2026-11-07 16:10:14 Asia/Colombo** — Training log confirms pinned stock auto-optimizer resolved to AdamW(lr0.00125,momentum0.9); this is recorded rather than assuming SGD. No corrupt-image/duplicate-label removal warnings found; independent manifest check found zero exact duplicate annotation rows. First epoch completed and epoch2 started; live displayed GPU memory about5.02G, final peak measurement pending.

- **2026-11-07 16:11:39 Asia/Colombo** — Renamed inspected mirror metadata to runs/unused-mirror-metadata.json to avoid confusing its claimed licence with the official Figshare data actually used. Retained the discovery record; no mirror images or annotations used.

- **2026-11-07 16:14:30 Asia/Colombo** — Before any audit/US model outcomes, added positive-only and negative-only operational metric stratification using the same frozen predictions/threshold. Motivation is the inventory's source-vs-US negative-image imbalance; primary all-image results and AP remain unchanged. No extra training or threshold tuning.

- **2026-11-07 16:17:52 Asia/Colombo** — Report generator now documents prediction-overlay colours and deterministic example sampling. Monitoring continues on the original trainingv1; no audit/US predictions have been generated or inspected.

- **2026-11-07 16:20:02 Asia/Colombo** — Clarified A diagnostic as post-training frozen-best float32 supervision, not actual training-trajectory assignments. Evaluation will hash the initial COCO asset retained in the immutable training output and record the observed v8.4.0 asset URL. Trainingv1 configuration remains unchanged.

- **2026-11-07 16:24:10 Asia/Colombo** — Report explicitly defines operational misses (same-class, source-thresholded, IoU>=0.5), including low-confidence/wrong-class/localisation failures rather than claiming every unmatched label is visually undetected. Detector training continues unchanged.

- **2026-11-07 16:25:45 Asia/Colombo** — Refined report's full-grid estimate to separate measured pilot-size runtime from explicitly assumed linear scaling to final-fold image counts. B multiplier/development/C budgets remain unmeasured assumptions; no rental or additional model experiments launched.

- **2026-11-07 16:27:27 Asia/Colombo** — Evaluation now retains source-selection predictions and selected image IDs alongside the threshold/grid, with an explicit India/Czech-only assertion. This makes threshold provenance independently reproducible; no thresholds are chosen from US or source-audit data.

- **2026-11-07 16:28:47 Asia/Colombo** — Creating local project-scoped commit: Harden X03 monitoring and preserve evaluation provenance

- **2026-11-07 16:42:30 Asia/Colombo** — Training progress monitor: original v1 remains RUNNING, roughly five batches/second with stable live memory ~5.02G. No OOM/model fallback, no source-audit/US scoring, and no training hyperparameter changes. Full live log retained under artifacts/train-live.txt; final timing/peak will come from saved JSON.

- **2026-11-07 16:50:40 Asia/Colombo** — Added derived small/thin shares of labels and operational misses, before any held-out predictions, to distinguish targeted small-object difficulty from the dominant total-error population. No additional inference, threshold changes or training modifications. Seven metric tests pass.

- **2026-11-07 16:53:56 Asia/Colombo** — Added measured peak allocated/reserved GPU memory and median post-warm-up epoch time to report generation, using saved timing JSON and deduplicated epoch callbacks. These will be T4 measurements, not assumed RTX4050 timings. Scientific training remains unchanged.

- **2026-11-07 17:03:23 Asia/Colombo** — Added independent local result-artifact verification before report generation/automatic results commit: frozen manifest hash, completed configuration, downloaded checkpoint SHA256s, source-only threshold IDs, complete two-scale prediction coverage, finite outputs and nonempty A diagnostics. Checker has compiled; outcome is pending actual artifacts, not yet marked passed.

- **2026-11-07 17:04:18 Asia/Colombo** — Corrected prediction input batching before evaluation: use a text file of image paths rather than an in-memory Python list, so Ultralytics streams batches of8 instead of potentially decoding the whole country into one memory batch. This is an execution/memory fix; model, scores, thresholds and data roles are unchanged.

- **2026-11-07 17:07:56 Asia/Colombo** — Verified pinned prediction source code: check_source lists are autocast to PIL/numpy, whereas LoadImagesAndVideos accepts a text manifest and requested batch size. Streaming fix is grounded in the actual pinned API. Training continues on original v1 without changes.

- **2026-11-07 17:27:40 Asia/Colombo** — Prediction outputs will be gzip-compressed for transfer (motivated by the earlier large optional-checkpoint download stall). Local verifier expands them to readable JSON before coverage/hash checks. No prediction content or metric definition changes; code compiles, end-to-end artifact verification remains pending.

- **2026-11-07 17:36:09 Asia/Colombo** — Artifact verifier additionally requires the actual training CSV to contain50 epochs ending at epoch50, independently of the completion metadata. Source-only scientific settings remain fixed; final model evaluation is pending.

- **2026-11-07 17:38:20 Asia/Colombo** — rashmithachamikara/x03-road-train has status "KernelWorkerStatus.COMPLETE"

- **2026-11-07 17:38:20 Asia/Colombo** — Command: `python -m kaggle kernels output rashmithachamikara/x03-road-train -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\artifacts\train --file-pattern .*(json|csv|yaml|log|txt)$|(^|/)(best|last)[.]pt$`

- **2026-11-07 17:39:00 Asia/Colombo** — Training outcome: {
  "status": "complete",
  "epochs": 50,
  "model": "yolo11s.pt",
  "batch": 16,
  "seconds": 5501.348426818848
}

- **2026-11-07 17:39:00 Asia/Colombo** — Command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\kaggle\evaluate --accelerator NvidiaTeslaT4 -t 43200`

- **2026-11-07 17:39:08 Asia/Colombo** — Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-road-evaluate

- **2026-11-07 17:39:09 Asia/Colombo** — rashmithachamikara/x03-road-evaluate has status "KernelWorkerStatus.QUEUED"

- **2026-11-07 17:41:11 Asia/Colombo** — Independently checked completed training artifacts:50 actual CSV epochs;5501.35 seconds (1.528h); peak allocated3.741GiB/reserved5.021GiB; median post-warm-up epoch109.12s. Best source-selection mAP50:95=.15964 at epoch48; last10 best gain=.00226 (source-selection metrics, not independent evaluation). Downloaded best/last SHA256s match saved hashes. Saved runs/training-measurements.json. Evaluationv1 queued; independent source-audit/US metrics not yet available.

- **2026-11-07 17:49:26 Asia/Colombo** — rashmithachamikara/x03-road-evaluate has status "KernelWorkerStatus.RUNNING"

- **2026-11-07 17:57:20 Asia/Colombo** — Evaluationv1 computed country AP/predictions/diagnostics but failed at its final C feature-shape probe with KeyError16: hooks were attached to a different model object than the predictor backend executed after validation. Training/checkpoint validity unaffected. Fixed probe to use a separately loaded frozen float32 model and direct forward on a source-selection image. Added summary persistence before the probe. This is instrumentation-only recovery after outcomes became visible: no retraining, threshold-rule change, bin change or target tuning. Evaluationv2 will reuse the exact trained checkpoint and protocol.

- **2026-11-07 17:57:38 Asia/Colombo** — rashmithachamikara/x03-road-evaluate has status "KernelWorkerStatus.ERROR"

- **2026-11-07 17:57:38 Asia/Colombo** — Command: `python -m kaggle kernels output rashmithachamikara/x03-road-evaluate -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\artifacts\evaluate --file-pattern .*log$`

- **2026-11-07 18:39:44 Asia/Colombo** — Pipeline stopped: evaluate failed; inspect downloaded log before retrying

- **2026-11-07 19:27:55 Asia/Colombo** — User requested continuation. Previous recovery launch was not executed: automatic approval review failed on account usage limit, with retry time19:24; not an unsafe-action determination. Current time is after that retry window. Original controller has stopped on evaluationv1 ERROR. Fixed direct feature probe/finally cleanup are present locally; rebuilt notebooks and compiled modules; seven tests passed. Resuming evaluation only, using unchanged trainingv1/preparationv5 and frozen protocol.

- **2026-11-07 19:28:02 Asia/Colombo** — Command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\kaggle\evaluate --accelerator NvidiaTeslaT4 -t 43200`

- **2026-11-07 19:28:08 Asia/Colombo** — Kernel version 2 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-road-evaluate

- **2026-11-07 19:28:12 Asia/Colombo** — rashmithachamikara/x03-road-evaluate has status "KernelWorkerStatus.QUEUED"

- **2026-11-07 19:29:12 Asia/Colombo** — Creating local project-scoped commit: Fix X03 feature probe and verify downloaded pilot artifacts

- **2026-11-07 19:49:08 Asia/Colombo** — Investigated long evaluation queue through documented installed SDK quota_view API:30.0 GPU hours allowed,1.69344 used,0 reserved, paid scaling disabled; reset2026-11-14 UTC. Saved runs/kaggle-quota-check.json. Quota exhaustion is not indicated; exact scheduler cause remains unreported. No billing/resource settings changed or duplicate run submitted.

- **2026-11-07 19:51:27 Asia/Colombo** — rashmithachamikara/x03-road-evaluate has status "KernelWorkerStatus.RUNNING"

- **2026-11-07 19:57:14 Asia/Colombo** — rashmithachamikara/x03-road-evaluate has status "KernelWorkerStatus.COMPLETE"

- **2026-11-07 19:57:14 Asia/Colombo** — Command: `python -m kaggle kernels output rashmithachamikara/x03-road-evaluate -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\artifacts\evaluate --file-pattern .*`

- **2026-11-07 19:59:51 Asia/Colombo** — Evaluation complete; wrote pilot-report.md and runs/summary.json. Results are one-seed development evidence.

- **2026-11-07 19:59:51 Asia/Colombo** — Creating local project-scoped commit: Record X03 Kaggle baseline pilot results and diagnostics

- **2026-11-07 20:08:10 Asia/Colombo** — Evaluationv2 succeeded, including P3[1,128,80,80]/P4[1,256,40,40]. Full artifact checks passed. Final audit found float cancellation at exact geometry cutoffs: canonicalised sides to six decimal pixels and recomputed only diagnostic metrics from immutable saved predictions. Czech target count9->8; US549->528, matching frozen inventory. Original summary preserved in artifacts; recompute script/geometry-correction.json retained. AP, all-object P/R/FP, predictions and weights unchanged; added inventory-consistency assertion and boundary test (8 tests pass). Corrected C positive cells48 India/8 Czech/502 US. Compressed-file decoding, complete prediction coverage, checkpoint hashes and source-only threshold IDs verified. Reviewed two US overlays and one India overlay: boxes align; examples illustrate missed cracks and a matched longitudinal box, not error frequencies. Added evidence-bounded A/B/C decisions; condensed tracked summary while full per-image metrics remain in artifacts.

- **2026-11-07 20:09:10 Asia/Colombo** — Creating local project-scoped commit: Correct geometry boundary accounting and interpret pilot results

- **2026-11-08 12:50:23 Asia/Colombo** — B prototype implementation authorised: fresh baseline/generic/small-thin arms,50 epochs each,seed42,COCO initialization, unchanged preparation manifest and source-only tuning; Japan untouched. Creating all new B assets under b-prototype. Budget gate8–12T4 GPU-hours to be checked after smoke; no full runs launched yet.

- **2026-11-08 13:07:27 Asia/Colombo** — Implemented B core: standard DetectionTrainer/EMA, differentiable half-view consistency, detached stock TAL/top3 weighting, Bernoulli KL+normalized L1, one scalar added once to stock3-component loss, augmented geometry masks and per-epoch telemetry. Added immutable experiment config and separate private Kaggle stages. Local isolated venv needed pip-bootstrap workaround and matching torchvision0.27 for existing CPU Torch2.12 (no global Torch change). Nine substantive CPU tests passed, including actual TAL/DFL gradients and empty batches; earlier missing/incompatible dependency checks were environment failures. CUDA smoke still pending. Added common-batch refusal of stock silent shrink, source-only subset/recovery checks, lazy prediction transfer, budget gate based on warm batch medians. Snapshot quota~1h47used/30, no reservation/paid scaling.

- **2026-11-08 13:13:09 Asia/Colombo** — B smokev1 trained/resumed the baseline but failed telemetry assertion: the pinned trainer emits an additional final-validation callback at epochs+1. Actual recovery was correct; excluded this non-training callback from timing/epoch accounting and added a regression test. No full runs launched. GPU consistency/recovery/export/budget checks still pending; rerunning the same smoke protocol with instrumentation fix.

- **2026-11-08 13:14:37 Asia/Colombo** — rashmithachamikara/x03-b-smoke has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 13:16:06 Asia/Colombo** — Ten local CPU tests now pass with compatible Torch2.12/TorchVision0.27. Added true TAL+DFL consistency-gradient test, teacher detach/empty-GT cases, scalar-loss scaling and final-validation callback regression. Implemented sequential budget-gated controller, all-model source-only threshold freeze, independent checkpoint/data-role/coverage checks, paired group-bootstrap reporting and fixed-hash overlay samples. Source references are retained locally (ignored) with URL/SHA manifest. Smokev2 monitoring active; full launches remain gated.

- **2026-11-08 13:16:50 Asia/Colombo** — rashmithachamikara/x03-b-smoke has status "KernelWorkerStatus.COMPLETE"

- **2026-11-08 13:16:50 Asia/Colombo** — B command: `python -m kaggle kernels output rashmithachamikara/x03-b-smoke -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\artifacts\smoke --file-pattern .*(json|log|yaml|csv|txt)$`

- **2026-11-08 13:17:27 Asia/Colombo** — B smoke/recovery passed; budget projection 9.256253278169455h, common batch16

- **2026-11-08 13:17:27 Asia/Colombo** — Creating local project-scoped commit: Add validated B consistency prototype and budget-gated Kaggle runner

- **2026-11-08 13:17:28 Asia/Colombo** — B command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\kaggle\baseline --accelerator NvidiaTeslaT4 -t 21600`

- **2026-11-08 13:17:32 Asia/Colombo** — Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-b-baseline

- **2026-11-08 13:17:35 Asia/Colombo** — rashmithachamikara/x03-b-baseline has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 13:23:01 Asia/Colombo** — Strengthened post-training artifacts without changing any training recipe: select now verifies native-versus-export predictions on three source-selection images per arm; select/evaluate measure session time/memory/storage. Local report now includes common-threshold results, class supports, missed-damage frequency, paired matched-GT gains/losses, and usable/skip/resource details. Rebuilt select/evaluate notebooks only; syntax and a controlled paired-transition check passed. Full baseline continues unchanged.

- **2026-11-08 13:24:50 Asia/Colombo** — Creating local project-scoped commit: Strengthen B export parity and paired diagnostic reporting

- **2026-11-08 13:25:03 Asia/Colombo** — Project-scoped reporting commit initially blocked by sandbox read-only .git/index permissions; retrying the same authorized local commit with filesystem escalation.

- **2026-11-08 13:25:03 Asia/Colombo** — Creating local project-scoped commit: Strengthen B export parity and paired diagnostic reporting

- **2026-11-08 13:35:04 Asia/Colombo** — User requested background status/handoff. Current measured progress: baseline epoch 9/50. Smokev2 passed at common batch16; projected total9.256T4h. Local controller control.py smoke --monitor remains running (exec session90126), sequencing baseline -> generic -> small-thin -> select -> evaluate, with report and project-only local commit on completion. Kaggle current job https://www.kaggle.com/code/rashmithachamikara/x03-b-baseline (v1). Stopped only the chat-side periodic progress polling cell; did not cancel Kaggle or the local controller. Next return: inspect runs/*-status.txt, main log and any report/verification.json; reattach monitor-only if necessary, avoid duplicate submissions. Laptop must stay awake and online for local controller to submit subsequent jobs/download results; a submitted Kaggle job runs in cloud independently.

- **2026-11-08 15:22:38 Asia/Colombo** — B baseline status-query failure1/5

- **2026-11-08 15:23:11 Asia/Colombo** — rashmithachamikara/x03-b-baseline has status "KernelWorkerStatus.COMPLETE"

- **2026-11-08 15:23:11 Asia/Colombo** — B command: `python -m kaggle kernels output rashmithachamikara/x03-b-baseline -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\artifacts\baseline --file-pattern .*(json|gz|csv|yaml|log|txt)$|.*-best[.]pt$`

- **2026-11-08 15:23:43 Asia/Colombo** — B command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\kaggle\generic --accelerator NvidiaTeslaT4 -t 21600`

- **2026-11-08 15:23:46 Asia/Colombo** — Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-b-generic

- **2026-11-08 15:23:47 Asia/Colombo** — rashmithachamikara/x03-b-generic has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 15:31:24 Asia/Colombo** — Resumed active B task without duplicate submission. Fresh baseline v1 completed and downloaded; verified50 CSV/timing epochs and exported checkpoint SHA256. Measured baseline verification: {"baseline_hours": 1.5905905644394445, "best_epoch": "48", "source_selection_map95": 0.15964, "peak_allocated_gib": 3.7410635948181152, "peak_reserved_gib": 5.021484375, "updated_budget_projection_hours": 9.592209139394697, "checkpoint_sha256": "d18a52a1f32ff23a4e3c5cb66a4f38c801f3f3daa41976503a68fc858a3ffd75"}. Generic consistency v1 already running under original controller (session90126). No source-audit or US results opened; all thresholds remain to be selected jointly after all training.

- **2026-11-08 15:37:33 Asia/Colombo** — Additional baseline reproducibility check against historical training CSV: {"epochs": [50, 50], "differing_epoch_counts": {"epoch": 0, "train/box_loss": 0, "train/cls_loss": 0, "train/dfl_loss": 0, "metrics/precision(B)": 0, "metrics/recall(B)": 0, "metrics/mAP50(B)": 0, "metrics/mAP50-95(B)": 0, "val/box_loss": 0, "val/cls_loss": 0, "val/dfl_loss": 0, "lr/pg0": 0, "lr/pg1": 0, "lr/pg2": 0}}. Comparison excludes runtime; this is a repeated seed/recipe, not independent research evidence.

- **2026-11-08 15:44:19 Asia/Colombo** — Added post-run validation of every consistency telemetry row: finite supervised/auxiliary losses, exact five-epoch ramp, complete50-epoch batch coverage, EMA-update continuity, skip/class-count reconciliation, and comparison of augmented geometry populations. Also requires source-image export parity records and50 timing epochs per arm before final report verification passes. Syntax check passed; actual telemetry checks await completed consistency jobs.

- **2026-11-08 16:08:21 Asia/Colombo** — User stopping rule: complete the authorized B prototype successfully, verify/save artifacts and report, commit locally, then stop. Further research experiments or follow-up interventions await the user. Current stage remains generic-consistency v1; no scope expansion.

- **2026-11-08 16:10:26 Asia/Colombo** — User clarified: do not actively monitor long background jobs. Ended chat-side periodic polling (cell56) and optional generic live-log viewer only (PID24760). Left the submitted Kaggle generic job and original background executor control.py smoke --monitor running so the authorized remaining stages can proceed. Returning control now; on next user message inspect existing status/artifacts before any new submission. No new experiments authorized beyond the agreed comparison.

- **2026-11-08 17:49:37 Asia/Colombo** — rashmithachamikara/x03-b-generic has status "KernelWorkerStatus.COMPLETE"

- **2026-11-08 17:49:37 Asia/Colombo** — B command: `python -m kaggle kernels output rashmithachamikara/x03-b-generic -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\artifacts\generic --file-pattern .*(json|gz|csv|yaml|log|txt)$|.*-best[.]pt$`

- **2026-11-08 17:51:21 Asia/Colombo** — B command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\kaggle\small-thin --accelerator NvidiaTeslaT4 -t 21600`

- **2026-11-08 17:51:26 Asia/Colombo** — Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-b-small-thin

- **2026-11-08 17:51:33 Asia/Colombo** — rashmithachamikara/x03-b-small-thin has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 19:14:12 Asia/Colombo** — B small-thin status-query failure1/5

- **2026-11-08 20:03:37 Asia/Colombo** — Single status check on user return: generic v1 complete; small-thin v1 still RUNNING on Kaggle. Previous local executor process/session no longer exists (no matching python control.py process); no job was resubmitted. Verified generic50-epoch history, checkpoint hash and all consistency telemetry. {"status": "passed", "hours": 2.393133352526667, "source_selection_best_map95": 0.15155, "peak_reserved_gib": 6.228515625, "telemetry": {"batches": 25850, "ema_updates": 6828, "counts": {"total": 476690, "visible": 472441, "target": 74951, "selected": 472441, "usable": 471037, "skip_no_positive": 1375, "skip_zero_weight": 29}}, "checkpoint_sha256": "3d37d005045c69f60a950473014c269f906a8bd6524f516cd7c6e76e0b1d567f"}. Source-audit/US outcomes remain unopened.

- **2026-11-08 20:04:16 Asia/Colombo** — Restored the authorized background executor as a detached hidden Windows process: control.py small-thin --monitor. It reattaches the existing cloud job, then downloads, selects thresholds, evaluates and commits; no training job duplication. PID and stdout/stderr paths recorded in b-prototype/runs/controller-resume.json. Per user preference, ending active monitoring after launch verification.

- **2026-11-08 20:04:25 Asia/Colombo** — rashmithachamikara/x03-b-small-thin has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 20:05:12 Asia/Colombo** — rashmithachamikara/x03-b-small-thin has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 20:05:32 Asia/Colombo** — Launch verification found that Windows/tool shell cleanup ended the detached PID10532 after its initial status query; it is not the active executor. Reattached the same existing small-thin Kaggle job via persistent exec session55449 instead (control.py small-thin --monitor). No job resubmission. Cloud training is independent; local sequencing depends on this execution session remaining alive and will require reattachment if the app/runtime closes. Stopping active checking now, as requested.

- **2026-11-08 20:08:29 Asia/Colombo** — User requested current running stage; performed one snapshot (no follow/watch). Baseline and generic COMPLETE; focused B Kaggle job RUNNING, latest logged epoch unavailable. Source-selection and final evaluation not yet started.

- **2026-11-08 20:14:20 Asia/Colombo** — User explicitly resumed active monitoring. Attached to existing executor session55449 and focused-B cloud job; continuing through the already authorized selection/evaluation/report verification, then stopping. No new training submission or scope expansion.

- **2026-11-08 20:20:26 Asia/Colombo** — rashmithachamikara/x03-b-small-thin has status "KernelWorkerStatus.COMPLETE"

- **2026-11-08 20:20:26 Asia/Colombo** — B command: `python -m kaggle kernels output rashmithachamikara/x03-b-small-thin -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\artifacts\small-thin --file-pattern .*(json|gz|csv|yaml|log|txt)$|.*-best[.]pt$`

- **2026-11-08 20:20:57 Asia/Colombo** — rashmithachamikara/x03-b-small-thin has status "KernelWorkerStatus.COMPLETE"

- **2026-11-08 20:20:57 Asia/Colombo** — B command: `python -m kaggle kernels output rashmithachamikara/x03-b-small-thin -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\artifacts\small-thin --file-pattern .*(json|gz|csv|yaml|log|txt)$|.*-best[.]pt$`

- **2026-11-08 20:21:15 Asia/Colombo** — B command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\kaggle\select --accelerator NvidiaTeslaT4 -t 7200`

- **2026-11-08 20:21:23 Asia/Colombo** — Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-b-select

- **2026-11-08 20:21:27 Asia/Colombo** — rashmithachamikara/x03-b-select has status "KernelWorkerStatus.QUEUED"

- **2026-11-08 20:21:31 Asia/Colombo** — B command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\kaggle\select --accelerator NvidiaTeslaT4 -t 7200`

- **2026-11-08 20:21:36 Asia/Colombo** — Kernel version 2 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-b-select

- **2026-11-08 20:21:39 Asia/Colombo** — rashmithachamikara/x03-b-select has status "KernelWorkerStatus.QUEUED"

- **2026-11-08 20:21:52 Asia/Colombo** — Focused B v1 completed50epochs; downloaded checkpoint/config/history/telemetry. SHA256 and all25850 consistency rows passed post-run validation. {"status": "passed", "hours": 2.452676812863055, "source_selection_best_map95": 0.15346, "peak_reserved_gib": 6.228515625, "telemetry": {"batches": 25850, "ema_updates": 6828, "counts": {"total": 476690, "visible": 472441, "target": 74951, "selected": 74951, "usable": 74244, "skip_no_positive": 698, "skip_zero_weight": 9}}, "same_augmented_geometry_counts": true, "checkpoint_sha256": "a92795d567260c4555ca8ed2a98081a9fd4562b4fe782b1d41cf67a8a35ecb3c"}. All three arms remain freshCOCO, commonbatch16; source selection queued automatically. No audit/US results yet opened. Reporting wording now specifies geometry-count equality (not pixel-view equality); live/snapshot logs are excluded by project .gitignore.

- **2026-11-08 20:22:46 Asia/Colombo** — rashmithachamikara/x03-b-select has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 20:23:07 Asia/Colombo** — rashmithachamikara/x03-b-select has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 20:23:18 Asia/Colombo** — Correction to20:05 process diagnosis: non-escalated Windows process inspection hid the detached executor; elevated CIM now confirmed PID10532 was alive alongside persistent executor23964. Both attempted identical source-selection submissions (v1/v2). Stopped both verified control.py processes before evaluation submission; cloud training completed once per arm and is unaffected. Adding a cross-process file lock before reattaching exactly one executor to selectionv2. Duplicate source-selection overhead will be recorded. Prior claim that detached PID had ended was incorrect; process visibility across sandbox contexts caused the error.

- **2026-11-08 20:24:05 Asia/Colombo** — Added OS-held executor byte lock; verified concurrent second process is rejected and a later process can acquire after release. Reattaching one executor to existing source-selection job, no new push.

- **2026-11-08 20:24:15 Asia/Colombo** — rashmithachamikara/x03-b-select has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 20:26:29 Asia/Colombo** — rashmithachamikara/x03-b-select has status "KernelWorkerStatus.COMPLETE"

- **2026-11-08 20:26:29 Asia/Colombo** — B command: `python -m kaggle kernels output rashmithachamikara/x03-b-select -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\artifacts\select --file-pattern .*`

- **2026-11-08 20:27:10 Asia/Colombo** — B command: `python -m kaggle kernels push -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\kaggle\evaluate --accelerator NvidiaTeslaT4 -t 7200`

- **2026-11-08 20:27:14 Asia/Colombo** — Kernel version 1 successfully pushed.  Please check progress at https://www.kaggle.com/code/rashmithachamikara/x03-b-evaluate

- **2026-11-08 20:27:18 Asia/Colombo** — rashmithachamikara/x03-b-evaluate has status "KernelWorkerStatus.QUEUED"

- **2026-11-08 20:27:35 Asia/Colombo** — Verified all three frozen checkpoint hashes and1034 exact source-only selection IDs; source-image export/native raw prediction differences are exactly0 on three images per arm. Frozen artifact SHA and confidence thresholds: {"status": "passed", "source_selection_ids": 1034, "frozen_file_sha256": "441a33579432e3fd47c287708142aa43ad10a5d7e17958e17d00019f2588c79b", "arms": {"baseline": {"threshold": 0.3871608040201005, "rule": "precision>=0.70, maximum recall, ties higher threshold", "source_image_parity_max_diff": 0}, "generic": {"threshold": 0.3871608040201005, "rule": "precision>=0.70, maximum recall, ties higher threshold", "source_image_parity_max_diff": 0}, "small_thin": {"threshold": 0.3721155778894472, "rule": "precision>=0.70, maximum recall, ties higher threshold", "source_image_parity_max_diff": 0}}}. Final audit/US evaluation has not yet produced outcomes.

- **2026-11-08 20:28:06 Asia/Colombo** — Both source-selection versions completed. Redundant v1 frozen configuration is exactly identical to retained v2; measured redundant stage overhead 0.04155969555083334T4-session hours (excluding install/queue/upload). Recorded in runs/duplicate-selection-overhead.json and will include in resources/report. Exactly one locked executor submitted evaluationv1; no duplicate evaluation.

- **2026-11-08 20:31:57 Asia/Colombo** — Strengthened final report verification while evaluation is queued: evaluation must retain the exact source-frozen configuration; report explicitly compares overall AP/recall and small/thin recall versus both comparators plus the common baseline threshold. Cross-permission-context lock rejection passed against the actual elevated executor. No new model or threshold tuning.

- **2026-11-08 20:42:06 Asia/Colombo** — Active final-evaluation queue check: accelerator quota snapshot saved in b-prototype/runs/quota-during-evaluation-queue.json; no paid scaling enabled. {"_time_used": "8:28:48.770000", "_time_reserved": "0:00:00", "_total_time_allowed": "1 day, 6:00:00", "_minimum_time_allowed": "1 day, 6:00:00", "_is_pay_to_scale_enabled": "False", "_has_ever_run": "True", "_is_frozen": "True"}. Preparing final report checks includes original versus augmented subgroup supports,54 deterministic overlays, class-count reconciliation, fixed50-epoch convergence diagnostics and exact frozen-config equality. No method changes or new experiments.

- **2026-11-08 20:54:07 Asia/Colombo** — Independent reconstruction of every production batch total loss from supervised items plus ramped auxiliary term passed for both arms, including final batch8: maximum relative errors generic1.1053e-7 andB1.0721e-7. Final verifier now enforces this batch-scaling identity. Evaluation still queued; quota available and no method changes.

- **2026-11-08 21:03:56 Asia/Colombo** — rashmithachamikara/x03-b-evaluate has status "KernelWorkerStatus.RUNNING"

- **2026-11-08 21:05:39 Asia/Colombo** — Final evaluationv1 began RUNNING at21:03:56 after approximately36min queue. Initial optional log-stream watcher received Kaggle HTTP500 while job was queued; reconnected watcher only, no evaluation resubmission. Exactly one file-locked executor active (session12231).

- **2026-11-08 21:13:50 Asia/Colombo** — Verified complete saved training recipes are identical across arms except name/save_dir, and resolved optimizer JSON is exactly identical. Added this to final artifact verifier; no configuration changes. Evaluation continues running after queue delay.

- **2026-11-08 21:23:21 Asia/Colombo** — rashmithachamikara/x03-b-evaluate has status "KernelWorkerStatus.COMPLETE"

- **2026-11-08 21:23:21 Asia/Colombo** — B command: `python -m kaggle kernels output rashmithachamikara/x03-b-evaluate -p C:\Files\Shared\Online Class\ITM\Sem7\FYP\fyp-research\projects\x03-road-damage\b-prototype\artifacts\evaluate --file-pattern .*`

- **2026-11-08 21:24:44 Asia/Colombo** — Evaluationv1 completed; downloading and verifying final artifacts. Account GPU quota after job: {"_time_used": "8:38:21.470000", "_time_reserved": "0:00:00", "_total_time_allowed": "1 day, 6:00:00", "_minimum_time_allowed": "1 day, 6:00:00", "_is_pay_to_scale_enabled": "False", "_has_ever_run": "True", "_is_frozen": "True"}. Also verified six pinned wheel source files equal official commit922563e after normalizing Windows newline translation; initial byte-hash comparison differed only by line endings. Source verification saved in runs/pinned-source-verification.json.

- **2026-11-08 21:25:37 Asia/Colombo** — B comparison/report completed; one-seed development evidence, not confirmation.

- **2026-11-08 21:25:37 Asia/Colombo** — Creating local project-scoped commit: Record B prototype comparison and verified diagnostic results

- **2026-11-08 21:27:04 Asia/Colombo** — Final review complete; verified report/metrics and executor lock released, all known Kaggle jobs COMPLETE. US findings: {"baseline": {"target_tp": 26, "target_gt": 528, "target_recall": 0.04924242424242424, "fp_per_image": 0.2853277835587929, "map50_95": 0.06304360067098233}, "generic": {"target_tp": 9, "target_gt": 528, "target_recall": 0.017045454545454544, "fp_per_image": 0.1529656607700312, "map50_95": 0.047741831567415245}, "small_thin": {"target_tp": 12, "target_gt": 528, "target_recall": 0.022727272727272728, "fp_per_image": 0.3267429760665973, "map50_95": 0.06151121604442702}}. B fails predefined FP guard: recall12/528 versus generic9/528, butFP/image0.3267 versus0.1530; baseline26/528 andFP/image0.2853. Classification=no improvement under this configuration; one-seed development evidence, not a general rejection of consistency. Three full trainings totaled6.4364T4h; accounted GPU-quota increase6.8554h. Reports and verified artifacts saved; stop now per user instruction. No further experiments or remote Git push.

- **2026-11-08 21:27:04 Asia/Colombo** — Creating local project-scoped commit: Finalize B prototype findings and stopped executor state
