import numpy as np

from results.results import results_eval_dir, results_final_dir
from utils.filesystem import load_csv_table, save_csv_table


def collect_avg_rmse_sgpl():
    easy_baseline = [
        load_csv_table(f"{results_eval_dir}/SG_PLbase_onlyPL_easy_RMSE/{i}_baseline_corr", header_count=1)[0] for
        i in range(0, 3)]
    easy_baseline_avgs = np.average(easy_baseline, 0)
    easy_noise = [load_csv_table(f"{results_eval_dir}/SG_PLbase_onlySG_easy_RMSE/{i}_noise_corr", header_count=1)[0] for
                  i in range(0, 3)]
    easy_noise_avgs = np.average(easy_noise, 0)
    easy_overall = [load_csv_table(f"{results_eval_dir}/SG_PLbase_SGPL_easy_RMSE/{i}_overall_corr", header_count=1)[0]
                    for
                    i in range(0, 3)]
    easy_overall_avgs = np.average(easy_overall, 0)
    hard_baseline = [
        load_csv_table(f"{results_eval_dir}/SG_PLbase_onlyPL_hard_RMSE/{i}_baseline_corr", header_count=1)[0] for
        i in range(0, 3)]
    hard_baseline_avgs = np.average(hard_baseline, 0)
    hard_noise = [load_csv_table(f"{results_eval_dir}/SG_PLbase_onlySG_hard_RMSE/{i}_noise_corr", header_count=1)[0] for
                  i in range(0, 3)]
    hard_noise_avgs = np.average(hard_noise, 0)
    hard_overall = [load_csv_table(f"{results_eval_dir}/SG_PLbase_SGPL_hard_RMSE/{i}_overall_corr", header_count=1)[0]
                    for
                    i in range(0, 3)]
    hard_overall_avgs = np.average(hard_overall, 0)
    save_csv_table([easy_baseline_avgs, easy_noise_avgs, easy_overall_avgs,
                    hard_baseline_avgs, hard_noise_avgs, hard_overall_avgs], f"{results_final_dir}/SGPL_RMSE/RMSE_avgs")


def collect_avg_rmse_cppl():
    easy_baseline = [
        load_csv_table(f"{results_eval_dir}/CPPL_onlyPL_easy_RMSE/{i}_baseline_corr", header_count=1)[0] for
        i in range(0, 3)]
    easy_baseline_avgs = np.average(easy_baseline, 0)
    easy_noise = [load_csv_table(f"{results_eval_dir}/CPPL_onlySG_easy_RMSE/{i}_noise_corr", header_count=1)[0] for
                  i in range(0, 3)]
    easy_noise_avgs = np.average(easy_noise, 0)
    easy_overall = [load_csv_table(f"{results_eval_dir}/CPPL_SGPL_easy_RMSE/{i}_overall_corr", header_count=1)[0]
                    for
                    i in range(0, 3)]
    easy_overall_avgs = np.average(easy_overall, 0)
    hard_baseline = [
        load_csv_table(f"{results_eval_dir}/CPPL_onlyPL_hard_RMSE/{i}_baseline_corr", header_count=1)[0] for
        i in range(0, 3)]
    hard_baseline_avgs = np.average(hard_baseline, 0)
    hard_noise = [load_csv_table(f"{results_eval_dir}/CPPL_onlySG_hard_RMSE/{i}_noise_corr", header_count=1)[0] for
                  i in range(0, 3)]
    hard_noise_avgs = np.average(hard_noise, 0)
    hard_overall = [load_csv_table(f"{results_eval_dir}/CPPL_SGPL_hard_RMSE/{i}_overall_corr", header_count=1)[0]
                    for
                    i in range(0, 3)]
    hard_overall_avgs = np.average(hard_overall, 0)
    save_csv_table([easy_baseline_avgs, easy_noise_avgs, easy_overall_avgs,
                    hard_baseline_avgs, hard_noise_avgs, hard_overall_avgs], f"{results_final_dir}/CPPL_RMSE/CPPL_avgs")


if __name__ == '__main__':
    collect_avg_rmse_sgpl()
    collect_avg_rmse_cppl()
