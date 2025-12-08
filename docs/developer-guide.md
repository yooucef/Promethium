# Developer Guide

## Environment Setup

### Prerequisites
*   **Python**: 3.10+
*   **Node.js**: 20+ (LTS)
*   **Docker**: 24.0+

### 1. Backend Setup (Conda)
We recommend Conda for managing heavy scientific dependencies (PyTorch, NumPy).

```bash
# Create environment
conda env create -f docker/environment.yml
conda activate promethium

# Install dev dependencies
pip install -r requirements-dev.txt

# Install package in editable mode
pip install -e .
```

### 2. Frontend Setup (Angular)
```bash
cd frontend
npm ci
npm start
```

## Code Standards

### Python
*   **Style**: PEP 8.
*   **Formatter**: `black` (Line length: 88).
*   **Linter**: `ruff`.
*   **MyPy**: Strict type checking enabled for `src/promethium/core` and `src/promethium/api`.

**Running Checks**:
```bash
ruff check .
black --check .
mypy src
```

### TypeScript / Angular
*   **Linter**: `eslint`.
*   **Formatter**: `prettier`.

## Project Structure

*   `src/promethium/core`: **Core Domain**. Configuration, Logging, Exceptions. No external dependencies ideally.
*   `src/promethium/io`: **Data Layer**. Wrappers for SEG-Y and Zarr.
*   `src/promethium/ml`: **Intelligence**. PyTorch models (`modules/`) and Lightning systems (`systems/`).
*   `src/promethium/api`: **Interface**. FastAPI routers, schemas.
*   `tests/`: **Verification**. Mirrored structure of source.

## Testing Strategy

*   **Unit Tests**: Fast, mocked tests. Run with `pytest tests/unit`.
*   **Integration Tests**: Database/Redis interactions. Run with `pytest tests/integration`.
*   **E2E Tests**: Full pipeline runs. Run with `pytest tests/e2e`.

## Contribution Workflow

1.  Create a feature branch: `git checkout -b feature/my-cool-model`
2.  Implement changes.
3.  Add/Update tests.
4.  Ensure all checks pass.
5.  Submit PR.
