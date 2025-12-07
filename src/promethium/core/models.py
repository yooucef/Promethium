from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
import numpy as np
import xarray as xr

@dataclass
class SeismicTrace:
    """
    Represents a single seismic trace.
    """
    data: np.ndarray
    sample_rate: float
    start_time: float = 0.0
    headers: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def time_axis(self) -> np.ndarray:
        return self.start_time + np.arange(len(self.data)) * self.sample_rate

@dataclass
class SeismicGather:
    """
    Represents a collection of traces (e.g., shot gather, receiver gather).
    """
    traces: List[SeismicTrace]
    gather_type: str = "shot"  # shot, receiver, cmp, etc.
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dataframe(self):
        # Implementation for conversion to pandas DataFrame or similar for easier inspection
        pass

    def to_xarray(self) -> xr.DataArray:
        # data = np.stack([t.data for t in self.traces])
        # Construct xarray with dimensions (trace, time)
        pass

class SeismicDataset:
    """
    Main container for a seismic dataset.
    Abstracts over memory-resident or disk-backed data.
    """
    def __init__(self, data: xr.DataArray | Any, metadata: Dict[str, Any] = None):
        self._data = data
        self.metadata = metadata or {}

    @property
    def data(self):
        return self._data
    
    def __repr__(self):
        return f"SeismicDataset(shape={self._data.shape}, metadata={self.metadata.keys()})"
