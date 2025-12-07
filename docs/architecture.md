# Architecture

Promethium is built as a set of loosely coupled services and libraries.

## High-Level Topology

```mermaid
graph TD
    User[User / Researcher] -->|HTTP| MB[Web Dashboard (React)]
    User -->|HTTP| API[Backend API (FastAPI)]
    
    subgraph "Application Layer"
        MB --> API
        API -->|Metadata| DB[(PostgreSQL)]
        API -->|Task Queue| Redis[(Redis)]
    end
    
    subgraph "Processing Layer"
        Worker[Celery Worker] -->|Poll| Redis
        Worker -->|Read/Write| Storage[File Storage (SEG-Y)]
        Worker -->|Update| DB
    end
```

## Components

### 1. Application Server (`src/promethium/api`)
- **Technology**: FastAPI (Python), Uvicorn.
- **Role**: Handles REST requests, validates inputs via Pydantic, controls the database transaction lifecycle, and dispatches long-running jobs to the queue.

### 2. Processing Worker (`src/promethium/workflow`)
- **Technology**: Celery, PyTorch, SciPy.
- **Role**: Executes CPU/GPU-intensive tasks.
  - **I/O Module**: Reads seismic data chunks efficiently.
  - **Signal Module**: Applies filters and deconvolution.
  - **ML Module**: Runs inference using pre-trained models.

### 3. Frontend (`web/`)
- **Technology**: React, TypeScript, Vite.
- **Role**: Provides the visual interface for uploading datasets and configuring pipeline parameters.

### 4. Persistence
- **PostgreSQL**: Stores relational data:
  - `datasets`: File paths, format info, acquisition headers.
  - `jobs`: Status, parameters, execution logic.
- **Redis**: Acts as the ephemeral message broker for Celery and caching layer.
- **File System**: Physical storage for SEG-Y files (Raw and Processed).

## Data Flow

1.  **Ingestion**: User uploads a SEG-Y file. API streams it to shared storage and creates a `Dataset` record in PostgreSQL.
2.  **Submission**: User selects a dataset and an algorithm (e.g., U-Net). API creates a `Job` record (status: QUEUED) and pushes a task ID to Redis.
3.  **Execution**: Worker picks up the task.
    - Loads data using `read_segy_robust`.
    - Normalizes data.
    - Passes data through the chosen `RecoveryAlgorithm` (e.g., `UNet.forward()`).
    - Denormalizes and saves the result as a new SEG-Y file.
4.  **Completion**: Worker updates `Job` status to COMPLETED and saves the `result_path`.
5.  **Retrieval**: Frontend polls the API and displays the completion status.

## Directory Structure

| Path | Purpose |
|------|---------|
| `src/promethium/core` | Base classes, configuration, logging. |
| `src/promethium/io` | Readers/Writers for SEG-Y, SAC, etc. |
| `src/promethium/ml` | PyTorch models and training loops. |
| `src/promethium/signal` | Filters and DSP algorithms. |
| `src/promethium/api` | Web server routes and schemas. |
| `src/promethium/workflows` | Celery task definitions. |
