# Contributing

Thank you for your interest in governed-compression.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
```

## Tests

```bash
pytest tests/ -v
```

## Lint

```bash
ruff check .
```

## Pull requests

- Branch from `main`
- Include tests for new functionality
- Ensure `pytest` and `ruff check` pass before submitting
