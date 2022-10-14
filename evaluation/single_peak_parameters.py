import numpy as np


def collect_single_peak_params(signal):
    maximum = np.max(signal[1])
    max_pos = signal[0][np.argmax(signal[1])]

    max_index = np.argmax(signal[1])
    idx = max_index
    while signal[1][idx] > 0.5 * signal[1][max_index]:
        idx = idx - 1
    half_peak_pos_left = signal[0][idx]
    idx = max_index
    while signal[1][idx] > 0.5 * signal[1][max_index]:
        idx = idx + 1
    half_peak_pos_right = signal[0][idx]

    half_peak_width = half_peak_pos_right - half_peak_pos_left

    return {'peak_position': max_pos, 'peak_value': maximum, 'half_peak_width': half_peak_width}
