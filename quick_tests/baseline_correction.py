from evaluation.evaluate import load_data, preprocess_all

import numpy as np

from utils.plot import Plot

from processing.baseline_correction import polynomial_baseline_correction


def sample_baseline_correction():
    initial_data = [
        "sample_name_of_test_suite"
    ]

    data = load_data(initial_data)

    print(np.shape(data))

    preprocessing_instructions = [
        [
            "POLYNOMIAL_BASELINE",
            0.2,
            0.8,
            3
        ]
    ]

    preprocessed = preprocess_all(data, preprocessing_instructions, "baseline")

    plot = Plot()
    polynomial_baseline_correction(data, preprocessing_instructions[0], plot)
    plot.show()


if __name__ == '__main__':
    sample_baseline_correction()