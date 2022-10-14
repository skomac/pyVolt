import numpy as np


def residual_curve(signal_ideal, signal_non_ideal):
    residual = np.copy(signal_non_ideal)
    residual[1] = residual[1] - signal_ideal[1]
    return residual


def residual_num(signal_ideal, signal_non_ideal):
    residual = residual_curve(signal_ideal, signal_non_ideal)
    return np.sqrt(np.sum(residual[1] * residual[1]))


def signal_recovery(signal_ideal, signal_noisy, signal_filtered):
    return 1 - residual_num(signal_ideal, signal_filtered) / residual_num(signal_ideal, signal_noisy)


def rmse(signal_ideal, signal_noisy):
    return residual_num(signal_ideal, signal_noisy) / np.sqrt(np.size(signal_ideal[1]))