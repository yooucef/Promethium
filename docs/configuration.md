# Configuration

Promethium uses a hierarchical configuration system based on Pydantic `BaseSettings`.

## Environment Variables

The primary configuration method is the `.env` file (or environment variables in K8s).

| Variable | Description | Default |
|String | ----------- | ------- |
| `APP_NAME` | Name of the application | Promethium |
| `DATABASE_URL` | PostgreSQL Connection String | `postgresql+asyncpg://...` |
| `REDIS_URL` | Redis Connection String | `redis://...` |
| `CELERY_BROKER_URL` | Broker for Celery | `redis://...` |
| `DATA_STORAGE_PATH` | Base path for storage | `/data` |
| `LOG_LEVEL` | Logging verbosity | `INFO` |

## Model Configuration

Models are configured via JSON/Dictionary objects passed to the training API.

```json
{
  "family": "unet",
  "n_channels": 1,
  "parameters": {
    "depth": 4,
    "base_filters": 32,
    "use_attention": true
  }
}
```

## Training Configuration

Hyperparameters for the training loop.

```json
{
  "batch_size": 32,
  "lr": 0.001,
  "epochs": 100,
  "loss": "mse", // Options: mse, l1, pinn
  "optimizer": "adamw"
}
```
