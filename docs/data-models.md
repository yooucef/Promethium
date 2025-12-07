# Data Models

Core data structures used within Promethium.

## Core Library

### `SeismicTrace`
Represents a single 1D time-series.
- `data`: numpy array (float32).
- `sample_rate`: float (seconds).
- `start_time`: float.
- `headers`: Dictionary of trace headers (cdp, offset, etc.).

### `SeismicDataset`
Represents a collection of traces (2D/3D volume).
- `data`: `xarray.DataArray` wrapping the numpy/mmap data.
  - Dimensions: `(trace, time)`.
  - Coordinates: `trace` index, `time` axis.
- `metadata`: Global survey info.

## Database Models

### `Dataset`
PostgreSQL registry entry.
- `id`: Integer PK.
- `file_path`: Absolute path on disk.
- `format`: String enum (SEGY, etc.).

### `Job`
Processing task record.
- `id`: UUID.
- `status`: QUEUED, RUNNING, COMPLETED, FAILED.
- `algorithm`: Identifier string.
- `params`: JSON parameter blob.
