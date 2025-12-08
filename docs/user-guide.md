# User Guide

This guide provides step-by-step instructions for interacting with the Promethium system.

## 1. Installation

Please refer to the [Deployment Guide](deployment-guide.md) for detailed installation instructions. Ensure you have the Docker stack running.

## 2. Accessing the Interface

Open your web browser and navigate to `http://localhost:4200`. You will see the main Dashboard.

## 3. Managing Datasets

### Registering a Dataset
1.  Navigate to the **Datasets** view.
2.  Click **"Upload / Register"**.
3.  Provide a name and the path to your SEG-Y file (must be accessible to the worker container).
4.  The system will index the file and generate metadata.

### Inspecting Data
Click on a dataset to view its header information, geometry (traces, samples, sampling rate), and a preview of the data.

## 4. Running a Job

### Configuration
1.  Navigate to **Jobs** > **New Job**.
2.  **Select Dataset**: Choose the source dataset.
3.  **Select Model**: Choose a model family (e.g., U-Net Denoising).
4.  **Hyperparameters**: Adjust parameters such as epochs, learning rate, or patch size.
5.  **Launch**: Click "Start Job".

### Monitoring
Go to the **Dashboard** or **Job Details** page to see the progress bar, real-time logs, and loss curves.

## 5. Visualizing Results

Once a job is complete, navigate to the **Visualization** tab.
*   **Split View**: Compare Input vs. Output.
*   **Difference Plot**: View the residuals (removed noise or added signal).
*   **Spectra**: Compare frequnecy contents.
