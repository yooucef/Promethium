# Benchmarking Methodology 📉

Promethium emphasizes rigorous quantitative evaluation. The `BenchmarkEngine` (`src/promethium/ml/benchmark.py`) computes standard metrics to track model performance.

## Key Metrics

### 1. Signal-to-Noise Ratio (SNR)
*   **Definition**: Ratio of signal power to noise power, in Decibels (dB).
*   **Goal**: Maximize. Typically > 15dB for high quality.
*   **Formula**: $10 \cdot \log_{10}(\frac{\sum y^2}{\sum (y - \hat{y})^2})$

### 2. Structural Similarity Index (SSIM)
*   **Definition**: Perceptual metric measuring similarity in luminance, contrast, and structure.
*   **Goal**: Maximize (Close to 1.0).
*   **Relevance**: Critical for seismic checking if reflector continuity is preserved.

### 3. Peak Signal-to-Noise Ratio (PSNR)
*   **Definition**: Ratio of maximum possible power to noise power.
*   **Goal**: Maximize.

### 4. Mean Squared Error (MSE)
*   **Definition**: Pixel-wise squared difference.
*   **Goal**: Minimize. Used as the primary training loss for many models.

## Running Benchmarks

Benchmarks are run automatically after training or can be triggered manually via the CLI (future) or API.

```python
from promethium.ml.benchmark import BenchmarkEngine
from promethium.ml.data.dataset import SeismicDataset

# Load Data
dataset = SeismicDataset("path/to/test_data.zarr")

# Initialize Engine
engine = BenchmarkEngine(model_config={...}, checkpoint_path="...")

# Run
metrics = engine.evaluate_dataset(dataset)
print(metrics)
# Output: {'mse': 0.002, 'ssim': 0.89, 'snr': 18.5}
```
