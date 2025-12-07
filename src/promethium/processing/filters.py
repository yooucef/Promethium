import numpy as np
from scipy.signal import butter, sosfilt, filtfilt
from typing import Optional

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    sos = butter(order, [low, high], btype='band', output='sos')
    return sos

def bandpass_filter(data: np.ndarray, lowcut: float, highcut: float, fs: float, order: int = 5, zero_phase: bool = True) -> np.ndarray:
    """
    Apply a Butterworth bandpass filter.
    
    Args:
        data: input 1D array.
        lowcut: Low cut frequency in Hz.
        highcut: High cut frequency in Hz.
        fs: Sampling frequency in Hz.
        order: Order of the filter.
        zero_phase: If True, uses filtfilt (zero phase), else using sosfilt.
    """
    sos = butter_bandpass(lowcut, highcut, fs, order=order)
    if zero_phase:
        return filtfilt(sos[0], sos[1], data, padlen=None) # Note: filtfilt usually takes b, a, but SOS support varies. 
        # Actually filtfilt with sos uses different signature in new scipy.
        # Let's use the sosfiltfilt if available or convert.
        from scipy.signal import sosfiltfilt
        return sosfiltfilt(sos, data)
    else:
        return sosfilt(sos, data)

def lowpass_filter(data: np.ndarray, cutoff: float, fs: float, order: int = 5) -> np.ndarray:
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)

def highpass_filter(data: np.ndarray, cutoff: float, fs: float, order: int = 5) -> np.ndarray:
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return filtfilt(b, a, data)
