import segyio
import numpy as np
from pathlib import Path
from typing import Union, Dict, Any, Optional
from promethium.core.models import SeismicDataset
from promethium.core.exceptions import DataIngestionError
from promethium.core.logging import logger
import mmap

def validate_segy(file_path: Path) -> bool:
    """
    Validates if the file is a readable SEG-Y.
    """
    try:
        with segyio.open(str(file_path), ignore_geometry=True) as f:
            return True
    except Exception:
        return False

def read_segy_robust(
    file_path: Union[str, Path], 
    strict: bool = False,
    memory_map: bool = True
) -> SeismicDataset:
    """
    Reads a SEG-Y file with production-grade robustness.
    
    Args:
        file_path: Path to the SEG-Y file.
        strict: Enforce strict SEG-Y standard compliance.
        memory_map: Use memory mapping for large files.
        
    Returns:
        SeismicDataset with xarray wrapper.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise DataIngestionError(f"File not found: {file_path}")

    try:
        # Check size for memory mapping decision logic if needed
        # Open with segyio
        with segyio.open(str(file_path), ignore_geometry=True, strict=strict) as f:
            # Metadata extraction
            n_traces = f.tracecount
            n_samples = f.samples.size
            if n_traces == 0 or n_samples == 0:
                raise DataIngestionError("SEG-Y file appears empty.")

            sample_rate = segyio.tools.dt(f) / 1000.0
            
            # Text header
            try:
                text_header = segyio.tools.wrap(f.text[0])
            except Exception:
                text_header = "Header unavailable"

            # Loading strategy
            if memory_map:
                # segyio provides a memmap interface or we can trust OS paging for 'raw'
                # Note: f.trace.raw returns a numpy array which copies unless using mmap explicitly
                # For robust integration with xarray/dask, simpler is often better:
                data = f.trace.raw[:] # In-memory load for now, dask integration later if >RAM
            else:
                data = f.trace.raw[:]

            metadata = {
                "n_traces": n_traces,
                "n_samples": n_samples,
                "sample_rate": sample_rate,
                "text_header": text_header,
                "filepath": str(file_path)
            }
            
            import xarray as xr
            da = xr.DataArray(
                data,
                dims=("trace", "time"),
                coords={
                    "trace": np.arange(n_traces),
                    "time": f.samples
                },
                name="amplitude",
                attrs=metadata
            )
            
            logger.info(f"Successfully loaded SEG-Y: {file_path} ({n_traces}x{n_samples})")
            return SeismicDataset(data=da, metadata=metadata)

    except Exception as e:
        logger.error(f"SEG-Y ingestion failed for {file_path}: {e}")
        raise DataIngestionError(f"Critical error reading SEG-Y: {e}") from e
