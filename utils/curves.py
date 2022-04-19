import numpy as np


def generate_series_of_curves(sample, multipliers):
    signals = np.array([sample])
    for i in multipliers:
        next_signal = np.copy(sample)
        next_signal[1] = next_signal[1] * i
        signals = np.concatenate((signals, np.array([next_signal])), axis=0)
    return signals[1:]


def get_maxima_from_series(signals):
    maxima = np.zeros(np.shape(signals)[0])
    i = 0
    for signal in signals:
        maxima[i] = np.max(signals[i][1])
        i += 1
    return maxima