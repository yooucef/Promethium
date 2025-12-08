# Promethium - Advanced Seismic Data Recovery and Reconstruction Framework

[![CI](https://github.com/olaflaitinen/Promethium/actions/workflows/ci.yml/badge.svg)](https://github.com/olaflaitinen/Promethium/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![Angular](https://img.shields.io/badge/Angular-17+-dd0031.svg)](https://angular.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)

Promethium is an advanced framework for seismic data recovery, reconstruction, and enhancement. It integrates state-of-the-art artificial intelligence and machine learning techniques with classical geophysical signal processing to solve complex inverse problems in exploration geophysics, seismology, and hazard analysis.

The system is designed for high-performance scale, supporting high-throughput ingestion of seismic data segments, processing via distributed GPU workers, and interactive visualization through a modern web interface.

## Branding and Visual Identity

The Promethium visual identity is anchored by a dark navy logo representing a continuous, organic waveform, symbolizing the recovery of signal fidelity from noise.

*   **Logo**: `assets/branding/promethium-logo.png`
*   **Primary Color**: Deep Navy `#050B24`
*   **Accent Color**: Electric Cyan `#00F0FF`

## Key Features

*   **Multi-Format Ingestion**: Native support for **SEG-Y**, **SEG-2**, **miniSEED**, and **SAC** formats.
*   **Signal Conditioning**: Robust pipelines for denoising, deconvolution, and wavelet estimation.
*   **AI/ML Reconstruction**: Implementation of **U-Net**, **Autoencoders**, **GANs**, and **PINNs** for data interpolation and inpainting.
*   **Physics-Informed Constraints**: Integration of Wave Equation losses to ensure physical viability of reconstructed wavefields.
*   **Scalable Architecture**: Asynchronous task orchestration using **Celery**, **Redis**, and **PostgreSQL**.
*   **Modern Frontend**: an **Angular**-based interface for job management, configuration, and real-time visualization.
*   **Containerized Deployment**: Fully Dockerized stack for consistent deployment across local and cloud environments.

## Architecture Snapshot

Promethium follows a modular microservices-inspired architecture:

1.  **Core Library**: Domain models and utilities (`src/promethium/core`).
2.  **ML Subsystem**: PyTorch-based models and training loops (`src/promethium/ml`).
3.  **Backend API**: FastAPI gateway exposing REST endpoints (`src/promethium/api`).
4.  **Workflow Engine**: Distributed workers for long-running computational tasks (`src/promethium/workflows`).
5.  **Frontend**: Interactive Angular user interface (`frontend/`).

For a detailed breakdown, please refer to [Architecture Overview](docs/architecture.md).

## Quick Start

The following instructions assume a Linux-based environment with Docker and Docker Compose installed.

### 1. clone the Repository

```bash
git clone https://github.com/olaflaitinen/Promethium.git
cd Promethium
```

### 2. Configure Environment

Copy the example configuration to a production environment file.

```bash
cp .env.example .env
```

### 3. Launch the Stack

Start all services in detached mode.

```bash
docker-compose up --build -d
```

Access the application at `http://localhost:4200` and the API documentation at `http://localhost:8000/docs`.

## Use Cases

*   **Exploration Geophysics**: Recovering missing traces in sparse acquisition surveys to improve subsurface imaging.
*   **Continuous Monitoring**: Real-time denoising of microseismic streams for accurate event detection.
*   **Academic Benchmarking**: Providing a standardized platform for comparing novel reconstruction algorithms against established baselines.

## Documentation

*   [Overview](docs/overview.md)
*   [User Guide](docs/user-guide.md)
*   [Developer Guide](docs/developer-guide.md)
*   [ML Pipelines](docs/ml-pipelines.md)
*   [Benchmarking](docs/benchmarking.md)
*   [Deployment Guide](docs/deployment-guide.md)

## Contributing

We welcome contributions from the community. Please review our [Contribution Guidelines](CONTRIBUTING.md) and [Governance Model](GOVERNANCE.md) before submitting Pull Requests.

## License

This project is currently proprietary. Please see the [LICENSE](LICENSE) file for details.
