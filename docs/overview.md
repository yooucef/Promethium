# Project Overview

## Problem Statement
Seismic data acquisition is often plagued by noise, missing traces, and irregular sampling due to environmental constraints, equipment limitations, or economic factors. High-quality seismic imaging relies on complete and clean wavefields. Traditional interpolation and denoising methods often struggle with complex geological structures or heavily aliased data.

## Promethium Mission
Promethium aims to bridge the gap between classical signal processing and modern Deep Learning. By leveraging state-of-the-art architectures like U-Nets and Physics-Informed Neural Networks (PINNs), Promethium reconstructs high-fidelity seismic data from sparse or noisy inputs, constrained by the governing physics of wave propagation.

## Design Principles
1.  **Accuracy**: Prioritize signal fidelity and structural preservation (SSIM) over perceptual smoothness.
2.  **Robustness**: Models must generalize across different surveys and acquisition geometries.
3.  **Scalability**: The system must handle terabyte-scale datasets via distributed processing.
4.  **Explainability**: Provide uncertainty estimates and physics-based validation metrics.

## Typical Workflows
1.  **Ingest**: Load SEG-Y data into a high-performance Zarr store.
2.  **Preprocess**: Apply gain, filtering, and normalization.
3.  **Train/Fine-tune**: Train a reconstruction model on a subset of the data or use a pretrained model.
4.  **reconstruct**: Run inference on the full volume to recover missing data.
5.  **Visualize**: Inspect the original, masking, and reconstruction side-by-side in the web dashboard.
