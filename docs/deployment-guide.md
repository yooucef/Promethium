# Deployment Guide

## Docker Stack

Promethium is designed to be deployed using Docker. The `docker-compose.yml` file defines the standard stack.

### Services

| Service | Image | Internal Port | Description |
|---------|-------|---------------|-------------|
| `api` | `promethium-backend` | 8000 | FastAPI REST server. |
| `worker`| `promethium-backend` | - | Celery worker process. |
| `db` | `postgres:15-alpine` | 5432 | Metadata store. |
| `redis` | `redis:7-alpine` | 6379 | Message broker & cache. |

### Configuration

Environment variables control the deployment. These are set in `docker-compose.yml` but should be managed via `.env` in production.

- `DATABASE_URL`: Connection string for PostgreSQL.
- `CELERY_BROKER_URL`: Redis URL for Celery.
- `DATA_STORAGE_PATH`: Host directory mounted to containers for persisting large files.

### Production Considerations

1. **Reverse Proxy**: Place Nginx or Traefik in front of the `api` service to handle SSL termination and static file serving.
2. **Persistence**: Ensure the `/data` volume and Postgres volumes are backed by reliable storage (e.g., EBS, NFS).
3. **Scaling**: The `worker` service can be scaled horizontally (`docker compose up -d --scale worker=3`) to handle higher job throughput.
