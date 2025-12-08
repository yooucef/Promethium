# Promethium - SoTA Seismic Reconstruction Framework 🧬

[![CI](https://github.com/olaflaitinen/Promethium/actions/workflows/ci.yml/badge.svg)](https://github.com/olaflaitinen/Promethium/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![Angular](https://img.shields.io/badge/Angular-17+-dd0031.svg)](https://angular.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![Code Style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)

![Promethium Logo](docs/img/logo.png)

> **Advanced Seismic Data Recovery, Denoising, and Inpainting using State-of-the-Art AI/ML.**

Promethium is a production-grade framework designed for geophysicists and ML researchers. It provides a unified pipeline for ingesting seismic data (SEG-Y), preprocessing it for deep learning, and applying advanced reconstruction models (U-Net, Autoencoders, PINNs).

## 🚀 Key Features

*   **SoTA Model Zoo**: Pre-implemented U-Net, ResUNet, Denoising Autoencoders, and PINN architectures.
*   **High-Performance I/O**: Direct SEG-Y support with optimized Zarr conversion for cloud-native random access.
*   **Physics-Informed**: Loss functions integrating the Wave Equation to ensure physical consistency.
*   **Interactive Frontend**: Modern Angular-based dashboard ("Void/Neon" data theme) for job management and visualization.
*   **Scalable Backend**: FastAPI + Celery + Redis architecture for distributed training and inference.
*   **Production Ops**: Docker Compose stack with Prometheus/Grafana monitoring and CI/CD workflows.

## 🛠️ Tech Stack

*   **Core**: Python 3.10, PyTorch 2.0, PyTorch Lightning.
*   **Data**: xarray, numpy, zarr, segyio.
*   **Backend**: FastAPI, SQLAlchemy, Celery, Redis.
*   **Frontend**: Angular 17+, TypeScript, SCSS.
*   **Infrastructure**: Docker, Nvidia Runtime, Github Actions.

## 🏁 Quick Start

### Prerequisites
*   Docker & Docker Compose
*   NVIDIA Drivers (for GPU support)

### 1. clone & Env
```bash
git clone https://github.com/olaflaitinen/Promethium.git
cd Promethium
cp .env.example .env
```

### 2. Launch Stack
```bash
docker-compose up --build -d
```
Access the dashboard at `http://localhost:4200` and the API docs at `http://localhost:8000/docs`.

### 3. Run a Job
1.  Upload a `.sgy` file via the Dashboard.
2.  Navigate to "Jobs" > "New Job".
3.  Select "U-Net (Denoise)" and your dataset.
4.  Launch! Monitor progress in real-time.

## 📚 Documentation

*   [**Architecture Overview**](docs/architecture.md): System design and component interaction.
*   [**ML Pipelines**](docs/ml-pipelines.md): Detailed model architectures and training engines.
*   [**User Guide**](docs/user-guide.md): Step-by-step generic workflows.
*   [**Developer Guide**](docs/developer-guide.md): Setup, testing, and contribution.
*   [**Benchmarking**](docs/benchmarking.md): Methodology for evaluating model accuracy.
*   [**Deployment**](docs/deployment-guide.md): Production setup via Kubernetes/Docker.

## ⚖️ License

Proprietary / Enterprise License (See `LICENSE` file).
