import json

import numpy as np

from config.config import cfg_eval_dir
from evaluation.filter_evaluation import signal_recovery_evaluation, rmse_evaluation
from evaluation.ml_evalutation import ml_assessment
from evaluation.pca_evalutation import pca_assessment
from evaluation.preprocess import preprocess_all_with_instr
from experimental.load_mat import import_juices
from results.results import results_prep_dir, results_eval_dir
from utils.data import for_each_first_curve_in_suite
from utils.filesystem import load_csv_plot, save_csv_table, save_csv_dict, load_prepared_samples, save_csv_plot
from os.path import isfile

from utils.plot import Plot


def get_suite_filepath(suite_name, index):
    return f"../results/preparation/{suite_name}/{suite_name}_{index}"


def evaluate(cfg):
    with open(f'{cfg_eval_dir}/{cfg}.json', 'r') as config_file:
        instructions = json.load(config_file)

    data = load_data(instructions["initial_data"])
    noise = load_noise(instructions["initial_data"])
    baseline = load_baseline(instructions["initial_data"])

    preprocessed = preprocess_all(data, instructions['preprocessing_instructions'], instructions['name'])

    if instructions["eval_type"] == "SIGNAL_RECOVERY":
        raw_data = []
        for suite_name in instructions["initial_data"]:
            raw_data.append(load_csv_plot(f"{results_prep_dir}/{suite_name}/{suite_name}_raw"))
        save_csv_table(signal_recovery_evaluation(data, preprocessed, raw_data),
                       f"{results_eval_dir}/{instructions['name']}",
                       ["Signal recovery"])
    elif instructions["eval_type"] == "RMSE":
        for suite_id, suite_name in enumerate(instructions["initial_data"]):
            samples = load_prepared_samples(suite_name)
            results_rmse = rmse_evaluation(data[suite_id], preprocessed[suite_id], noise[suite_id], baseline[suite_id], samples)
            for rmse_type, results in results_rmse.items():
                save_csv_table([results], f"{results_eval_dir}/{instructions['name']}/{suite_id}_{rmse_type}",
                               ["Original RMSE", "Preprocessed RMSE"])
            save_csv_plot(preprocessed[suite_id][0],
                          f"{results_eval_dir}/{instructions['name']}/{suite_id}_sample_preprocessed")
    elif instructions["eval_type"] == "ML_ASSESSMENT":
        save_csv_dict(ml_assessment(data, preprocessed, instructions["eval_config"]),
                      f"{results_eval_dir}/{instructions['name']}")
    elif instructions["eval_type"] == "PCA_ASSESSMENT":
        results = pca_assessment(data, preprocessed, instructions["eval_config"], instructions["initial_data"])
        for data_type_id, data_type_name in enumerate(["raw", "preprocessed"]):
            for i, sample in enumerate(results[data_type_id]["samples_data_normalized"]):
                save_csv_plot(sample,
                              f"{results_eval_dir}/{instructions['name']}/{data_type_name}_samples_data_normalized_{i}")
            for i, component in enumerate(results[data_type_id]["component_data"]):
                save_csv_plot(component,
                              f"{results_eval_dir}/{instructions['name']}/{data_type_name}_component_data_{i}")
            for i, cluster in enumerate(results[data_type_id]["cluster_data"]):
                save_csv_plot(cluster,
                              f"{results_eval_dir}/{instructions['name']}/{data_type_name}_cluster_data_{i}")
            save_csv_table([results[data_type_id]["explained_variance"]],
                           f"{results_eval_dir}/{instructions['name']}/{data_type_name}_explained_variance")
    else:
        exit(1)


plot_count = 0


def plot_one(curve, name):
    plot = Plot()


def preprocess_all(data, instructions, evaluation_name):
    preprocessed = np.copy(data)
    for_each_first_curve_in_suite(data, plot_one, f"{evaluation_name}-initial")
    for instr in instructions:
        preprocessed = preprocess_all_with_instr(preprocessed, instr)
    return preprocessed


def load_data(suite_names):
    """[suite_id, file_id, x/y, point]"""
    data = []
    if np.size(suite_names) == 0:
        return data
    if suite_names[0] == "experimental":
        data = import_juices()
        return data
    for suite_id, suite_name in enumerate(suite_names):
        data.append([])
        i = 0
        while isfile(get_suite_filepath(suite_name, i)):
            data[suite_id].append(load_csv_plot(get_suite_filepath(suite_name, i)))
            i = i + 1
    return data


def load_noise(suite_names):
    """[suite_id, file_id, x/y, point]"""
    data = []
    for suite_id, suite_name in enumerate(suite_names):
        data.append([])
        i = 0
        while isfile(get_suite_filepath(suite_name, i)):
            data[suite_id].append(load_csv_plot(f"{get_suite_filepath(suite_name, i)}_noise"))
            i = i + 1
    return data


def load_baseline(suite_names):
    """[suite_id, file_id, x/y, point]"""
    data = []
    for suite_id, suite_name in enumerate(suite_names):
        data.append([])
        i = 0
        while isfile(get_suite_filepath(suite_name, i)):
            data[suite_id].append(load_csv_plot(f"{get_suite_filepath(suite_name, i)}_baseline"))
            i = i + 1
    return data



def evaluate_all():
    # evaluate('sample_ml_pca')
    # evaluate('sample')
    # evaluate('sample_ml')
    # evaluate('SG_PLbase/SG_easy_RMSE')
    # evaluate('SG_PLbase/SG_hard_RMSE')
    # evaluate('SG_PLbase/SG_easy_PCA')
    # evaluate('SG_PLbase/SG_hard_PCA')
    # evaluate('SG_PLbase/SG_experimental_PCA')
    # evaluate('SG_PLbase/PL_easy_RMSE')
    # evaluate('SG_PLbase/PL_hard_RMSE')
    # evaluate('SG_PLbase/PL_easy_PCA')
    # evaluate('SG_PLbase/PL_hard_PCA')
    # evaluate('SG_PLbase/PL_experimental_PCA')
    # evaluate('SG_PLbase/SGPL_easy_RMSE')
    # evaluate('SG_PLbase/SGPL_hard_RMSE')
    # evaluate('SG_PLbase/SGPL_easy_PCA')
    # evaluate('SG_PLbase/SGPL_hard_PCA')
    # evaluate('SG_PLbase/SGPL_experimental_PCA')
    evaluate('new_methods/PL_easy_RMSE')
    evaluate('new_methods/PL_hard_RMSE')
    evaluate('new_methods/SG_easy_RMSE')
    evaluate('new_methods/SG_hard_RMSE')
    evaluate('new_methods/SGPL_easy_RMSE')
    evaluate('new_methods/SGPL_hard_RMSE')


if __name__ == '__main__':
    evaluate_all()