# User Guide

This guide describes how to use Promethium for storing, visualizing, and reconstructing seismic data.

## 1. Accessing the Dashboard

Navigate to `http://localhost:3000`. You will be greeted by the **Landing Page**, which displays system status and quick stats (Total Datasets, Active Jobs).

## 2. Managing Datasets

### Registering a Dataset
1.  Go to the **Datasets** view.
2.  Click **"Upload New"**.
3.  Select a standard **SEG-Y** file (`.sgy` or `.segy`).
4.  (Optional) Provide a meaningful name (e.g., `Gulf_of_Mexico_Block_A`).
5.  Click **Upload**. The file will be uploaded in parallel chunks for maximum speed.

### Inspecting Data
Once registered, click on a dataset card to open the **Seismic Viewer**.
*   **Trace View**: View individual traces.
*   **Gather View**: View 2D slices (Time vs Offset/Inline).
*   **Spectral View**: Analyze frequency content (Amplitude Spectrum).

## 3. Running Reconstruction Jobs

### Configuring a Job
1.  Navigate to **Jobs > New Job**.
2.  **Select Dataset**: Choose the input volume.
3.  **Select Model**:
    *   `UNet-Denoise`: For removing random noise.
    *   `PINN-Reconstruct`: For filling large gaps (trace interpolation) with physical constraints.
    *   `SuperRes-GAN`: For enhancing frequency (bandwidth extension).
4.  **Set Parameters**:
    *   `Patch Size`: Default `128`.
    *   `Overlap`: Default `0.25` (25%).
    *   `Device`: Select specific GPU ID if available.
5.  **Launch**: Click **Start Job**.

### Monitoring Progress
Go to the **Jobs** list.
*   **Status**: `QUEUED` -> `RUNNING` -> `COMPLETED`.
*   **Logs**: Click to see real-time inference logs.
*   **metrics**: Post-job, view SNR improvement and SSIM scores.

## 4. Comparing Results

1.  Open a completed Job.
2.  Click **"Compare"**.
3.  You will see a Split-Screen view:
    *   **Left**: Original Input.
    *   **Right**: Reconstructed Output.
    *   **Slider**: Drag to sweep between before/after.
4.  **Difference Map**: toggle to see the residual (what was added/removed).
