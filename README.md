# TinyGPT from Scratch

**Character-level language modeling with manually implemented causal attention.**

Naveen Aravapalli · DATA266 · PyTorch

[Results](task1_llm/naveen/results.md) · [Metrics](task1_llm/naveen/metrics_report.csv) · [Failure analysis](task1_llm/naveen/failure_analysis.md) · [Reproduction guide](REPRODUCIBILITY.md) · [Team repository](https://github.com/aravapallinaveen/DATA266-Lab1-Pair25)

> Portfolio package assembled from Naveen's work at commit `f2c44af85977`. Metrics below are transcribed from saved artifacts, not independently rerun. This repository supplements the shared team submission.

## Project and recorded results

A decoder-only PyTorch model trained on TinyStories using a character vocabulary of 110, a 256-character context, four Transformer blocks, eight attention heads, and 256-dimensional embeddings. The recorded run used 100,000 training stories and 10,000 validation stories, seed 171, and 10 epochs on an RTX 5090.

The notebook contains the attention and model implementation; no prebuilt Transformer or attention module is claimed by the original results. Architecture rationale and failure analysis are preserved as the author's original work.

| Recorded validation metric | Value |
|---|---:|
| Cross-entropy | 0.62849 |
| Character-level perplexity | 1.87478 |
| Bits per character | 0.90672 |
| Next-character accuracy | 79.98% |
| Trainable/model parameters | 3,278,336 |

Character-level perplexity should be compared only under matching tokenization and evaluation protocols. Training duration and throughput in the original report are hardware-specific measurements.

## Explore the evidence

- [Included notebook](task1_llm/naveen/src/Task1_LLM_Naveen.ipynb)
- [Original result visualization](https://github.com/aravapallinaveen/DATA266-Lab1-Pair25/blob/f2c44af85977ada3fc36cc70949f266a58726881/task1_llm/naveen/outputs/train_val_loss_curve.png)
- [Source and ownership record](PROVENANCE.md)
- [Recorded metrics](task1_llm/naveen/metrics_report.csv) and [original interpretation](task1_llm/naveen/results.md)

## Repository layout

```text
README.md
REPRODUCIBILITY.md
PROVENANCE.md
requirements.in                 # dependency candidates, not a tested lock
reproducibility/
  artifact_checksums.json       # hashes of this portfolio snapshot
  run_manifest.template.json    # template for a future verified rerun
scripts/verify_evidence.py      # integrity check; does not train a model
task1_llm/naveen/
  src/                         # original notebook / implementation
  outputs/                     # selected small recorded tables
  metrics_report.csv
  results.md
  failure_analysis.md
```

Original task/member paths are retained so provenance and relative references remain recognizable. Large artifacts and datasets are not bundled; some original documents reference files available only upstream or in the submission package.

## Quick inspection

From this repository's root, with Python available:

```powershell
python scripts/verify_evidence.py
```

This checks the packaged evidence against local SHA-256 records. It does **not** reproduce training or validate metric correctness. Follow [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for remaining setup and run requirements.

## Ownership and academic context

This showcase contains Naveen's task folder, with attribution to the shared Pair 25 repository. Praveen's models and team-level leaderboard outcomes are not represented as Naveen's independent achievements. The assignment's shared team repository, individual training, and combined report requirements remain separate.

The original architecture choices, results, and analysis remain attributable to their author. AI assistance in this packaging pass covered documentation, organization, and evidence inspection; it did not conduct training or the human audit. Review all wording and disclose assistance as required by the course.

No new license is granted by this package. Confirm rights to publish course-derived material, data excerpts, and any reused code before adding a license or releasing the showcase publicly.
