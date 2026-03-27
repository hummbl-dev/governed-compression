# governed-compression

Private research implementation surface for governed vector and KV-cache compression.

## Purpose

This repo exists to provide a better implementation surface than the current fragmented TurboQuant-adjacent landscape.

Core goals:

- CPU reference implementation first
- reproducible benchmarks
- Windows via WSL2 first
- tuple-based experiment logging from day one
- method comparison across TurboQuant-style, QJL, and simple baselines

## Initial Scope

- vector encode / decode
- approximate dot product
- distortion metrics
- simple benchmark harness
- experiment logging

This repo is not yet a full inference-runtime integration project.

## Layout

```text
governed_compression/
  core/
  bench/
  logging/
tests/
examples/
docs/
```

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python -m governed_compression.cli
```

## Current Status

Stage 1 scaffold only.
