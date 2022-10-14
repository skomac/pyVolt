import numpy as np
from matplotlib import pyplot as plt

from utils.filesystem import load_csv_plot, load_csv_table, ensure_dir_creation
from results.results import results_eval_dir, results_sim_dir, results_base_dir, results_prep_dir, results_final_dir

from os.path import exists


def load_cluster_plot(filename_prefix):
    result = []
    i = 0
    while exists(f"{filename_prefix}_{i}"):
        result.append(load_csv_plot(f"{filename_prefix}_{i}"))
        i = i + 1
    if i == 0:
        print(f"WARNING:load_cluster_plot: No data matching prefix: {filename_prefix}")
    return result


def collect_all_SGPL():
    name = "Savitzky-Golay i linia bazowa wielomianowa"
    abstract = ""
    sample_raw_easy_unmodified = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_0/pca_sample_dataset_0_raw")
    sample_raw_easy_signal = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_0/pca_sample_dataset_0_0")
    sample_raw_easy_baseline = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_0/pca_sample_dataset_0_baseline")
    sample_raw_easy_noise = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_0/pca_sample_dataset_0_noise")
    sample_raw_hard_unmodified = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_raw")
    sample_raw_hard_signal = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_0")
    sample_raw_hard_baseline = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_baseline")
    sample_raw_hard_noise = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_noise")
    sample_corrected_signal = load_csv_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_RMSE/0_sample_preprocessed")
    sample_corrected_baseline = load_csv_plot(f"{results_eval_dir}/SG_PLbase_onlyPL_hard_RMSE/0_sample_preprocessed")
    sample_corrected_noise = load_csv_plot(f"{results_eval_dir}/SG_PLbase_onlySG_hard_RMSE/0_sample_preprocessed")
    rmse_signal = [load_csv_table(f"{results_eval_dir}/SG_PLbase_SGPL_easy_RMSE/0_overall_corr", header_count=1),
                   load_csv_table(f"{results_eval_dir}/SG_PLbase_SGPL_hard_RMSE/0_overall_corr",
                                  header_count=1)]  # easy/hard
    rmse_baseline = [load_csv_table(f"{results_eval_dir}/SG_PLbase_onlyPL_easy_RMSE/0_baseline_corr", header_count=1),
                     load_csv_table(f"{results_eval_dir}/SG_PLbase_onlyPL_hard_RMSE/0_baseline_corr",
                                    header_count=1)]  # easy/hard
    rmse_noise = [load_csv_table(f"{results_eval_dir}/SG_PLbase_onlySG_easy_RMSE/0_noise_corr", header_count=1),
                  load_csv_table(f"{results_eval_dir}/SG_PLbase_onlySG_hard_RMSE/0_noise_corr",
                                 header_count=1)]  # easy/hard
    pca_raw_easy_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_SGPL_easy_PCA/raw_cluster_data")
    pca_raw_hard_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/raw_cluster_data")
    pca_raw_experimental_plot = [
        load_cluster_plot(f"{results_eval_dir}/SG_PLbase_SGPL_experimental_PCA/raw_cluster_data")]
    pca_raw_explained_variation_easy = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_easy_PCA/raw_explained_variance")
    pca_raw_explained_variation_hard = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/raw_explained_variance")
    pca_raw_explained_variation_experimental = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_experimental_PCA/raw_explained_variance")
    pca_easy_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_SGPL_easy_PCA/preprocessed_cluster_data")
    pca_hard_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/preprocessed_cluster_data")
    pca_experimental_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_SGPL_experimental_PCA/preprocessed_cluster_data")
    pca_explained_variation_easy = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_easy_PCA/preprocessed_explained_variance")
    pca_explained_variation_hard = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/preprocessed_explained_variance")
    pca_explained_variation_experimental = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_experimental_PCA/preprocessed_explained_variance")
    pca_baseline_easy_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_onlyPL_easy_PCA/preprocessed_cluster_data")
    pca_baseline_hard_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_onlyPL_hard_PCA/preprocessed_cluster_data")
    pca_baseline_experimental_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_onlyPL_experimental_PCA/preprocessed_cluster_data")
    pca_baseline_explained_variation_easy = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlyPL_easy_PCA/preprocessed_explained_variance")
    pca_baseline_explained_variation_hard = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlyPL_hard_PCA/preprocessed_explained_variance")
    pca_baseline_explained_variation_experimental = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlyPL_experimental_PCA/preprocessed_explained_variance")
    pca_noise_easy_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_onlySG_easy_PCA/preprocessed_cluster_data")
    pca_noise_hard_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_onlySG_hard_PCA/preprocessed_cluster_data")
    pca_noise_experimental_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_onlySG_experimental_PCA/preprocessed_cluster_data")
    pca_noise_explained_variation_easy = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlySG_easy_PCA/preprocessed_explained_variance")
    pca_noise_explained_variation_hard = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlySG_hard_PCA/preprocessed_explained_variance")
    pca_noise_explained_variation_experimental = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlySG_experimental_PCA/preprocessed_explained_variance")
    note = ""

    # SAMPLE_GENERATED

    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    plt.plot(np.copy(sample_raw_easy_unmodified[0]) * 0.001, sample_raw_easy_unmodified[1], linewidth=2.5,
             label="składowa użyteczna")
    plt.plot(np.copy(sample_raw_easy_noise[0]) * 0.001, sample_raw_easy_noise[1], linewidth=1, label="składowa szumu")
    plt.plot(np.copy(sample_raw_easy_baseline[0]) * 0.001, sample_raw_easy_baseline[1], linewidth=2.5,
             label="linia bazowa")
    plt.plot(np.copy(sample_raw_easy_signal[0]) * 0.001, sample_raw_easy_signal[1], linewidth=1,
             label="wygenerowany sygnał")
    plt.xlim(-0.5, 0.5)
    plt.title("Składowe przykładowego sygnału z grupy A", fontdict={'fontsize': 12})
    plt.xlabel("E [V]")
    plt.ylabel("I [μA]")
    plt.legend(loc='upper center')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/sample_generated_A.png")
    plt.savefig(f"{results_final_dir}/sample_generated_A.png")
    plt.close(fig)

    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    plt.plot(np.copy(sample_raw_hard_unmodified[0]) * 0.001, sample_raw_hard_unmodified[1], linewidth=2.5,
             label="składowa użyteczna")
    plt.plot(np.copy(sample_raw_hard_noise[0]) * 0.001, sample_raw_hard_noise[1], linewidth=1, label="składowa szumu")
    plt.plot(np.copy(sample_raw_hard_baseline[0]) * 0.001, sample_raw_hard_baseline[1], linewidth=2.5,
             label="linia bazowa")
    plt.plot(np.copy(sample_raw_hard_signal[0]) * 0.001, sample_raw_hard_signal[1], linewidth=1,
             label="wygenerowany sygnał")
    plt.xlim(-0.5, 0.5)
    plt.ylim(-1., 15)
    plt.title("Składowe przykładowego sygnału z grupy B", fontdict={'fontsize': 12})
    plt.xlabel("E [V]")
    plt.ylabel("I [μA]")
    plt.legend(loc='upper center')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/sample_generated_B.png")
    plt.savefig(f"{results_final_dir}/sample_generated_B.png")
    plt.close(fig)

    sample_raw_easy_0 = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_0/pca_sample_dataset_0_0")
    sample_raw_easy_1 = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_1/pca_sample_dataset_1_0")
    sample_raw_easy_2 = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_2/pca_sample_dataset_2_0")
    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    plt.plot(sample_raw_easy_0[0] * 0.001, sample_raw_easy_0[1], linewidth=1, label="A_1")
    plt.plot(sample_raw_easy_1[0] * 0.001, sample_raw_easy_1[1], linewidth=1, label="A_2")
    plt.plot(sample_raw_easy_2[0] * 0.001, sample_raw_easy_2[1], linewidth=1, label="A_3")
    plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Przykładowe sygnały z zestawów grupy A", fontdict={'fontsize': 12})
    plt.xlabel("E [V]")
    plt.ylabel("I [μA]")
    plt.legend(loc='upper center')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/samples_generated_A.png")
    plt.savefig(f"{results_final_dir}/samples_generated_A.png")
    plt.close(fig)

    sample_raw_hard_0 = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_0")
    sample_raw_hard_1 = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_1/ml_sample_dataset_1_0")
    sample_raw_hard_2 = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_2/ml_sample_dataset_2_0")
    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    plt.plot(sample_raw_hard_0[0] * 0.001, sample_raw_hard_0[1], linewidth=1, label="B_1")
    plt.plot(sample_raw_hard_1[0] * 0.001, sample_raw_hard_1[1], linewidth=1, label="B_2")
    plt.plot(sample_raw_hard_2[0] * 0.001, sample_raw_hard_2[1], linewidth=1, label="B_3")
    plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Przykładowe sygnały z zestawów grupy B", fontdict={'fontsize': 12})
    plt.xlabel("E [V]")
    plt.ylabel("I [μA]")
    plt.legend(loc='upper center')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/samples_generated_B.png")
    plt.savefig(f"{results_final_dir}/samples_generated_B.png")
    plt.close(fig)

    # PREPROCESSING
    # preprocessing output -> SGPL
    non_preprocessed = np.copy(sample_raw_hard_signal)
    preprocessed = np.copy(sample_corrected_signal)
    target = np.copy(sample_raw_hard_unmodified)
    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    plt.plot(non_preprocessed[0] * 0.001, non_preprocessed[1], linewidth=1, label="Sygnał przed przetwarzaniem",
             color='gray')
    plt.plot(preprocessed[0] * 0.001, preprocessed[1], linewidth=1, label="Sygnał po przetworzeniu", color='red')
    plt.plot(target[0] * 0.001, target[1], linewidth=1, label="Cel - sygnał niezmodyfikowany", color='blue')
    plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Przykładowy wynik metody przetwarzania (SG+PL)", fontdict={'fontsize': 12})
    plt.xlabel("E [V]")
    plt.ylabel("I [μA]")
    plt.legend(loc='upper center')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/preprocess_output_SGPL.png")
    plt.savefig(f"{results_final_dir}/preprocess_output_SGPL.png")
    plt.close(fig)

    # preprocessing output -> PL
    non_preprocessed = np.copy(sample_raw_hard_signal)
    preprocessed = np.copy(sample_corrected_baseline)
    target = np.copy(sample_raw_hard_unmodified)
    target[1] = target[1] + sample_raw_hard_noise[1]
    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    plt.plot(non_preprocessed[0] * 0.001, non_preprocessed[1], linewidth=1, label="Sygnał przed przetwarzaniem",
             color='gray')
    plt.plot(preprocessed[0] * 0.001, preprocessed[1], linewidth=0.5, label="Sygnał po przetworzeniu", color='red')
    plt.plot(target[0] * 0.001, target[1], linewidth=0.5, label="Cel - sygnał bez linii bazowej", color='blue')
    plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Przykładowy wynik metody przetwarzania (PL)", fontdict={'fontsize': 12})
    plt.xlabel("E [V]")
    plt.ylabel("I [μA]")
    plt.legend(loc='upper center')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/preprocess_output_PL.png")
    plt.savefig(f"{results_final_dir}/preprocess_output_PL.png")
    plt.close(fig)

    # preprocessing output -> SG
    non_preprocessed = np.copy(sample_raw_hard_signal)
    preprocessed = np.copy(sample_corrected_noise)
    target = np.copy(sample_raw_hard_unmodified)
    target[1] = target[1] + sample_raw_hard_baseline[1]
    fig, ax = plt.subplots(figsize=[4.8, 3.6], tight_layout=True)
    print(ax)
    plt.style.use('ggplot')
    plt.plot(non_preprocessed[0] * 0.001, non_preprocessed[1], linewidth=0.4, label="Sygnał przed przetwarzaniem",
             color='gray')
    plt.plot(preprocessed[0] * 0.001, preprocessed[1], linewidth=0.6, label="Sygnał po przetworzeniu", color='red')
    plt.plot(target[0] * 0.001, target[1], linewidth=0.6, label="Cel - sygnał bez szumu losowego", color='blue')
    plt.xlim(-0.5, 0.5)
    plt.ylim(-2., 17)
    plt.title("Przykładowy wynik metody przetwarzania (SG)", fontdict={'fontsize': 12})
    plt.xlabel("E [V]")
    plt.ylabel("I [μA]")

    plt.legend(loc='upper right', prop={'size': 8})

    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
    axins = zoomed_inset_axes(ax, 5, loc='lower left')
    axins.set_xlim(-0.4, -0.35)
    axins.set_ylim(5.8, 6.8)
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    axins.plot(non_preprocessed[0] * 0.001, non_preprocessed[1], linewidth=0.4, label="Sygnał przed przetwarzaniem",
               color='gray')
    axins.plot(preprocessed[0] * 0.001, preprocessed[1], linewidth=1, label="Sygnał po przetworzeniu", color='red')
    axins.plot(target[0] * 0.001, target[1], linewidth=1, label="Cel - sygnał bez szumu losowego", color='blue')

    mark_inset(ax, axins, loc1=1, loc2=2, fc="none", ec="0.3")

    axins2 = zoomed_inset_axes(ax, 5, loc='upper left')
    axins2.set_xlim(-0.18, -0.13)
    axins2.set_ylim(5.4, 6.4)
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    axins2.plot(non_preprocessed[0] * 0.001, non_preprocessed[1], linewidth=0.4, label="Sygnał przed przetwarzaniem",
                color='gray')
    axins2.plot(preprocessed[0] * 0.001, preprocessed[1], linewidth=1, label="Sygnał po przetworzeniu", color='red')
    axins2.plot(target[0] * 0.001, target[1], linewidth=1, label="Cel - sygnał bez szumu losowego", color='blue')

    mark_inset(ax, axins2, loc1=1, loc2=3, fc="none", ec="0.3")

    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/preprocess_output_SG.png")
    plt.savefig(f"{results_final_dir}/preprocess_output_SG.png")
    plt.close(fig)


