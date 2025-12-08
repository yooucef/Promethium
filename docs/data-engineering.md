# Data Engineering

Promethium's data engineering layer is designed for high-throughput access to seismic data, enabling efficient training of Deep Learning models.

## Data Formats

### SEG-Y
The industry standard format. Promethium uses `segyio` for header parsing and trace reading. While widely used, SEG-Y is row-oriented and not optimized for the random access patterns required by sliding-window inference or patch-based training.

### Zarr
Promethium converts ingested SEG-Y files into **Zarr** arrays. Zarr is a cloud-native, chunked, compressed format.
*   **Chunking**: Data is split into multi-dimensional chunks (e.g., `128x128` blocks).
*   **Access**: This allows independent retrieval of small patches without reading the entire file, drastically reducing I/O latency during training.
*   **Storage**: Zarr stores can be kept on local disk or object storage (S3, GCS).

## Pipelines

### Ingestion Pipeline
1.  **Validation**: Check SEG-Y headers for consistency.
2.  **Conversion**: Write trace data to Zarr chunks.
3.  **Metadata Extraction**: Store geometry (inlines, crosslines) in PostgreSQL.

### Preprocessing Pipeline
Implemented via `src/promethium/signal/transforms.py`.
*   **Normalization**: RMS, Min-Max, or Standard Score normalization.
*   **Agumentation**: Random flips, gains, and time shifts applied dynamically during data loading.

## Lineage & Governance
Every artifact produced by Promethium is linked to:
*   The source dataset ID.
*   The specific model configuration snapshot.
*   The software version (Git commit hash).
This ensures full reproducibility of results.
