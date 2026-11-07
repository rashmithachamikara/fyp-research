# X03 Kaggle baseline pilot

Source-only development pilot, not confirmatory worldwide generalisation evidence.

## Experiment

Original author RDD2022 country ZIPs: India (7706), Czech (2829), United States (4805 labelled images). Japan is neither downloaded nor inspected. Author release: https://github.com/sekilab/RoadDamageDetector ; dataset paper https://doi.org/10.1002/gdj3.260 (CC BY-SA 4.0). Archive/image/XML hashes and conversion decisions are saved by preparation.

The old S3 URLs returned 403. Preparation now uses byte ranges against the official Figshare archive https://figshare.com/articles/dataset/21431547 (file38030910), retrieving only the three nested country ZIPs. A fresh redirect is requested per range because download signatures expire after ten seconds. Genuine out-of-scope D01/D11/D43/D44/D50 annotations are ignored while retaining images and four-class labels. Unknown spellings/malformed annotations are quarantined and counted; excluded counts must be disclosed.

India/Czech are split approximately 80/10/10 by conservative duplicate groups into detector fit, checkpoint/threshold selection and independent source audit. US is simulated-unseen development data. No source-derived metric or threshold uses US. US-informed redesign contaminates future US confirmation; explicitly retain that limitation. There is no verified route metadata; duplicate grouping does not guarantee sequence independence.

Stock COCO YOLO11s, 640, Ultralytics 8.4.192, seed 42, 50 epochs, AMP, one GPU. Batch fallback 16/8/4, nano only if small cannot fit. Other resolved pinned-package defaults are archived in args.yaml. Checkpoint is source-selected; precision>=0.7 threshold selection uses a fixed 200-value grid, with highest recall then higher threshold; best F1 fallback. Not a guarantee of target precision.

Geometry is measured at fixed square-letterboxed 640 reference: small area<1024, thin short side<16, union counted once. Operational matching is class-aware confidence-ordered greedy IoU>=.5, after matching all boxes. AP uses pinned YOLO validation at conf=.001/max_det=300. C grid includes letterbox padding and predicts missed centres, not damage extent. A diagnostic has no parameter updates. B diagnostic compares 640 vs320 at the same source threshold; it cannot establish consistency training helps. C uses raw weak maps only, with tie-aware average precision and positive-cell prevalence; no monitor is trained.

## Jobs

`python build_notebooks.py` creates self-contained private notebooks. Use `python -m kaggle`, since the executable is not on this machine's PATH.

1. `kaggle/prepare`: CPU download/audit/conversion/group splits. Output prepared.tar.gz plus original_xml.tar.gz and audit/manifest/overlays.
2. `kaggle/smoke`: GPU two-epoch subset job, deliberate interruption after epoch-zero checkpoint, resume optimizer/epoch verification. Depends on successful preparation.
3. `kaggle/train`: GPU full 50-epoch baseline starting from COCO, not smoke weights. Depends on successful smoke and preparation. Assignment diagnostics run after checkpoint preservation.
4. `kaggle/evaluate`: GPU source threshold selection then independent country evaluation, scale/miss-grid diagnostics and deterministic example overlays. Depends on preparation/training.

Submit with `python -m kaggle kernels push -p kaggle/STAGE --accelerator NvidiaTeslaT4 -t 43200` (omit accelerator and use shorter timeout for CPU preparation). CLI limit and actual account GPU availability apply. Only device0 is used even when T4x2 is allocated. Outputs are versioned Kaggle kernel artifacts, not ephemeral interactive files.

The recovery smoke test must pass before main training. Unexpected training interruption requires inspecting last.pt epoch/optimizer, retaining the original 50-epoch schedule and resuming from the upstream checkpoint; never silently restart as a resume. One seed and finite epochs are pilot limitations. Examine source learning curves for unresolved convergence before attributing misses to the method.

## Files and records

All commands/results belong to this directory. `runs/` contains launch/status and concise records; `artifacts/` holds downloaded large outputs and is Git-ignored. Code, notebooks, manifests/audits (without large data) and the final pilot report can be committed. Raw images, archives, model weights and caches are ignored. No secrets or remote Git push.

Validation: run `python -m unittest discover -s . -p test_metrics.py` with numpy/Pillow installed. Run the actual Kaggle smoke test for GPU/library compatibility. Kaggle job failures propagate through checked subprocess calls.
