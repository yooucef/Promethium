import pytest
import torch
import numpy as np
from promethium.ml.models import UNet
from promethium.ml.data import SeismicTorchDataset

def test_unet_shape():
    model = UNet(n_channels=1, n_classes=1)
    x = torch.randn(1, 1, 64, 64)
    y = model(x)
    assert y.shape == (1, 1, 64, 64)

def test_dataset_item():
    data = np.random.randn(100, 100)
    ds = SeismicTorchDataset(data, patch_size=(32, 32), stride=(32, 32))
    img, mask = ds[0]
    assert img.shape == (1, 32, 32)
    assert mask.shape == (1, 32, 32)
