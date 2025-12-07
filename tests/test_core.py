import pytest
import numpy as np
import xarray as xr
from promethium.core.models import SeismicDataset, SeismicTrace
from promethium.io.readers import read_segy_robust
from promethium.core.exceptions import DataIngestionError
from pathlib import Path

def test_seismic_trace_creation():
    data = np.zeros(100)
    trace = SeismicTrace(data=data, sample_rate=0.002)
    assert trace.sample_rate == 0.002
    assert len(trace.time_axis) == 100
    assert trace.time_axis[-1] == 0.002 * 99

def test_seismic_dataset_creation():
    data = xr.DataArray(np.zeros((10, 100)), dims=("trace", "time"))
    dataset = SeismicDataset(data=data, metadata={"test": True})
    assert dataset.metadata["test"] is True
    assert dataset.data.shape == (10, 100)

def test_read_segy_missing_file():
    with pytest.raises(DataIngestionError):
        read_segy_robust("non_existent_file.sgy")

def test_read_segy_mock(tmp_path):
    # We can't easily generate a valid binary SEG-Y without segyio writing it first.
    # For now, we test that it attempts to read and handles errors gracefully 
    # or use a check for file existence
    f = tmp_path / "fake.sgy"
    f.touch()
    # segyio.open should fail on empty file
    with pytest.raises(DataIngestionError):
        read_segy_robust(f)
