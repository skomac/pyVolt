import numpy as np

from processing.assessment import signal_recovery, rmse
from utils.filesystem import save_csv_plot
from utils.plot import Plot


def signal_recovery_evaluation(data, preprocessed, raws):
    result = []
    for suite_data, suite_proc, raw in zip(data, preprocessed, raws):
        for curve_data, curve_proc in zip(suite_data, suite_proc):
            result.append(signal_recovery(raw, curve_data, curve_proc))
    return result


def rmse_evaluation(suite_data, suite_preprocessed, noise_data, baseline_data, sample_collection):
    results_overall_corr = []
    results_noise_corr = []
    results_baseline_corr = []
    for curve_data, curve_proc, curve_noise, curve_baseline in zip(suite_data, suite_preprocessed, noise_data, baseline_data):
        result_original = rmse(sample_collection["unmodified"], curve_data)
        result_preprocessed = rmse(sample_collection["unmodified"], curve_proc)
        results_overall_corr.append([result_original, result_preprocessed])
        # plot = Plot()
        # plot.add_plot(sample_collection["unmodified"], "unmodified")
        # plot.add_plot(curve_data, "data")
        # plot.add_plot(curve_proc, "processed")
        # print(f"original: {result_original}")
        # print(f"processed: {result_preprocessed}")
        # plot.show()

        only_baseline_added = np.copy(sample_collection["unmodified"])
        only_baseline_added[1] = only_baseline_added[1] + curve_baseline[1]
        result_original = rmse(only_baseline_added, curve_data)
        result_preprocessed = rmse(only_baseline_added, curve_proc)
        results_noise_corr.append([result_original, result_preprocessed])
        print(result_original)
        print(result_preprocessed)

        # plot = Plot()
        # plot.add_plot(only_baseline_added, "only_baseline_added")
        # plot.add_plot(curve_data, "data")
        # plot.add_plot(curve_proc, "processed")
        # print(f"original: {result_original}")
        # print(f"processed: {result_preprocessed}")
        # plot.show()

        only_noise_added = np.copy(sample_collection["unmodified"])
        only_noise_added[1] = only_noise_added[1] + curve_noise[1]
        result_original = rmse(only_noise_added, curve_data)
        result_preprocessed = rmse(only_noise_added, curve_proc)
        results_baseline_corr.append([result_original, result_preprocessed])

        # plot = Plot()
        # plot.add_plot(only_noise_added, "only_noise_added")
        # plot.add_plot(curve_data, "data")
        # plot.add_plot(curve_proc, "processed")
        # print(f"original: {result_original}")
        # print(f"processed: {result_preprocessed}")
        # plot.show()

    return {"overall_corr": np.average(results_overall_corr, 0), "noise_corr": np.average(results_noise_corr, 0),
            "baseline_corr": np.average(results_baseline_corr, 0)}
    # return {"overall_corr": results_overall_corr, "noise_corr": results_noise_corr,
    #         "baseline_corr": results_baseline_corr}
