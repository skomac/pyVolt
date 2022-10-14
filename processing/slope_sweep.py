import numpy as np
from matplotlib import pyplot as plt
from numpy import polyfit, polyval

from results.results import results_prep_dir, results_eval_dir, results_final_dir
from utils.filesystem import load_csv_plot, ensure_dir_creation


def slope(pointA, pointB, curve):
    if pointA == pointB:
        print("slope:ERROR: pointA==pointB")
        return 0
    return (curve[1][pointB] - curve[1][pointA]) / (curve[0][pointB] - curve[0][pointA])


def slope_sweep_points(curve):
    points_and_slope = [(0, -1e200)]
    for i in range(1, np.size(curve[0])):
        current_slope = slope(points_and_slope[-1][0], i, curve)
        while current_slope <= points_and_slope[-1][1]:
            points_and_slope.pop()
            current_slope = slope(points_and_slope[-1][0], i, curve)
        points_and_slope.append((i, current_slope))

    partial_curve = [[curve[0][ij[0]]+0.0 for ij in points_and_slope],
                     [curve[1][ij[0]] for ij in points_and_slope]]

    return partial_curve


def slope_sweep_baseline(curve):
    partial_curve = slope_sweep_points(curve)
    fit_poly = polyfit(partial_curve[0], partial_curve[1], 5)
    baseline = np.copy(curve)
    baseline[1] = polyval(fit_poly, baseline[0])
    return baseline, partial_curve


