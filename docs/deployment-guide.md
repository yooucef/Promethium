# Deployment Guide 🚀

## Production Architecture (Docker)

The recommended deployment uses Docker Compose or Kubernetes.

### Stack Components
*   **promethium-api**: FastAPI Backend.
*   **promethium-worker**: Celery Worker (GPU enabled).
*   **promethium-frontend**: Nginx serving Angular static files.
*   **redis**: Message Broker.
*   **postgres**: Metadata Store.
*   **prometheus/grafana**: Monitoring.

### Deployment Steps (Docker Compose)

1.  **Build Images**:
    ```bash
    docker-compose build
    ```

2.  **Configuration**:
    Ensure `.env` contains production secrets (DB passwords, etc.).

3.  **Run**:
    ```bash
    docker-compose up -d
    ```

4.  **Verify**:
    *   Frontend: `http://localhost:4200`
    *   API: `http://localhost:8000/health`
    *   Grafana: `http://localhost:3000`

## Environment Optimization

### GPU Support
Ensure the `nvidia-container-runtime` is installed on the host. The `docker-compose.yml` configures the worker service to request GPU resources:

```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: 1
          capabilities: [gpu]
```

### Data Storage
*   Mount high-performance SSD/NVMe storage to `/data` volume for Zarr archives.
*   Use standard storage for PostgreSQL and Logs.
