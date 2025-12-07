# Promethium Docker Deployment Guide

## Overview

This guide covers building and running Promethium using Docker with optimized build times.

## Build Performance

| Build Type | Before Optimization | After Optimization |
|------------|---------------------|-------------------|
| First build (cold) | 30-40 minutes | 3-5 minutes |
| Rebuild (no changes) | 30-40 minutes | 10-20 seconds |
| Rebuild (code only) | 30-40 minutes | 30-60 seconds |

### Why the Improvement?

1. **Conda Pre-compiled Packages**: NumPy, SciPy, PyTorch installed via Conda with optimized BLAS/LAPACK
2. **Multi-stage Builds**: Final images contain only runtime dependencies
3. **Layer Caching**: Dependencies installed before copying source code
4. **Separated Requirements**: Conda environment.yml and pip requirements.txt cached independently

## Quick Start

### Build and Run

```bash
# Navigate to project root
cd promethium

# Build and start all services
docker compose -f docker/docker-compose.yml up --build -d

# Wait for services to be healthy (about 30 seconds)
docker compose -f docker/docker-compose.yml ps
```

### Access Points

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:3000 | Angular Web Dashboard |
| API | http://localhost:8000 | FastAPI Backend |
| API Docs | http://localhost:8000/docs | Swagger Documentation |
| PostgreSQL | localhost:5432 | Database (promethium/promethium_dev_password) |
| Redis | localhost:6379 | Message Broker |

## Common Commands

### View Logs

```bash
# All services
docker compose -f docker/docker-compose.yml logs -f

# Specific service
docker compose -f docker/docker-compose.yml logs -f api
docker compose -f docker/docker-compose.yml logs -f worker
docker compose -f docker/docker-compose.yml logs -f frontend
```

### Stop Services

```bash
docker compose -f docker/docker-compose.yml down
```

### Clean Rebuild

```bash
# Remove volumes and rebuild
docker compose -f docker/docker-compose.yml down -v
docker compose -f docker/docker-compose.yml up --build -d
```

### Debug Mode

```bash
# Run with debug logging
docker compose -f docker/docker-compose.yml up --build

# Execute shell in running container
docker exec -it promethium-api /bin/bash
docker exec -it promethium-worker /bin/bash
```

## CI/CD Integration

### GitHub Actions Cache

```yaml
# .github/workflows/docker.yml
name: Docker Build

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Build and cache
        uses: docker/build-push-action@v5
        with:
          context: .
          file: docker/backend.Dockerfile
          push: false
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

### Reproducible Builds

All dependencies are pinned:
- `docker/environment.yml` - Conda packages
- `docker/requirements.txt` - Pip packages
- `frontend/package-lock.json` - npm packages

## Architecture

```
promethium/
├── docker/
│   ├── backend.Dockerfile      # Miniconda-based backend
│   ├── frontend.Dockerfile     # Node.js 20 + Nginx
│   ├── docker-compose.yml      # Service orchestration
│   ├── environment.yml         # Conda dependencies
│   └── requirements.txt        # Pip dependencies
├── frontend/
│   ├── nginx.conf              # Frontend proxy config
│   └── package-lock.json       # npm lock file
└── src/
    └── promethium/             # Backend source code
```

## Troubleshooting

### Build Fails on Conda

If Miniconda image fails to pull:
```bash
docker pull continuumio/miniconda3:24.1.2-0
```

### Port Already in Use

```bash
# Check what's using the port
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# Or change ports in docker-compose.yml
```

### Out of Disk Space

```bash
# Clean Docker cache
docker system prune -a
docker volume prune
```

## Model Storage

For ML models and large files, mount a persistent volume:

```yaml
volumes:
  - ./models:/app/models
```

Or use environment variables:
```bash
MODEL_STORAGE_PATH=/app/models
```
