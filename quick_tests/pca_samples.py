import numpy as np

from evaluation.evaluate import load_data, preprocess_all
import pca_poc as pca
import baseline_correction as base
from utils.plot import Plot

if __name__ == '__main__':
    # initial_data = [
    #     "pca_sample_dataset_0",
    #     "pca_sample_dataset_1",
    #     "pca_sample_dataset_2"
    # ]

    initial_data = [
        "ml_sample_dataset_0",
        "ml_sample_dataset_1",
        "ml_sample_dataset_2"
    ]

    baseline_correction_instructions = [
        [
            "POLYNOMIAL_BASELINE",
            0.15,
            0.85,
            3
        ]
    ]

    digital_filtering_instructions = [
        [
            "SAVITZKY_GOLAY",
            31,
            2
        ]
    ]

    raw_data = load_data(initial_data)

    plot = Plot()
    baseline_corrected = base.polynomial_baseline_correction(np.copy(raw_data), baseline_correction_instructions[0],
                                                             plot)

    only_filtered = preprocess_all(np.copy(raw_data), digital_filtering_instructions, "filtered")

    everything_done = base.polynomial_baseline_correction(np.copy(only_filtered), baseline_correction_instructions[0],
                                                          plot)

    print(np.shape(raw_data))
    print(np.shape(baseline_corrected))
    print(np.shape(only_filtered))
    print(np.shape(everything_done))

    for i in range(0, 3):
        examples_plot = Plot()
        examples_plot.add_plot(raw_data[i][0], "Oryginalna krzywa")
        examples_plot.add_plot(only_filtered[i][0], "Tylko filtracja cyfrowa", thick=True)
        examples_plot.add_plot(baseline_corrected[i][0], "Tylko korekcja linii bazowej")
        examples_plot.add_plot(everything_done[i][0], "Filtracja cyfrowa oraz korekcja linii bazowej", thick=True)
        examples_plot.show()

    pca.pca_analysis(raw_data)
    pca.pca_analysis(baseline_corrected)
    pca.pca_analysis(only_filtered)
    pca.pca_analysis(everything_done)
