# User Guide

This guide explains how to use Promethium to process seismic data.

## Prerequisites

- Access to a running Promethium instance (see Deployment Guide).
- Seismic data in SEG-Y format.

## Step 1: Accessing the Dashboard

Navigate to the web interface (default: `http://localhost:8000` or the configured ingress URL). You will see the main dashboard with two panels: **Dataset Registry** and **Processing Jobs**.

## Step 2: Ingesting Data

1. Locate the **Dataset Registry** panel.
2. Enter a friendly **Name** for the dataset.
3. Select the **Format** (e.g., `SEGY`).
4. Click **Choose File** and select your `.sgy` or `.segy` file.
5. Click **Upload**.
   - *Note*: Large files may take time. The system creates a memory map index upon upload.

## Step 3: Launching a Recovery Job

1. Locate the **Processing Jobs** panel.
2. Select your uploaded dataset from the dropdown menu.
3. Select the **Algorithm**:
   - **U-Net Reconstruction**: Best for complex structure recovery.
   - **Matrix Completion**: Best for randomly missing traces in dense surveys.
   - **Deconvolution**: Removes wavelet effects (shortens the pulse).
4. Click **Start Job**.
5. The job will appear in the list with `QUEUED` status, transitioning to `RUNNING` and then `COMPLETED`.

## Step 4: Viewing Results

(Feature In Development)
Once completed, the job entry will show a success status. Future versions will allow direct visualization in the "Interactive Visualization" area. Currently, results are saved to the backend storage directory defined in `DATA_STORAGE_PATH`.

## Troubleshooting

- **Upload Fails**: Ensure the file is a valid SEG-Y Standard Revision 1 file. Custom headers may cause parsing issues.
- **Job Fails**: Check the logs of the worker container. Common issues include insufficient memory for very large gathers or GPU OOM errors for U-Net inference on large patches.
