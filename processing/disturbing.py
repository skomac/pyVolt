import numpy as np


def disturb(signal, fraction):
    noise = np.copy(signal)
    noise[1] = np.max(signal[1]) * fraction * np.random.default_rng().normal(
        size=np.size(signal[1]))
    signal[1] = signal[1] + noise[1]
    return signal, noise