def collect_PCA_SGPL():
    name = "Savitzky-Golay i linia bazowa wielomianowa"
    abstract = ""
    sample_raw_easy_unmodified = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_0/pca_sample_dataset_0_raw")
    sample_raw_easy_signal = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_0/pca_sample_dataset_0_0")
    sample_raw_easy_baseline = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_0/pca_sample_dataset_0_baseline")
    sample_raw_easy_noise = load_csv_plot(f"{results_prep_dir}/pca_sample_dataset_0/pca_sample_dataset_0_noise")
    sample_raw_hard_unmodified = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_raw")
    sample_raw_hard_signal = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_0")
    sample_raw_hard_baseline = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_baseline")
    sample_raw_hard_noise = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_noise")
    sample_corrected_signal = load_csv_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_RMSE/0_sample_preprocessed")
    sample_corrected_baseline = load_csv_plot(f"{results_eval_dir}/SG_PLbase_onlyPL_hard_RMSE/0_sample_preprocessed")
    sample_corrected_noise = load_csv_plot(f"{results_eval_dir}/SG_PLbase_onlySG_hard_RMSE/0_sample_preprocessed")
    rmse_signal = [load_csv_table(f"{results_eval_dir}/SG_PLbase_SGPL_easy_RMSE/0_overall_corr", header_count=1),
                   load_csv_table(f"{results_eval_dir}/SG_PLbase_SGPL_hard_RMSE/0_overall_corr",
                                  header_count=1)]  # easy/hard
    rmse_baseline = [load_csv_table(f"{results_eval_dir}/SG_PLbase_onlyPL_easy_RMSE/0_baseline_corr", header_count=1),
                     load_csv_table(f"{results_eval_dir}/SG_PLbase_onlyPL_hard_RMSE/0_baseline_corr",
                                    header_count=1)]  # easy/hard
    rmse_noise = [load_csv_table(f"{results_eval_dir}/SG_PLbase_onlySG_easy_RMSE/0_noise_corr", header_count=1),
                  load_csv_table(f"{results_eval_dir}/SG_PLbase_onlySG_hard_RMSE/0_noise_corr",
                                 header_count=1)]  # easy/hard
    pca_raw_easy_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_SGPL_easy_PCA/raw_cluster_data")
    pca_raw_hard_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/raw_cluster_data")
    pca_raw_experimental_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_SGPL_experimental_PCA/raw_cluster_data")
    pca_raw_explained_variation_easy = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_easy_PCA/raw_explained_variance")
    pca_raw_explained_variation_hard = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/raw_explained_variance")
    pca_raw_explained_variation_experimental = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_experimental_PCA/raw_explained_variance")
    pca_easy_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_SGPL_easy_PCA/preprocessed_cluster_data")
    pca_hard_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/preprocessed_cluster_data")
    pca_experimental_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_SGPL_experimental_PCA/preprocessed_cluster_data")
    pca_explained_variation_easy = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_easy_PCA/preprocessed_explained_variance")
    pca_explained_variation_hard = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/preprocessed_explained_variance")
    pca_explained_variation_experimental = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_SGPL_experimental_PCA/preprocessed_explained_variance")
    pca_baseline_easy_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_onlyPL_easy_PCA/preprocessed_cluster_data")
    pca_baseline_hard_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_onlyPL_hard_PCA/preprocessed_cluster_data")
    pca_baseline_experimental_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_onlyPL_experimental_PCA/preprocessed_cluster_data")
    pca_baseline_explained_variation_easy = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlyPL_easy_PCA/preprocessed_explained_variance")
    pca_baseline_explained_variation_hard = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlyPL_hard_PCA/preprocessed_explained_variance")
    pca_baseline_explained_variation_experimental = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlyPL_experimental_PCA/preprocessed_explained_variance")
    pca_noise_easy_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_onlySG_easy_PCA/preprocessed_cluster_data")
    pca_noise_hard_plot = load_cluster_plot(f"{results_eval_dir}/SG_PLbase_onlySG_hard_PCA/preprocessed_cluster_data")
    pca_noise_experimental_plot = load_cluster_plot(
        f"{results_eval_dir}/SG_PLbase_onlySG_experimental_PCA/preprocessed_cluster_data")
    pca_noise_explained_variation_easy = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlySG_easy_PCA/preprocessed_explained_variance")
    pca_noise_explained_variation_hard = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlySG_hard_PCA/preprocessed_explained_variance")
    pca_noise_explained_variation_experimental = load_csv_table(
        f"{results_eval_dir}/SG_PLbase_onlySG_experimental_PCA/preprocessed_explained_variance")
    note = ""

    # PCA CLUSTER PLOTS

    # pca_raw_easy_plot / pca_easy_plot
    non_preprocessed = np.copy(pca_raw_easy_plot)
    preprocessed = np.copy(pca_easy_plot)
    fig, ax = plt.subplots(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey']
    colors_dark = ['red', 'dodgerblue', 'black']
    for i in range(0, 3):
        plt.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"A-{i + 1}",
                 color=colors_light[i], marker='+', linewidth=0)
        plt.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"SG+PL(A-{i + 1})", color=colors_dark[i],
                 marker='x', linewidth=0)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA dla grupy A (SG+PL)", fontdict={'fontsize': 12})
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    # plt.legend(loc='upper center')
    plt.legend(loc='best')
    # plt.show()

    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
    axins = zoomed_inset_axes(ax, 10, loc='lower center')
    axins.set_xlim(-193, -172)
    axins.set_ylim(-108, -94)
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    for i in range(0, 3):
        axins.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"{i + 1}",
                   color=colors_light[i], marker='+', linewidth=0)
        axins.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"SG({i + 1})", color=colors_dark[i],
                   marker='x', linewidth=0)

    mark_inset(ax, axins, loc1=3, loc2=2, fc="none", ec="0.3")

    ensure_dir_creation(f"{results_final_dir}/PCA_cluster_easy_SGPL.png")
    plt.savefig(f"{results_final_dir}/PCA_cluster_easy_SGPL.png")
    plt.close(fig)

    non_preprocessed = np.copy(pca_raw_hard_plot)
    preprocessed = np.copy(pca_hard_plot)
    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey']
    colors_dark = ['red', 'dodgerblue', 'black']
    for i in range(0, 3):
        plt.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"B-{i + 1}",
                 color=colors_light[i], marker='+', linewidth=0)
        plt.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"SG+PL(B-{i + 1})", color=colors_dark[i],
                 marker='x', linewidth=0)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA dla grupy B (SG+PL)", fontdict={'fontsize': 12})
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    # plt.legend(loc='upper center')
    plt.legend(loc='best')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/PCA_cluster_hard_SGPL.png")
    plt.savefig(f"{results_final_dir}/PCA_cluster_hard_SGPL.png")
    plt.close(fig)

    non_preprocessed = np.copy(pca_raw_easy_plot)
    preprocessed = np.copy(pca_baseline_easy_plot)
    fig, ax = plt.subplots(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey']
    colors_dark = ['red', 'dodgerblue', 'black']
    for i in range(0, 3):
        plt.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"A-{i + 1}",
                 color=colors_light[i], marker='+', linewidth=0)
        plt.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"PL(A-{i + 1})", color=colors_dark[i],
                 marker='x', linewidth=0)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA dla grupy A (PL)", fontdict={'fontsize': 12})
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    # plt.legend(loc='upper center')
    plt.legend(loc='best')
    # plt.show()

    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
    axins = zoomed_inset_axes(ax, 10, loc='lower center')
    axins.set_xlim(-193, -172)
    axins.set_ylim(-108, -94)
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    for i in range(0, 3):
        axins.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"{i + 1}",
                   color=colors_light[i], marker='+', linewidth=0)
        axins.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"SG({i + 1})", color=colors_dark[i],
                   marker='x', linewidth=0)

    mark_inset(ax, axins, loc1=3, loc2=2, fc="none", ec="0.3")

    ensure_dir_creation(f"{results_final_dir}/PCA_cluster_easy_PL.png")
    plt.savefig(f"{results_final_dir}/PCA_cluster_easy_PL.png")
    plt.close(fig)

    non_preprocessed = np.copy(pca_raw_hard_plot)
    preprocessed = np.copy(pca_baseline_hard_plot)
    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey']
    colors_dark = ['red', 'dodgerblue', 'black']
    for i in range(0, 3):
        plt.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"B-{i + 1}",
                 color=colors_light[i], marker='+', linewidth=0)
        plt.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"PL(B-{i + 1})", color=colors_dark[i],
                 marker='x', linewidth=0)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA dla grupy B (PL)", fontdict={'fontsize': 12})
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    # plt.legend(loc='upper center')
    plt.legend(loc='best')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/PCA_cluster_hard_PL.png")
    plt.savefig(f"{results_final_dir}/PCA_cluster_hard_PL.png")
    plt.close(fig)

    non_preprocessed = np.copy(pca_raw_easy_plot)
    preprocessed = np.copy(pca_noise_easy_plot)
    fig, ax = plt.subplots(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey']
    colors_dark = ['red', 'dodgerblue', 'black']
    for i in range(0, 3):
        plt.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"A-{i + 1}",
                 color=colors_light[i], marker='+', linewidth=0)
        plt.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"SG(A-{i + 1})", color=colors_dark[i],
                 marker='x', linewidth=0)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA dla grupy A (SG)", fontdict={'fontsize': 12})
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    # plt.legend(loc='upper center')
    plt.legend(loc='best')
    # plt.show()

    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
    axins = zoomed_inset_axes(ax, 10, loc='lower center')
    axins.set_xlim(-193, -172)
    axins.set_ylim(-108, -94)
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    for i in range(0, 3):
        axins.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"{i + 1}",
                   color=colors_light[i], marker='+', linewidth=0)
        axins.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"SG({i + 1})", color=colors_dark[i],
                   marker='x', linewidth=0)

    mark_inset(ax, axins, loc1=3, loc2=2, fc="none", ec="0.3")

    ensure_dir_creation(f"{results_final_dir}/PCA_cluster_easy_SG.png")
    plt.savefig(f"{results_final_dir}/PCA_cluster_easy_SG.png")
    plt.close(fig)

    non_preprocessed = np.copy(pca_raw_hard_plot)
    preprocessed = np.copy(pca_noise_hard_plot)
    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey']
    colors_dark = ['red', 'dodgerblue', 'black']
    for i in range(0, 3):
        plt.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"B-{i + 1}",
                 color=colors_light[i], marker='+', linewidth=0)
        plt.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"SG(B-{i + 1})", color=colors_dark[i],
                 marker='x', linewidth=0)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA dla grupy A (SG)", fontdict={'fontsize': 12})
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    # plt.legend(loc='upper center')
    plt.legend(loc='best')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/PCA_cluster_hard_SG.png")
    plt.savefig(f"{results_final_dir}/PCA_cluster_hard_SG.png")
    plt.close(fig)

    non_preprocessed = np.copy(pca_raw_experimental_plot)
    preprocessed = np.copy(pca_experimental_plot)
    fig, ax = plt.subplots(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey', 'lime', 'darkviolet', 'aquamarine', 'violet', 'gold',
                    'silver', 'green', 'blue']
    colors_dark = ['red', 'dodgerblue', 'black', 'limegreen', 'indigo', 'lightseagreen', 'fuchsia', 'orange', 'grey',
                   'darkgreen', 'darkblue']
    for i in range(0, 11):
        plt.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"E-{i + 1}",
                 color=colors_light[i], marker='+', linewidth=0)
        plt.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"SG+PL(E-{i + 1})", color=colors_dark[i],
                 marker='x', linewidth=0)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA dla grupy E (SG+PL)", fontdict={'fontsize': 12})
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    # plt.legend(loc='upper center')
    # plt.legend(loc='best', prop={'size': 5})
    plt.legend(bbox_to_anchor=(1.05, 1.1), prop={'size': 7})
    # plt.show()

    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
    axins = zoomed_inset_axes(ax, 12, loc='lower center')
    axins.set_xlim(-5.5, -5.)
    axins.set_ylim(-5.5, -4.)
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    for i in range(0, 11):
        axins.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"E-{i + 1}",
                   color=colors_light[i], marker='+', linewidth=0)
        axins.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"PL(E-{i + 1})", color=colors_dark[i],
                   marker='x', linewidth=0)

    mark_inset(ax, axins, loc1=3, loc2=2, fc="none", ec="0.3")

    ensure_dir_creation(f"{results_final_dir}/PCA_cluster_E_SGPL.png")
    plt.savefig(f"{results_final_dir}/PCA_cluster_E_SGPL.png")
    plt.close(fig)

    non_preprocessed = np.copy(pca_raw_experimental_plot)
    preprocessed = np.copy(pca_noise_experimental_plot)
    fig, ax = plt.subplots(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey', 'lime', 'darkviolet', 'aquamarine', 'violet', 'gold',
                    'silver', 'green', 'blue']
    colors_dark = ['red', 'dodgerblue', 'black', 'limegreen', 'indigo', 'lightseagreen', 'fuchsia', 'orange', 'grey',
                   'darkgreen', 'darkblue']
    for i in range(0, 11):
        plt.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"E-{i + 1}",
                 color=colors_light[i], marker='+', linewidth=0)
        plt.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"SG(E-{i + 1})", color=colors_dark[i],
                 marker='x', linewidth=0)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA dla grupy E (SG)", fontdict={'fontsize': 12})
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    # plt.legend(loc='upper center')
    # plt.legend(loc='best', prop={'size': 5})
    plt.legend(bbox_to_anchor=(1.05, 1.1), prop={'size': 7})
    # plt.show()

    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
    axins = zoomed_inset_axes(ax, 12, loc='lower center')
    axins.set_xlim(-5.5, -5.)
    axins.set_ylim(-5.5, -4.)
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    for i in range(0, 11):
        axins.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"E-{i + 1}",
                   color=colors_light[i], marker='+', linewidth=0)
        axins.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"(E-{i + 1})", color=colors_dark[i],
                   marker='x', linewidth=0)

    mark_inset(ax, axins, loc1=3, loc2=2, fc="none", ec="0.3")

    ensure_dir_creation(f"{results_final_dir}/PCA_cluster_E_SG.png")
    plt.savefig(f"{results_final_dir}/PCA_cluster_E_SG.png")
    plt.close(fig)

    non_preprocessed = np.copy(pca_raw_experimental_plot)
    preprocessed = np.copy(pca_baseline_experimental_plot)
    fig, ax = plt.subplots(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey', 'lime', 'darkviolet', 'aquamarine', 'violet', 'gold',
                    'silver', 'green', 'blue']
    colors_dark = ['red', 'dodgerblue', 'black', 'limegreen', 'indigo', 'lightseagreen', 'fuchsia', 'orange', 'grey',
                   'darkgreen', 'darkblue']
    for i in range(0, 11):
        plt.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"E-{i + 1}",
                 color=colors_light[i], marker='+', linewidth=0)
        plt.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"PL(E-{i + 1})", color=colors_dark[i],
                 marker='x', linewidth=0)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA dla grupy E (PL)", fontdict={'fontsize': 12})
    plt.xlabel("PC1")
    plt.ylabel("PC2")

    # plt.legend(loc='upper center')
    # plt.legend(loc='best', prop={'size': 5})
    plt.legend(bbox_to_anchor=(1.05, 1.1), prop={'size': 7})

    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
    axins = zoomed_inset_axes(ax, 12, loc='lower center')
    axins.set_xlim(-5.5, -5.)
    axins.set_ylim(-5.5, -4.)
    plt.xticks(visible=False)
    plt.yticks(visible=False)
    for i in range(0, 11):
        axins.plot(non_preprocessed[i][0], non_preprocessed[i][1], markersize=10, label=f"E-{i + 1}",
                   color=colors_light[i], marker='+', linewidth=0)
        axins.plot(preprocessed[i][0], preprocessed[i][1], markersize=10, label=f"PL(E-{i + 1})", color=colors_dark[i],
                   marker='x', linewidth=0)

    mark_inset(ax, axins, loc1=3, loc2=2, fc="none", ec="0.3")

    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/PCA_cluster_E_PL.png")
    plt.savefig(f"{results_final_dir}/PCA_cluster_E_PL.png")
    plt.close(fig)


