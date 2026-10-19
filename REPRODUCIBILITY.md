# Reproduction status and setup

## What was checked

Source files, recorded CSV metrics, notebook structure, and provenance were inspected. Training and evaluation were not executed in this packaging environment, which has no PyTorch installed. Dependency installation and GPU availability are not verified.

## Fresh environment

1. Create an isolated environment with a Python version compatible with the chosen PyTorch build.
2. Install a compatible PyTorch/CUDA build following its official installation instructions.
3. Review requirements.in against the notebook imports and original environment evidence. It is a dependency candidate list, not an exact lockfile.
4. After resolving and testing the environment, capture it with `python -m pip freeze > requirements.lock.txt`. Do not fabricate a lock from guessed versions.
5. Obtain `TinyStories` through its original provider or authorized course storage. Keep raw/processed datasets outside Git. Add an access-enabled course Drive link where required; no dataset link was provided for this packaging pass.
6. Retrieve checkpoints from the pinned upstream task folder when present; for external checkpoints record the URL and SHA-256 in a completed run manifest. Hash-check before use. Only load weights from a trusted source.

## Execute safely and record evidence

The original notebook derives paths from its working directory and contains CUDA-specific cells. Open it from its src folder in a fresh working copy. A portable, one-command training smoke test has not yet been validated.

Launch Jupyter from `task1_llm/naveen/src/` and open `Task1_LLM_Naveen.ipynb`. Inspect setup, preprocessing, model definitions, and GPU checks before running. Work in a fresh checkout so fixed output filenames cannot overwrite historical artifacts. The notebook is not a packaged training CLI.

Before a full run, use the author's own model on a tiny data subset and verify forward pass, finite loss, one optimizer step, and checkpoint reload. Record the actual passing command, expected outputs, environment, runtime, and artifact hashes. This remaining smoke-test work is separate from the supplied `scripts/verify_evidence.py` integrity check.

Use run-specific directories. Preserve logs without editing, record split identifiers and seeds, checkpoint-to-metric mappings, hardware, timing units, and evaluator version. Fill `reproducibility/run_manifest.template.json` from the executed run; null fields mean unknown, never zero.

## Before claiming exact reproduction

- [ ] Dataset/split revision and access instructions verified.
- [ ] Actual run configuration reconciled with stored checkpoint.
- [ ] A tested environment lock saved.
- [ ] One-command model smoke test passes from a clean environment.
- [ ] Evaluation can map each reported number to a checkpoint and raw evidence.
- [ ] Historic evidence limitations remain disclosed.
