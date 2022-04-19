import sklearn
from scipy import signal as sig

import numpy as np
from utils.math import average_to_reduce
from utils.data import for_each_curve


def average_to_reduce_tmp(curve, target_dim):
    return np.array([np.arange(0, target_dim), average_to_reduce(curve[1], target_dim)])


def normalize_tmp(curve):
    curve[1] = sklearn.preprocessing.normalize(np.array([curve[1]]))[0]
    return curve


def preprocess(curve, instructions):
    preprocessed = curve[:]
    for instr in instructions:
        if instr[0] == "SAVITZKY_GOLAY":
            preprocessed = sig.savgol_filter(preprocessed, instr[1], instr[2])
        elif instr[0] == "REDUCE_DIMENSIONALITY_AVERAGING":
            preprocessed = np.array([np.arange(0, instr[1]), average_to_reduce(preprocessed[1], instr[1])])
        elif instr[0] == "NORMALIZE":
            preprocessed[1] = sklearn.preprocessing.normalize(np.array([preprocessed[1]]))[0]

    return preprocessed


def preprocess_all_with_instr(data, instr):
    # given data may be lost
    if instr[0] == "SAVITZKY_GOLAY":
        for_each_curve(data, sig.savgol_filter, instr[1], instr[2])
    elif instr[0] == "REDUCE_DIMENSIONALITY_AVERAGING":
        for_each_curve(data, average_to_reduce_tmp, instr[1], shape_change=True)
    elif instr[0] == "NORMALIZE":
        for_each_curve(data, normalize_tmp)

    return data

