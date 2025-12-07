import numpy as np
from scipy.linalg import toeplitz, solve

def autocorrelation(x: np.ndarray, max_lag: int) -> np.ndarray:
    """Computes autocorrelation of x up to max_lag."""
    n = len(x)
    # Pad to power of 2 for efficiency if needed, but simple correlation here
    # Using numpy correlate
    full_corr = np.correlate(x, x, mode='full')
    mid = len(full_corr) // 2
    return full_corr[mid : mid + max_lag + 1]

def predictive_deconvolution(data: np.ndarray, operator_length: int, prediction_distance: int, white_noise: float = 0.1) -> np.ndarray:
    """
    Apply predictive deconvolution to a single trace.
    
    Args:
        data: Seismic trace data.
        operator_length: Length of the prediction operator (in samples).
        prediction_distance: Prediction distance (gap) in samples.
        white_noise: Pre-whitening percentage.
        
    Returns:
        Deconvolved trace.
    """
    # 1. Compute autocorrelation
    r = autocorrelation(data, operator_length + prediction_distance)
    
    # 2. Design Normal Equations (Yule-Walker) for prediction operator
    # We want to predict x[t+alpha] from x[t], x[t-1]...
    # R * a = g
    # Matrix R is Toeplitz of autocorrelation
    
    # Create R matrix
    R = toeplitz(r[:operator_length])
    
    # Add pre-whitening to diagonal
    R[np.diag_indices_from(R)] *= (1.0 + white_noise / 100.0)
    
    # RHS vector is autocorrelation shifted by prediction distance (alpha)
    # We are solving for the prediction filter 'a' that predicts the future sample.
    g = r[prediction_distance : prediction_distance + operator_length]
    
    # Solve R * a = g
    try:
        a = solve(R, g)
    except np.linalg.LinAlgError:
        # Fallback or return original if unstable
        return data

    # 3. Construct Error Filter (1, 0, ..., 0, -a)
    # The prediction error filter is f = [1, 0...0, -a] where -a is at lag alpha
    # Actually, specific implementation varies.
    # Standard predictive decon filter: 
    #   if alpha=1 (spiking), filter is inverse of wavelet.
    #   if alpha>1 (gap), filter removes periodic multiples.
    
    # Prediction error filter: e(t) = x(t) - x^(t)
    # x^(t) is predicted from past.
    # Filter f = [1, -a0, -a1, ... ] applied to x?
    # No, strictly: output = x(t) - convolution(x, a)
    # So filter is [1, 0, ..., 0] - [0, ..., 0, a]
    
    filter_kernel = np.zeros(prediction_distance + len(a))
    filter_kernel[0] = 1.0
    filter_kernel[prediction_distance:] = -a
    
    # 4. Apply filter
    deconvolved = np.convolve(data, filter_kernel, mode='same')
    return deconvolved
