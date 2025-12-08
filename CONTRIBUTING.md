# Contributing to Promethium

Thank you for your interest in contributing to Promethium. This document outlines the process for contributing to the project, ensuring that your contributions can be integrated efficiently and effectively.

## Contribution Philosophy

Promethium aims to be a definitive framework for seismic data reconstruction. We value:

1.  **Technical Excellence**: Code should be performant, robust, and mathematically correct.
2.  **Clarity**: Documentation and code comments must be precise and unambiguous.
3.  **Reproducibility**: All algorithmic results must be reproducible via provided configurations and seeds.

## Development Environment Setup

### Backend (Python)

The backend requires **Python 3.10+**. We recommend using `Conda` or `venv` for environment management.

```bash
# Create environment
conda create -n promethium python=3.10
conda activate promethium

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Frontend (Angular)

The frontend requires **Node.js 20+**.

```bash
cd frontend
npm ci
```

### Docker

Ensure **Docker Engine** and **Docker Compose** are installed to run the full integration stack locally.

## Coding Standards

### Python

*   **Style**: We adhere to **PEP 8**.
*   **Linting**: use `ruff` for linting and import sorting.
*   **Formatting**: Use `black` for code formatting.
*   **Typing**: All function signatures must be fully type-hinted.

### Angular / TypeScript

*   Follow the official [Angular Style Guide](https://angular.io/guide/styleguide).
*   Use `ESLint` and `Prettier` configurations provided in the repository.

### Commit Messages

Use the [Conventional Commits](https://www.conventionalcommits.org/) specification:

*   `feat: ...` for new features.
*   `fix: ...` for bug fixes.
*   `docs: ...` for documentation changes.
*   `refactor: ...` for code restructuring without behavioral change.

## Pull Request Guidelines

1.  **Branch Naming**: Use descriptive names, e.g., `feat/unet-attention-blocks` or `fix/segy-header-parsing`.
2.  **Scope**: Keep PRs focused on a single logical change.
3.  **Testing**: Include unit tests for new logic. Ensure all existing tests pass.
4.  **Documentation**: Update relevant documentation in `docs/` if functionality changes.

## Issue Reporting

When filing an issue, please include:

1.  A clear, descriptive title.
2.  Steps to reproduce the issue (minimal example).
3.  Expected vs. actual behavior.
4.  Environment details (OS, Python version, Docker version).
