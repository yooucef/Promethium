# API Reference

**Base URL**: `/api/v1`

## Datasets

### Upload Dataset
`POST /datasets/`

Registers a new dataset in the system.

**Request (Multipart/Form-Data)**
- `name` (string): Friendly name.
- `format` (string): `SEGY`, `SAC`, etc.
- `file` (file): The binary file.

**Response (201 Created)**
```json
{
  "id": 1,
  "name": "Survey A",
  "format": "SEGY",
  "file_path": "/data/uuid_filename.sgy",
  "upload_time": "2025-01-01T12:00:00Z"
}
```

### List Datasets
`GET /datasets/`

Returns a paginated list of datasets.

**Query Parameters**
- `skip` (int): Offset (default 0).
- `limit` (int): Count (default 100).

## Jobs

### Submit Job
`POST /jobs/`

Queues a new processing task.

**Request (JSON)**
```json
{
  "dataset_id": 1,
  "algorithm": "unet",
  "params": {
    "epochs": 10,
    "lr": 0.001
  }
}
```

**Response (201 Created)**
```json
{
  "id": "uuid-string",
  "status": "QUEUED",
  "created_at": "..."
}
```

### Job Status
`GET /jobs/{id}`

Returns the current status and result path.

**Response**
```json
{
  "id": "uuid-string",
  "status": "COMPLETED",
  "result_path": "/data/results/output.sgy",
  "error_message": null
}
```
