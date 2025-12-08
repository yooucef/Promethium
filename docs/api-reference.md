# API Reference

The Promethium API is a RESTful interface built with FastAPI. It provides access to datasets, jobs, and system metadata.

> **Note**: Interactive OpenAPI documentation is available at `/docs` when the service is running.

## Datasets

### List Datasets
`GET /api/v1/datasets`

Returns a list of registered datasets.

**Response**:
```json
[
  {
    "id": "uuid",
    "name": "Gulf of Mexico Block A",
    "path": "/data/gom_block_a.sgy",
    "size_bytes": 1024000
  }
]
```

### Register Dataset
`POST /api/v1/datasets`

**Body**:
```json
{
  "name": "North Sea Survey",
  "path": "/data/imports/ns_04.sgy"
}
```

## Jobs

### Submit Job
`POST /api/v1/ml/train`

**Body**:
```json
{
  "dataset_id": "uuid",
  "model_config": {
    "family": "unet",
    "n_channels": 1
  },
  "training_config": {
    "epochs": 50,
    "batch_size": 32
  }
}
```

### Get Job Status
`GET /api/v1/ml/jobs/{job_id}`

**Response**:
```json
{
  "job_id": "uuid",
  "status": "RUNNING",
  "result": null
}
```
