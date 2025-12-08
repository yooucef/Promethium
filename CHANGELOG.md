# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
*   Implementation of Physics-Informed Neural Networks (PINNs) for wave equation constrained reconstruction.
*   New `BenchmarkEngine` for standardized calculation of SSIM, PSNR, and SNR metrics.
*   Visualization component in Angular for interactive seismic trace viewing.
*   Comprehensive documentation suite including `benchmarking.md` and `ml-pipelines.md`.

### Changed
*   Restructured repository layout to `src/promethium` for better packaging.
*   Updated Angular frontend to version 17+ with the "Void/Neon" design system.
*   Refactored `SeismicDataset` to use `xarray` and `zarr` for improved I/O performance.

### Fixed
*   Resolved memory leaks in large-scale batch inference.
*   Fixed parsing issues with non-standard SEG-Y headers.

## [1.0.0] - 2024-01-01

### Added
*   Initial release of the Promethium framework.
*   Basic U-Net implementation for denoising.
*   FastAPI backend with basic job orchestration.
