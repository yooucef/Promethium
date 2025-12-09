# Kaggle Integration Guide

Promethium is designed to be **Kaggle-native**, meaning it can be used seamlessly in Kaggle notebooks both with and without internet access.

This guide explains how to use Promethium in Kaggle competitions and kernels using **Pip-less Source Imports** or **Offline Wheel Installation**.

---

## 1. Dataset Strategy

To use Promethium without downloading it from PyPI every time (or for offline competitions), you should attach one of the following Kaggle Datasets to your notebook.

### A. Wheel Dataset (Recommended for Stability)
This dataset contains the pre-built `.whl` file.

*   **Dataset Name**: `promethium-seismic-wheel-1.0.3` (or current version)
*   **Contents**:
    *   `promethium_seismic-1.0.3-py3-none-any.whl`
*   **Path in Kernel**: `../input/promethium-seismic-wheel-100/`

### B. Source Dataset (Recommended for Development)
This dataset contains the raw source code.

*   **Dataset Name**: `promethium-seismic-source-1.0.3`
*   **Contents**:
    *   `promethium/` (The package directory)
*   **Path in Kernel**: `../input/promethium-seismic-source-100/`

---

## 2. Usage Patterns

### Mode A: Standard PyPI (Network Required)
If your notebook has internet access, you can simply install from PyPI.

```python
!pip install promethium-seismic==1.0.3
import promethium
```

### Mode B: Offline Wheel Install (No Network)
Fastest installation method. Does not require internet.

```python
# Install from the attached Wheel dataset
!pip install ../input/promethium-seismic-wheel-100/promethium_seismic-1.0.3-py3-none-any.whl

import promethium
```

### Mode C: Pip-less Source Import (Zero Install)
Directly import the code from the dataset source. Useful if you want to modify code on the fly or avoid any installation overhead.

```python
import sys

# Add the dataset path to sys.path
SOURCE_ROOT = "/kaggle/input/promethium-seismic-source-100"
if SOURCE_ROOT not in sys.path:
    sys.path.append(SOURCE_ROOT)

import promethium
```

---

## 3. Best Practices for Kaggle

### GPU Selection
Promethium automatically detects GPUs. You can explicitly manage devices using:
```python
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
```

### Memory Management
Kaggle kernels often have limited RAM (13-30GB).
*   Use `SeismicRecoveryPipeline` with `batch_size` configurations if processing large surveys.
*   Avoid loading entire SEG-Y files into memory if possible; use memmapped reading (default in `segyio`).

### Output Data
Always write your results to `/kaggle/working/`.
```python
output_path = "/kaggle/working/reconstructed_data.sgy"
promethium.io.write_segy(data, output_path)
```
