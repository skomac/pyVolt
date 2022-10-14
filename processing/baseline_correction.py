import numpy as np

from processing.slope_sweep import slope_sweep_baseline


def cppl_correction(data, instruction):
    first_curve = data[0][0]
    baseline, _ = slope_sweep_baseline(first_curve)

    preprocessed = np.zeros(np.shape(data))
    for suite_id, suite in enumerate(data):
        for i, curve in enumerate(suite):
            preprocessed[suite_id][i][0] = curve[0]
            preprocessed[suite_id][i][1] = curve[1] - baseline[1]

    return preprocessed


def polynomial_baseline_correction(data, instruction, plot):
    curve_size = np.size(data[0][0][0])
    low_cutoff = int(np.floor(instruction[1] * curve_size))
    high_cutoff = int(np.ceil(instruction[2] * curve_size))

    first_curve = data[0][0]
    reduced_x = np.append(first_curve[0][0:low_cutoff], first_curve[0][high_cutoff:curve_size])
    reduced_y = np.append(first_curve[1][0:low_cutoff], first_curve[1][high_cutoff:curve_size])
    fit = np.polyfit(reduced_x, reduced_y, instruction[3])
    fitted_y = np.polyval(fit, np.array(first_curve[0], dtype=object))

    preprocessed = np.zeros(np.shape(data))
    for suite_id, suite in enumerate(data):
        for i, curve in enumerate(suite):
            preprocessed[suite_id][i][0] = curve[0]
            preprocessed[suite_id][i][1] = curve[1]-fitted_y

    # plot.add_plot(first_curve, "Pierwotna krzywa")
    # plot.add_plot([first_curve[0], fitted_y], "Wielomianowa linia bazowa", thick=True)
    # plot.add_plot([first_curve[0], preprocessed[0][0][1]], "Skorygowana krzywa")
    #
    # # if __name__ == '__main__':
    # plot.show()
    return preprocessed