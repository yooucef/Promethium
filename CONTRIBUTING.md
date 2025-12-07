# Contributing to Promethium

Thank you for your interest in contributing to Promethium. We aim to build a robust, scientific-grade framework for seismic data analysis. To maintain high standards of code quality and scientific rigor, please adhere to the following guidelines.

## Philosophy

- **Scientific Rigor**: Algorithms must be technically correct and ideally referenced against established literature.
- **Reproducibility**: All data processing steps must be deterministic where possible, or seeded if stochastic.
- **Quality**: Code must be tested, typed, and documented.

## Getting Started

1. **Fork and Clone**
   Fork the repository to your account and clone it locally.

2. **Environment Setup**
   We recommend using a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e .[dev]
   ```

3. **Pre-commit Checks**
   Ensure you have the necessary linters installed (`ruff`, `black`, `mypy`).

## Development Workflow

### Branching Strategy

- `main`: Stable production code. do not push directly to main.
- `feature/Name`: New capabilities or algorithms.
- `bugfix/Name`: Resolutions for specific issues.
- `docs/Name`: Documentation updates.

### Pull Requests

1. **Tests**: Ensure all unit tests pass (`pytest`). Add new tests for any new logic.
2. **Linting**: Code must be formatted with `black` and linted with `ruff`.
3. **Documentation**: Update docstrings and relevant markdown files in `docs/` if architecture changes.
4. **Description**: Clearly describe the geophysical or technical context of your change.

## Coding Standards

### Python
- **Type Hints**: Mandatory for all function signatures.
- **Style**: Google-style docstrings.
- **Formatting**: `black` with default line length (88).

### Frontend (React)
- **Components**: Functional components with TypeScript interfaces.
- **State**: Use hooks effectively; avoid excessive global state.
- **Styling**: Use CSS modules or defined global variables; do not hardcode hex values.

## Issue Reporting

When reporting issues, please include:
1. **Context**: Operation being performed (e.g., "SEG-Y Ingestion").
2. **Reproduction**: Minimal code snippet or steps to trigger the error.
3. **Logs**: Relevant stack traces from the worker or API logs.
4. **Environment**: OS, Python version, Docker version.

## Security

Please refer to [SECURITY.md](SECURITY.md) for reporting vulnerabilities.
