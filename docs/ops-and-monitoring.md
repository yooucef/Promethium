# Operations & Monitoring

## Logging

Promethium uses structured logging.

*   **Format**: Logs are emitted with timestamp, level, module, and message.
*   **Aggregation**: In production, logs from Docker containers should be aggregated to a central system (e.g., ELK Stack, Splunk, or CloudWatch).

## Metrics

The system exposes metrics via **Prometheus**.

### Key Metrics
*   `http_request_duration_seconds`: API latency.
*   `job_duration_seconds`: Time taken for training/inference jobs.
*   `gpu_utilization`: GPU usage on worker nodes (via DCGM exporter).
*   `memory_usage`: RAM consumption.

## Monitoring Stack

A default monitoring stack is provided in `docker/docker-compose.monitor.yml`.

### Components
1.  **Prometheus**: Scrapes metrics from the API and Worker services.
2.  **Grafana**: Visualization dashboard connected to Prometheus. Defaults to port `3000`.

## Operational Best Practices

*   **Backups**: Regularly backup the PostgreSQL database (`promethium-db`) and the Zarr storage volume.
*   **Scaling**: The Worker service (`promethium-worker`) is stateless and can be scaled horizontally across multiple GPU nodes (requires Swarm or Kubernetes).
*   **Resource Limits**: Set Docker resource limits (CPU/RAM) to prevent OOM kills impacting other services.
