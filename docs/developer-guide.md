# Developer Guide

## Development Environment

### Requirements
- Python 3.10+
- Node.js 18+ (for frontend)
- Docker & Docker Compose (optional but recommended)

### Setup

1. **Backend**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e .[dev]
   ```

2. **Frontend**:
   ```bash
   cd web
   npm install
   ```

## Codebase Structure

- `src/promethium/`: Core Python package.
  - `api/`: FastAPI application. Add new routers in `api/routers/`.
  - `core/`: Shared utilities. `models.py` defines core data structures.
  - `io/`: Data ingestion. New formats should inherit or follow patterns in `readers.py`.
  - `ml/`: PyTorch definitions. `models.py` contains architectures.
  - `signal/`: DSP algorithms.
  - `workflows/`: Celery tasks defined in `tasks.py`.

## Adding a New Algorithm

To add a new signal processing or recovery algorithm:

1. **Implement Logic**:
   Create a new file in `src/promethium/signal` or `recovery`.
   ```python
   # src/promethium/signal/new_algo.py
   def my_filter(data: np.ndarray, param: float) -> np.ndarray:
       ...
   ```

2. **Expose in Worker**:
   Update `src/promethium/workflows/tasks.py` to import and call your function inside `run_reconstruction_job` based on the `algorithm` parameter.

3. **Update UI**:
   Add the new option to the `<select>` element in `web/src/components/JobManager.tsx`.

## Testing

Run the full suite with:
```bash
pytest tests/
```

- **Unit Tests**: `tests/unit/` (Fast, isolated)
- **Integration**: `tests/integration/` (Requires DB/Redis if not mocked)

## Linting

We use `ruff` for linting and formatting.
```bash
ruff check .
ruff format .
```
