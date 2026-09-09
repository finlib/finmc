# About this repo

finmc is a Python library for Monte Carlo Simulation of financial models.

## Requirements

- Python 3.12

## Structure

```text
├── .github/                 # GitHub metadata and CI workflows
├── docs/                    # MkDocs documentation source
├── finmc/                   # Main package
│   ├── calc/                # Option pricing calculators
│   ├── models/              # MC model implementations (Heston, Hull-White, Local Vol, ...)
│   ├── plots/               # Plotting helpers
│   ├── utils/               # Shared utilities
│   └── VERSION              # Static version file
├── notebooks/               # Jupyter notebooks
├── tests/                   # pytest test suite
├── Makefile                 # Project utilities
├── requirements.txt         # Runtime dependencies
├── requirements-test.txt    # Dev/test dependencies
└── setup.py                 # Package setup
```

## Setting up a development environment

**Windows (PowerShell)**
```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -e .[test]
```

**Linux / macOS**
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .[test]
```

On Linux/macOS, `make virtualenv` does the above automatically.

## Running tests

```bash
pytest -v tests/
```

With coverage:
```bash
pytest -v --cov=finmc --cov-config .coveragerc tests/
```

## Linting and formatting

```bash
ruff check finmc/ tests/
mypy --ignore-missing-imports finmc/
```

Format code:
```bash
isort finmc/
ruff format finmc/ tests/
```

## The Makefile (Linux / macOS)

```bash
make help        # Show available targets
make virtualenv  # Create .venv and install dependencies
make install     # Install in editable mode
make lint        # Run ruff and mypy
make fmt         # Format with ruff and isort
make test        # Lint + run tests with coverage
make clean       # Remove build artifacts and caches
make release     # Tag and push a new release
```
