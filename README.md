# TinyGPT from Scratch

**Character-level language modeling with manually implemented causal attention.**

Naveen Aravapalli · Python · PyTorch

[Results](reports/results.md) · [Metrics](reports/metrics.csv) · [Failure analysis](reports/failure_analysis.md) · [Setup](SETUP.md)

See [setup notes](SETUP.md) for dependencies, data requirements, and current reproducibility limitations.

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

- [Notebook](notebooks/train_tinygpt.ipynb)
- [Result visualization](https://github.com/aravapallinaveen/DATA266-Lab1-Pair25/blob/f2c44af85977ada3fc36cc70949f266a58726881/task1_llm/naveen/outputs/train_val_loss_curve.png)
- [Recorded metrics](reports/metrics.csv) and [detailed results](reports/results.md)

## Repository layout

```text
notebooks/          # training and evaluation notebooks
reports/            # metrics, results, and failure analysis
outputs/            # generated samples and evaluation tables
```

The code is organized into notebooks, experiment reports, and supporting artifacts. Datasets and large model artifacts are not bundled; see the reproduction guide for availability and setup details.



## Hardware

The saved results were recorded on an NVIDIA GeForce RTX 5090.
