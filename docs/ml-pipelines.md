# ML Pipelines

Promethium integrates Deep Learning for advanced seismic reconstruction tasks, specifically focusing on data interpolation (inpainting) and denoising.

## Models

### U-Net
The primary driver for reconstruction is a 2D U-Net architecture (`src/promethium/ml/models.py`).
- **Input**: 1-channel seismic patches (Time x Trace), normalized.
- **Output**: Reconstructed patches.
- **Loss Function**: MSE (Mean Squared Error) between reconstructed and ground truth (or observed) data.

### Autoencoders (Planned)
Denoising autoencoders are planned for unsupervised noise attenuation tasks.

## Training Pipeline

The training logic is encapsulated in `src/promethium/ml/training.py`.

### Data Loading
Data is ingested via `SeismicTorchDataset` (`src/promethium/ml/data.py`).
- **Patching**: Large seismic sections are sliced into fixed-size patches (e.g., 64x64).
- **Augmentation**:
  - **Trace Masking**: Simulates missing traces during training to teach the network to interpolate.
  - **Noise Injection**: Adds Gaussian noise for robustness.

### Execution
Training can be triggered programmatically or via the Job API by passing specific parameters. The worker node utilizes GPU resources if `torch.cuda.is_available()` is true.

## Evaluation Metrics

- **MSE (Mean Squared Error)**: Pixel-wise difference.
- **PSNR (Peak Signal-to-Noise Ratio)**: Quality of reconstruction relative to signal power.
- **SSIM (Structural Similarity Index)**: Perceptual quality metric (planned).
