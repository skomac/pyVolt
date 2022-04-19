import numpy as np


def polynomial_baseline_correction(data, preprocessing_instructions, plot):
    curve_size = np.size(data[0][0][0])
    low_cutoff = int(np.floor(preprocessing_instructions[0][1] * curve_size))
    high_cutoff = int(np.ceil(preprocessing_instructions[0][2] * curve_size))

    first_curve = data[0][0]
    reduced_x = np.append(first_curve[0][0:low_cutoff], first_curve[0][high_cutoff:curve_size])
    reduced_y = np.append(first_curve[1][0:low_cutoff], first_curve[1][high_cutoff:curve_size])
    fit = np.polyfit(reduced_x, reduced_y, preprocessing_instructions[0][3])
    fitted_y = np.polyval(fit, np.array(first_curve[0], dtype=object))

    preprocessed = np.zeros(np.shape(data))
    for suite_id, suite in enumerate(data):
        for i, curve in enumerate(suite):
            preprocessed[suite_id][i][0] = curve[0]
            preprocessed[suite_id][i][1] = curve[1]-fitted_y

    plot.add_plot(first_curve, "Original")
    plot.add_plot([first_curve[0], fitted_y], "fitted", thick=True)
    plot.add_plot([first_curve[0], preprocessed[0][0][1]], "adjusted")

    if __name__ == '__main__':
        plot.show()
    return preprocessed