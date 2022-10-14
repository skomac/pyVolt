from scipy import signal as sig
import numpy as np

from processing.baseline_correction import polynomial_baseline_correction, cppl_correction
from processing.slope_sweep import slope_sweep_baseline
from utils.math import average_to_reduce, normalize
from utils.data import for_each_curve, for_each_curve_modify_shape
from utils.plot import Plot


def preprocess_all_with_instr(data, instr):
    # given data may be lost
    if instr[0] == "SAVITZKY_GOLAY":
        return for_each_curve(data, sig.savgol_filter, instr[1], instr[2])
    elif instr[0] == "REDUCE_DIMENSIONALITY_AVERAGING":
        return for_each_curve_modify_shape(data, average_to_reduce, instr[1])
    elif instr[0] == "NORMALIZE":
        return for_each_curve(data, normalize)
    elif instr[0] == "POLYNOMIAL_BASELINE":
        plot = Plot()
        processed = polynomial_baseline_correction(data, instr, plot)
        # plot.show()
        return processed
    elif instr[0] == "CPPL":
        plot = Plot()
        processed = cppl_correction(data, instr)
        # plot.show()
        return processed

