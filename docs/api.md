# API Documentation

The Promethium API is built with FastAPI and follows RESTful principles.

## Base URL
`/api/v1`

## Endpoints

### Datasets
- `POST /datasets/`: Upload and register a new dataset.
  - Form Data: `name` (string), `format` (string), `file` (binary).
- `GET /datasets/`: List all registered datasets.
- `GET /datasets/{id}`: Get metadata for a specific dataset.

### Jobs
- `POST /jobs/`: Submit a processing job.
  - Body: JSON with `dataset_id`, `algorithm`, `params`.
- `GET /jobs/`: List all jobs.
- `GET /jobs/{id}`: Get status and results of a job.

## Schemas
All requests and responses are validated using Pydantic models. Refer to the Swagger UI (`/docs`) for detailed schema definitions.

## Authentication
(Pending Implementation) - Designed to support JWT Bearer tokens.
