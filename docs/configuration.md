# Configuration

Promethium uses **Pydantic Settings** to manage configuration via environment variables.

## Global Settings

| Variable | Default | Description |
|----------|---------|-------------|
| `APP_NAME` | `Promethium` | Name of the application instance. |
| `DEBUG` | `False` | Enable debug mode/logging. |
| `DATABASE_URL` | *Required* | SQLAlchemy connection string (e.g., `postgresql+asyncpg://...`). |
| `REDIS_URL` | *Required* | Redis connection string for caching. |
| `CELERY_BROKER_URL`| *Required* | Redis/RabbitMQ URL for task queue. |
| `DATA_STORAGE_PATH`| `/var/lib/promethium/data` | Path to persistent storage for SEG-Y files. |

## Pipeline Configuration

Job parameters (`params`) are passed as JSON blobs to the API.

### U-Net Parameters

```json
{
  "patch_size": [64, 64],
  "stride": [32, 32],
  "epochs": 50,
  "learning_rate": 1e-3,
  "batch_size": 16,
  "missing_trace_prob": 0.3
}
```

### Deconvolution Parameters

```json
{
  "operator_length": 40,
  "prediction_distance": 4,
  "white_noise": 0.1
}
```
