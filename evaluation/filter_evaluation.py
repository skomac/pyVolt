from processing.assessment import signal_recovery, rmse
from utils.filesystem import save_csv_plot


def signal_recovery_evaluation(data, preprocessed, raws):
    result = []
    for suite_data, suite_proc, raw in zip(data, preprocessed, raws):
        for curve_data, curve_proc in zip(suite_data, suite_proc):
            result.append(signal_recovery(raw, curve_data, curve_proc))
    return result


def rmse_evaluation(data, preprocessed, raws):
    result = []
    for suite_data, suite_proc, raw in zip(data, preprocessed, raws):
        for curve_data, curve_proc in zip(suite_data, suite_proc):
            result_original = rmse(raw, curve_data)
            result_preprocessed = rmse(raw, curve_proc)
            result.append([result_original, result_preprocessed])
    return result