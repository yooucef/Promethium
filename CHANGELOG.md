# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Core**: Robust `SeismicDataset` model with xarray backend.
- **I/O**: Memory-mapped SEG-Y reader with rigorous header validation.
- **Signal**: Butterworth filters (bandpass, lowpass, highpass) and predictive deconvolution.
- **ML**: U-Net architecture for seismic interpolation in `src/promethium/ml/models.py`.
- **API**: FastAPI backend with `/datasets` and `/jobs` endpoints.
- **UI**: React-based dashboard for dataset and job management.
- **Deployment**: Docker Compose configuration for full stack deployment.

## [0.1.0] - 2025-12-07

### Initial Release
- Project scaffolding and architecture definition.
- Basic implementation of core libraries and web services.
