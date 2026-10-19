# TinyGPT from Scratch

**Character-level language modeling with manually implemented causal attention.**

Naveen Aravapalli · Python · PyTorch

[Results](task1_llm/naveen/results.md) · [Metrics](task1_llm/naveen/metrics_report.csv) · [Failure analysis](task1_llm/naveen/failure_analysis.md) · [Reproduction guide](REPRODUCIBILITY.md)

Results below come from the saved experiment metrics. See [reproducibility notes](REPRODUCIBILITY.md) for environment setup and current rerun limitations.

## Overview and results

A decoder-only PyTorch model trained on TinyStories using a character vocabulary of 110, a 256-character context, four Transformer blocks, eight attention heads, and 256-dimensional embeddings. The recorded run used 100,000 training stories and 10,000 validation stories, seed 171, and 10 epochs on an RTX 5090.

Causal self-attention is implemented directly with query, key, and value projections, scaled dot products, and a lower-triangular mask. The notebook also implements the Transformer blocks, language-model head, and autoregressive generation.

| Recorded validation metric | Value |
|---|---:|
| Cross-entropy | 0.62849 |
| Character-level perplexity | 1.87478 |
| Bits per character | 0.90672 |
| Next-character accuracy | 79.98% |
| Parameters | 3,278,336 |

Character-level perplexity should be compared only under matching tokenization and evaluation protocols. Training duration and throughput in the original report are hardware-specific measurements.

## Code and analysis

- [Notebook](task1_llm/naveen/src/Task1_LLM_Naveen.ipynb)
- [Result visualization](https://github.com/aravapallinaveen/DATA266-Lab1-Pair25/blob/f2c44af85977ada3fc36cc70949f266a58726881/task1_llm/naveen/outputs/train_val_loss_curve.png)
- [Source history and attribution](PROVENANCE.md)
- [Recorded metrics](task1_llm/naveen/metrics_report.csv) and [detailed results](task1_llm/naveen/results.md)

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

The implementation retains its original directory structure. Datasets and large model artifacts are not bundled; see the reproduction guide for availability and setup details.

## Verify local files

From this repository's root, with Python available:

```powershell
python scripts/verify_evidence.py
```

This checks file integrity against the saved SHA-256 hashes. It does not run the model or recompute evaluation metrics. Follow [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for remaining setup and run requirements.

## Author and source history

Implemented by Naveen Aravapalli. [PROVENANCE.md](PROVENANCE.md) records the original source, attribution, and changes made when organizing this repository.
