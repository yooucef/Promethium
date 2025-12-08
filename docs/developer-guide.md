# Developer Guide

## Repository Layout

*   `src/promethium/core`: Configuration, logging, exception classes.
*   `src/promethium/io`: Readers and writers for SEG-Y, Zarr, etc.
*   `src/promethium/ml`: PyTorch models, datasets, training loops.
*   `src/promethium/api`: FastAPI routers and schemas.
*   `src/promethium/workflows`: Celery task definitions.
*   `frontend/`: Angular application source.

## Backend Development

### Setup
1.  Install Python 3.10+.
2.  Create virtual environment: `python -m venv venv`.
3.  Install deps: `pip install -r requirements.txt`.

### Running Locally
```bash
uvicorn src.promethium.api.main:app --reload --port 8000
```

### Running Tests
We use `pytest`.
```bash
pytest tests/
```

## Frontend Development

### Setup
1.  Install Node.js 20.
2.  Install Angular CLI: `npm install -g @angular/cli`.
3.  Install deps: `cd frontend && npm ci`.

### Running Locally
```bash
ng serve
```
Navigate to `http://localhost:4200`.

## Adding a New Model

1.  Create a new class in `src/promethium/ml/models/` inheriting from `PromethiumModel`.
2.  Register the model using the `@ModelRegistry.register("model_name")` decorator.
3.  Update `docs/ml-pipelines.md` to document the new architecture.
