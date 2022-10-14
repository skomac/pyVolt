import pywt
import numpy as np

from evaluation.evaluate import load_data, preprocess_all
from utils.plot import Plot


def flatten_coefficients_with_map(coeffs):
    index_map = []
    flattened = []
    for i, array in enumerate(coeffs):
        for j, coeff in enumerate(array):
            index_map.append((i, j))
            flattened.append(coeff)
    return flattened, index_map


def look_for_biggest_variance_dwt(data, number):
    print(np.shape(data))
    index_map = []
    all_coeffs = []
    for i, suite in enumerate(data):
        for j, curve in enumerate(suite):
            coeffs = pywt.wavedec(curve[1], 'db4')
            flattened, index_map = flatten_coefficients_with_map(coeffs)
            all_coeffs.append(flattened)

    all_coeffs = np.array(all_coeffs)

    print("Index map: ")
    print(index_map)
    print("Shape of index map:")
    print(np.shape(index_map))
    print("Shape of coeffs:")
    print(np.shape(all_coeffs))
    variances = []
    for i in range(0, np.shape(all_coeffs)[1]):
        variances.append(np.var(all_coeffs[:, i]))
    found_indices = np.argsort(variances)[np.size(variances) - number:]
    print("Shape of variances")
    print(np.shape(variances))
    print("Variances:")
    print(variances)
    print("indices of biggest variances")
    print(found_indices)
    mapped_indices_set = set()
    for index in found_indices:
        mapped_indices_set.add(index_map[index])
    print(mapped_indices_set)
    return mapped_indices_set


def main():
    target_dimensionality = 20

    initial_data = [
        "ml_sample_dataset_0",
        "ml_sample_dataset_1",
        "ml_sample_dataset_2"
    ]

    preprocessing_instructions = [
        [
            "SAVITZKY_GOLAY",
            17,
            2
        ],
        [
            "POLYNOMIAL_BASELINE",
            0.2,
            0.8,
            3
        ]
    ]
    data = load_data(initial_data)

    preprocessed = preprocess_all(data, preprocessing_instructions, "dwt_test")
    biggest_variance_tuples = look_for_biggest_variance_dwt(preprocessed, target_dimensionality)

    flat_coeffs_with_biggest_variance = []

    plot = Plot()
    for suite_id, suite in enumerate(preprocessed):
        for curve_id, curve in enumerate(suite):

            # print(np.shape(data[0][0][1]))
            sample_data = curve
            # for i in range(0, 24):
            #     print(np.shape(sample_data))
            #     print(np.shape([[sample_data[0][1000-1 + i] + 1.], [sample_data[1][1000-1]]]))
            #     sample_data = np.append(sample_data, [[sample_data[0][1000-1 + i] + 1.], [sample_data[1][1000-1]]], axis=1)
            #     print(np.shape(sample_data))
            sample_curve = sample_data[1]
            print(np.shape(sample_curve))
            # print(sample_curve)

            coeffs = pywt.wavedec(sample_curve, 'db4')

            coeffs_flattened = []
            for single_coeff_array in coeffs:
                for value in single_coeff_array:
                    coeffs_flattened.append(abs(value))

            # sorted = np.sort(coeffs_flattened, )
            # threshold = 0
            # if np.size(sorted) > 30:
            #     threshold = sorted[np.size(sorted) - 1 - 25]
            # print(sorted)

            flattened_target = []

            count = 0
            global_count = 0
            for i, single_coeff_array in enumerate(coeffs):
                for j, value in enumerate(single_coeff_array):
                    if (i, j) in biggest_variance_tuples:
                        count = count + 1
                        global_count = global_count + 1
                        flattened_target.append(value)
                    else:
                        coeffs[i][j] = 0
                print(count)
                count = 0

            flat_coeffs_with_biggest_variance.append(flattened_target)

            # print(coeffs)

            reconstructed = pywt.waverec(coeffs, 'db4')
            # print(reconstructed)

            print(global_count)

            if curve_id == 0:
                plot.add_plot(sample_data, "original")
                plot.add_plot([sample_data[0], reconstructed], "reconstructed")
    plot.show()
    print(np.shape(flat_coeffs_with_biggest_variance))
    print(np.array(flat_coeffs_with_biggest_variance))

    result = [[]]
    for flat_coeffs in flat_coeffs_with_biggest_variance:
        result[0].append([range(0, target_dimensionality), flat_coeffs])

    print("results:")
    print(result)
    print(np.shape(result))

    plot2 = Plot(xlim=[0, target_dimensionality])
    plot2.add_plot([range(0, target_dimensionality), flat_coeffs_with_biggest_variance[0]], "1.1")
    plot2.add_plot([range(0, target_dimensionality), flat_coeffs_with_biggest_variance[1]], "1.2")
    plot2.add_plot([range(0, target_dimensionality), flat_coeffs_with_biggest_variance[40]], "2.1")
    plot2.add_plot([range(0, target_dimensionality), flat_coeffs_with_biggest_variance[41]], "2.2")
    plot2.add_plot([range(0, target_dimensionality), flat_coeffs_with_biggest_variance[80]], "3.1")
    plot2.add_plot([range(0, target_dimensionality), flat_coeffs_with_biggest_variance[81]], "3.2")
    plot2.show()

    preprocessing_instructions2 = [
        [
            "NORMALIZE"
        ]
    ]
    normalized = preprocess_all(result, preprocessing_instructions2, "Normalization")
    plot3 = Plot(xlim=[0, target_dimensionality])
    plot3.add_plot(normalized[0][0], "1.1")
    plot3.add_plot(normalized[0][1], "1.2")
    plot3.add_plot(normalized[0][40], "2.1")
    plot3.add_plot(normalized[0][41], "2.2")
    plot3.add_plot(normalized[0][80], "3.1")
    plot3.add_plot(normalized[0][81], "3.2")
    plot3.show()

    no_in_suite = np.shape(data)[1]
    return [normalized[0][0:no_in_suite], normalized[0][no_in_suite:2*no_in_suite], normalized[0][2*no_in_suite:3*no_in_suite]]


if __name__ == '__main__':
    main()
