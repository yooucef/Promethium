import pytest
import numpy as np
from promethium.core.models import SeismicTrace, SeismicDataset, SeismicGather

def test_trace_creation():
    data = np.zeros(100)
    trace = SeismicTrace(data=data, sample_rate=0.004)
    assert trace.sample_rate == 0.004
    assert len(trace.time_axis) == 100

def test_gather_creation():
    data = np.zeros(100)
    traces = [SeismicTrace(data=data, sample_rate=0.004) for _ in range(5)]
    gather = SeismicGather(traces=traces)
    assert len(gather.traces) == 5

def test_dataset_import():
    import xarray as xr
    da = xr.DataArray(np.zeros((5, 100)))
    ds = SeismicDataset(data=da)
    assert ds.data.shape == (5, 100)