if __name__ == '__main__':
    sample_curve = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_0")
    sample_baseline, sample_partial_curve = slope_sweep_baseline(sample_curve)
    corrected = np.copy(sample_curve)
    corrected[1] = corrected[1] - sample_baseline[1]

    sample_raw_hard_unmodified = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_raw")
    sample_raw_hard_noise = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_noise")

    # preprocessing output -> PL
    non_preprocessed = np.copy(sample_curve)
    preprocessed = np.copy(corrected)
    target = np.copy(sample_raw_hard_unmodified)
    target[1] = target[1] + sample_raw_hard_noise[1]
    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    plt.plot(non_preprocessed[0] * 0.001, non_preprocessed[1], linewidth=0.3, label="Sygnał przed przetwarzaniem",
             color='gray')
    plt.plot(np.copy(sample_partial_curve[0])*0.001, sample_partial_curve[1], markersize=4, label=f"Wyznaczona przez algorytm łamana wypukła",
             linewidth=1, marker='o')
    plt.plot(sample_baseline[0] * 0.001, sample_baseline[1], linewidth=1, label="Wyznaczona linia bazowa")
    plt.plot(preprocessed[0] * 0.001, preprocessed[1], linewidth=0.3, label="Sygnał po przetworzeniu", color='red')
    plt.plot(target[0] * 0.001, target[1], linewidth=0.3, label="Cel - sygnał bez linii bazowej", color='blue')
    plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Przykładowy wynik metody przetwarzania (CPPL)", fontdict={'fontsize': 11})
    plt.xlabel("E [V]")
    plt.ylabel("I [μA]")
    plt.legend(loc='upper center', prop={'size':7})
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/preprocess_output_CPPL.png")
    plt.savefig(f"{results_final_dir}/preprocess_output_CPPL.png")
    plt.close(fig)

    # fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    # plt.style.use('ggplot')
    # plt.plot(sample_curve[0], sample_curve[1], markersize=10, label=f"wyjściowa krzywa",
    #          linewidth=0.5)
    # plt.plot(sample_partial_curve[0], sample_partial_curve[1], markersize=4, label=f"wyznaczona przez algorytm łamana wypukła",
    #          linewidth=1, marker='o')
    # plt.plot(sample_baseline[0], sample_baseline[1], markersize=4, label=f"dopasowany wielomian",
    #          linewidth=1.5)
    # plt.plot(corrected[0], corrected[1], markersize=10, label=f"krzywa z przeprowadzoną korekcją linii bazowej",
    #          linewidth=0.5)
    # # plt.xlim(-0.5, 0.5)
    # # plt.ylim(-1., 10)
    # plt.title("Korekta linii bazowej - metoda CPPL", fontdict={'fontsize': 10})
    # plt.xlabel("E [V]")
    # plt.ylabel("I [μA]")
    # # plt.legend(loc='upper center')
    # plt.legend(loc='best', prop={'size':7})
    # plt.show()
    # # ensure_dir_creation(f"{results_final_dir}/PCA_component_hard_SGPL.png")
    # # plt.savefig(f"{results_final_dir}/PCA_component_hard_SGPL.png")
    # plt.close(fig)

    # fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    # plt.style.use('ggplot')
    # plt.plot(sample_curve[0], sample_curve[1], markersize=10, label=f"wyjściowa krzywa wstępnie przetworzona za pomocą SG",
    #          linewidth=1)
    # plt.plot(sample_partial_curve[0], sample_partial_curve[1], markersize=4, label=f"wyznaczona przez algorytm łamana wypukła",
    #          linewidth=1, marker='o')
    # plt.plot(sample_baseline[0], sample_baseline[1], markersize=4, label=f"dopasowany wielomian",
    #          linewidth=1.5)
    # plt.plot(corrected[0], corrected[1], markersize=10, label=f"krzywa z przeprowadzoną korekcją linii bazowej",
    #          linewidth=1)
    # # plt.xlim(-0.5, 0.5)
    # # plt.ylim(-1., 10)
    # plt.title("Korekta linii bazowej - metoda CPPL", fontdict={'fontsize': 10})
    # plt.xlabel("E [V]")
    # plt.ylabel("I [μA]")
    # # plt.legend(loc='upper center')
    # plt.legend(loc='best', prop={'size':7})
    # plt.show()
    # # ensure_dir_creation(f"{results_final_dir}/PCA_component_hard_SGPL.png")
    # # plt.savefig(f"{results_final_dir}/PCA_component_hard_SGPL.png")
    # plt.close(fig)

    sample_curve = load_csv_plot(f"{results_eval_dir}/SG_PLbase_onlySG_hard_RMSE/0_sample_preprocessed")
    sample_baseline, sample_partial_curve = slope_sweep_baseline(sample_curve)
    corrected = np.copy(sample_curve)
    corrected[1] = corrected[1] - sample_baseline[1]

    # PREPROCESSING
    # preprocessing output -> SGPL
    non_preprocessed = np.copy(sample_curve)
    preprocessed = np.copy(corrected)
    target = np.copy(sample_raw_hard_unmodified)
    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    plt.plot(non_preprocessed[0] * 0.001, non_preprocessed[1], linewidth=1, label="Sygnał po zastosowaniu algorytmu SG",
             color='gray')
    plt.plot(np.copy(sample_partial_curve[0])*0.001, sample_partial_curve[1], markersize=4, label=f"Wyznaczona przez algorytm łamana wypukła",
             linewidth=1, marker='o')
    plt.plot(sample_baseline[0] * 0.001, sample_baseline[1], linewidth=1, label="Wyznaczona linia bazowa")
    plt.plot(preprocessed[0] * 0.001, preprocessed[1], linewidth=1, label="Sygnał po przetworzeniu", color='red')
    plt.plot(target[0] * 0.001, target[1], linewidth=1, label="Cel - sygnał niezmodyfikowany", color='blue')
    plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Przykładowy wynik metody przetwarzania (SG+CPPL)", fontdict={'fontsize': 11})
    plt.xlabel("E [V]")
    plt.ylabel("I [μA]")
    plt.legend(loc='upper center', prop={'size':7})
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/preprocess_output_SGCPPL.png")
    plt.savefig(f"{results_final_dir}/preprocess_output_SGCPPL.png")
    plt.close(fig)
