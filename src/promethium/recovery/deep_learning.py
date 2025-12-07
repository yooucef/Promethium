import torch
import torch.nn as nn
from .base import RecoveryAlgorithm
import numpy as np

class SimpleAutoencoder(nn.Module):
    def __init__(self, input_dim: int, latent_dim: int):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, latent_dim)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.ReLU(),
            nn.Linear(128, input_dim)
        )
        
    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)

class DLRecovery(RecoveryAlgorithm):
    """
    Wrapper for Deep Learning based recovery.
    """
    def __init__(self, epochs: int = 10, lr: float = 1e-3, device: str = 'cpu'):
        super().__init__()
        self.epochs = epochs
        self.lr = lr
        self.device = device
        self.model = None

    def fit(self, data: np.ndarray, mask: np.ndarray = None) -> 'DLRecovery':
        # Data shape: (n_traces, n_samples)
        n_traces, n_samples = data.shape
        self.model = SimpleAutoencoder(n_samples, latent_dim=32).to(self.device)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=self.lr)
        criterion = nn.MSELoss()
        
        # Simple training loop (unsupervised/self-supervised style)
        # Using observed data as target, zeroing out missing in input
        tensor_data = torch.from_numpy(data).float().to(self.device)
        tensor_mask = torch.from_numpy(mask).float().to(self.device) if mask is not None else torch.ones_like(tensor_data)
        
        self.model.train()
        for epoch in range(self.epochs):
            optimizer.zero_grad()
            
            # Input with missing values zeroed
            inputs = tensor_data * tensor_mask
            outputs = self.model(inputs)
            
            # Loss only on observed values
            loss = (criterion(outputs * tensor_mask, tensor_data * tensor_mask) / 
                    tensor_mask.sum()) # Normalize by mask sum
            # Note: simplistic loss calculation
            
            loss.backward()
            optimizer.step()
            
        return self

    def transform(self, data: np.ndarray, mask: np.ndarray = None) -> np.ndarray:
        self.model.eval()
        with torch.no_grad():
            tensor_data = torch.from_numpy(data).float().to(self.device)
            tensor_mask = torch.from_numpy(mask).float().to(self.device) if mask is not None else torch.ones_like(tensor_data)
            inputs = tensor_data * tensor_mask
            outputs = self.model(inputs)
            return outputs.cpu().numpy()
