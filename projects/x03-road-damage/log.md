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
