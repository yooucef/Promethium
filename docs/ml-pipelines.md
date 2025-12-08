# AI/ML Pipelines & Models 🧠

Promethium implements state-of-the-art architectures tailored for seismic signal processing.

## Model Families

All models inherit from `PromethiumModel` and are instantiated via the `ModelRegistry`.

### 1. U-Net (Reconstruction & Inpainting)
*   **Purpose**: General-purpose signal recovery, missing trace interpolation.
*   **Architecture**: Encoder-Decoder with skip connections.
*   **SoTA Features**:
    *   Residual Blocks in encoder/decoder.
    *   Optional Attention Gates for focusing on wavefronts.
    *   Support for 1D (Trace), 2D (Gather), and 3D (Cube) inputs.

### 2. Autoencoder (Denoising)
*   **Purpose**: Suppressing random and coherent noise.
*   **Architecture**: Deep Convolutional Autoencoder (DAE).
*   **Mechanism**: Compresses input to a latent representation, filtering out high-frequency noise that doesn't fit the learned manifold of valid seismic signals.

### 3. PINN (Physics-Informed)
*   **Purpose**: Ensuring physical consistency of reconstructions.
*   **Mechanism**: Adds a "Physics Loss" term to the standard objective.
*   **Equation**: Acoustic Wave Equation $u_{tt} = c^2 \nabla^2 u$.
*   **Implementation**: `WaveEquationLoss` in `src/promethium/ml/loss.py` uses finite-difference kernels to penalize violations of the wave equation.

## Training Pipeline

The training process is standardized via `src/promethium/ml/train.py`.

1.  **Config**: Hydrated from YAML or API Request.
2.  **Data Loading**: 
    *   `SeismicDataset` lazily reads Zarr chunks.
    *   **Augmentation**: Random Polarity Flip, Gain, Time Shift applied on-the-fly (`transforms.py`).
3.  **Loop**: PyTorch Lightning handles Epochs, Validation, and Checkpointing.
4.  **Logging**: Matrices pushed to MLFlow/Tensorboard.

## Inference Pipeline

Inference (`src/promethium/ml/inference.py`) is designed for production scale.

*   **Patch-Based**: Large volumes are broken into overlapping patches (e.g., 128x128).
*   **Cosine Blending**: Overlapping regions are blended using a cosine window to eliminate blocking artifacts at patch boundaries.
*   **Batched**: Patches are batched for maximum GPU throughput.
