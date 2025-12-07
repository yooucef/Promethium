import numpy as np
from .base import RecoveryAlgorithm

class SoftImpute(RecoveryAlgorithm):
    """
    Basic implementation of Soft Impute algorithm for Matrix Completion.
    Minimizes ||X - M||_F^2 + lambda * ||X||_*
    """
    def __init__(self, lamb: float = 0.1, max_iters: int = 100, tol: float = 1e-5):
        super().__init__()
        self.lamb = lamb
        self.max_iters = max_iters
        self.tol = tol
        self.X_reconstructed = None

    def fit(self, data: np.ndarray, mask: np.ndarray = None) -> 'SoftImpute':
        if mask is None:
            mask = ~np.isnan(data)
            
        # Initialize X with zeros or mean
        X_old = np.zeros_like(data)
        X_old[mask] = data[mask]
        
        for i in range(self.max_iters):
            # SVD
            U, s, Vt = np.linalg.svd(X_old, full_matrices=False)
            
            # Soft thresholding of singular values
            s_thresh = np.maximum(s - self.lamb, 0)
            
            # Reconstruct
            X_new = np.dot(U * s_thresh, Vt)
            
            # Enforce consistency with observed data
            X_new[mask] = data[mask]
            
            # Check convergence
            diff = np.linalg.norm(X_new - X_old) / (np.linalg.norm(X_old) + 1e-9)
            if diff < self.tol:
                break
            
            X_old = X_new
            
        self.X_reconstructed = X_old
        return self

    def transform(self, data: np.ndarray, mask: np.ndarray = None) -> np.ndarray:
        if self.X_reconstructed is None:
            raise RuntimeError("Model must be fitted before calling transform")
        return self.X_reconstructed
