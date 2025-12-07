# Promethium

**Advanced Seismic Data Recovery and Reconstruction Framework**

Promethium is a production-grade framework designed for the systematic recovery, reconstruction, and enhancement of seismic data. It unifies classical geophysical signal processing, modern machine learning, and advanced optimization under a single, coherent architecture.

## Features

- **Multi-channel data handling**: Support for SEG-Y, SEG-2, miniSEED, and SAC.
- **Signal Processing**: Adaptive filtering, deconvolution, and spectral analysis.
- **Data Recovery**: Matrix completion, compressive sensing, and deep learning-based interpolation.
- **Physics-Aware**: Integration of wave equation constraints and PINNs.
- **Web Interface**: Interactive dashboard for data visualization and job management.

## Installation

```bash
pip install -e .
```

## Development

```bash
pip install -e ".[dev,viz]"
pytest
```
