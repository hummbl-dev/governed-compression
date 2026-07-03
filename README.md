# governed-compression

[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/hummbl-dev/governed-compression/main)](https://github.com/hummbl-dev/governed-compression/commits/main)

Private research implementation surface for governed vector and KV-cache compression.

Learn more at [hummbl.io](https://hummbl.io).

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

## Repository Health

See [REPO_HEALTH.md](docs/REPO_HEALTH.md) for the authoritative repository
health contract and validation checks.

## Current Status

Stage 1 scaffold only.