def collect_components_SGPL():
    raw_components_hard = [load_csv_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/raw_component_data_0"),
                           load_csv_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/raw_component_data_1")]
    preprocessed_components_hard_SG = [
        load_csv_plot(f"{results_eval_dir}/SG_PLbase_onlySG_hard_PCA/preprocessed_component_data_0"),
        load_csv_plot(f"{results_eval_dir}/SG_PLbase_onlySG_hard_PCA/preprocessed_component_data_1")]
    preprocessed_components_hard_PL = [
        load_csv_plot(f"{results_eval_dir}/SG_PLbase_onlyPL_hard_PCA/preprocessed_component_data_0"),
        load_csv_plot(f"{results_eval_dir}/SG_PLbase_onlyPL_hard_PCA/preprocessed_component_data_1")]
    preprocessed_components_hard_SGPL = [
        load_csv_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/preprocessed_component_data_0"),
        load_csv_plot(f"{results_eval_dir}/SG_PLbase_SGPL_hard_PCA/preprocessed_component_data_1")]

    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey']
    colors_dark = ['red', 'dodgerblue', 'black']
    for i in range(0, 2):
        plt.plot(raw_components_hard[i][0], raw_components_hard[i][1], markersize=10, label=f"PC{i + 1}",
                 color=colors_light[i], linewidth=0.5)
        plt.plot(preprocessed_components_hard_SG[i][0], preprocessed_components_hard_SG[i][1], markersize=10,
                 label=f"PC{i + 1}(SG)", color=colors_dark[i],
                 linewidth=2)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA - główne składowe (grupa B, algorytm SG)", fontdict={'fontsize': 10})
    plt.xlabel("E [V]")
    # plt.ylabel("")
    # plt.legend(loc='upper center')
    plt.legend(loc='best')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/PCA_component_hard_SG.png")
    plt.savefig(f"{results_final_dir}/PCA_component_hard_SG.png")
    plt.close(fig)

    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    # colors_light = ['lightcoral', 'deepskyblue', 'dimgrey']
    colors_light = ['black', 'olive', 'dimgrey']
    colors_dark = ['red', 'dodgerblue', 'black']
    for i in range(0, 2):
        plt.plot(raw_components_hard[i][0], raw_components_hard[i][1], markersize=10, label=f"PC{i + 1}",
                 color=colors_light[i], linewidth=0.5)
        plt.plot(preprocessed_components_hard_PL[i][0], preprocessed_components_hard_PL[i][1], markersize=10,
                 label=f"PC{i + 1}(PL)", color=colors_dark[i],
                 linewidth=0.5)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA - główne składowe (grupa B, algorytm PL)", fontdict={'fontsize': 10})
    plt.xlabel("E [V]")
    # plt.ylabel("")
    # plt.legend(loc='upper center')
    plt.legend(loc='best')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/PCA_component_hard_PL.png")
    plt.savefig(f"{results_final_dir}/PCA_component_hard_PL.png")
    plt.close(fig)

    fig = plt.figure(tight_layout=True, figsize=[4.8, 3.6])
    plt.style.use('ggplot')
    colors_light = ['lightcoral', 'deepskyblue', 'dimgrey']
    colors_dark = ['red', 'dodgerblue', 'black']
    for i in range(0, 2):
        plt.plot(raw_components_hard[i][0], raw_components_hard[i][1], markersize=10, label=f"PC{i + 1}",
                 color=colors_light[i], linewidth=0.5)
        plt.plot(preprocessed_components_hard_SGPL[i][0], preprocessed_components_hard_SGPL[i][1], markersize=10,
                 label=f"PC{i + 1}(SG+PL)", color=colors_dark[i],
                 linewidth=2)
    # plt.xlim(-0.5, 0.5)
    # plt.ylim(-1., 10)
    plt.title("Analiza PCA - główne składowe (grupa B, algorytm SG+PL)", fontdict={'fontsize': 10})
    plt.xlabel("E [V]")
    # plt.ylabel("")
    # plt.legend(loc='upper center')
    plt.legend(loc='best')
    # plt.show()
    ensure_dir_creation(f"{results_final_dir}/PCA_component_hard_SGPL.png")
    plt.savefig(f"{results_final_dir}/PCA_component_hard_SGPL.png")
    plt.close(fig)


if __name__ == "__main__":
    # collect_all_SGPL()
    # collect_PCA_SGPL()
    collect_components_SGPL()
