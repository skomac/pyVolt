import json

import numpy as np

from config.config import cfg_eval_dir
from evaluation.filter_evaluation import signal_recovery_evaluation, rmse_evaluation
from evaluation.ml_evalutation import ml_assessment
from evaluation.pca_evalutation import pca_assessment
from evaluation.preprocess import preprocess, preprocess_all_with_instr
from results.results import results_prep_dir, results_eval_dir
from utils.filesystem import load_csv_plot, save_csv_table, save_csv_dict
from os.path import isfile


def get_suite_filepath(suite_name, index):
    return f"../results/preparation/{suite_name}/{suite_name}_{index}"


def evaluate(cfg):
    with open(f'{cfg_eval_dir}/{cfg}.json', 'r') as config_file:
        instructions = json.load(config_file)

    data = load_data(instructions["initial_data"])

    preprocessed = preprocess_all(data, instructions['preprocessing_instructions'])

    if instructions["eval_type"] == "SIGNAL_RECOVERY":
        raw_data = []
        for suite_name in instructions["initial_data"]:
            raw_data.append(load_csv_plot(f"{results_prep_dir}/{suite_name}/{suite_name}_raw"))
        save_csv_table(signal_recovery_evaluation(data, preprocessed, raw_data),
                       f"{results_eval_dir}/{instructions['name']}",
                       ["Signal recovery"])
    elif instructions["eval_type"] == "RMSE":
        raw_data = []
        for suite_name in instructions["initial_data"]:
            raw_data.append(load_csv_plot(f"{results_prep_dir}/{suite_name}/{suite_name}_raw"))
        save_csv_table(rmse_evaluation(data, preprocessed, raw_data), f"{results_eval_dir}/{instructions['name']}",
                       ["Original RMSE", "Preprocessed RMSE"])
    elif instructions["eval_type"] == "ML_ASSESSMENT":
        save_csv_dict(ml_assessment(data, preprocessed, instructions["eval_config"]),
                      f"{results_eval_dir}/{instructions['name']}")
    elif instructions["eval_type"] == "PCA_ASSESSMENT":
        save_csv_dict(pca_assessment(data, preprocessed, instructions["eval_config"]),
                      f"{results_eval_dir}/{instructions['name']}")
    else:
        exit(1)


def preprocess_all(data, instructions):
    preprocessed = []
    for suite in data:
        processed_suite = []
        for curve in suite:
            processed_suite.append(preprocess(curve, instructions))
        preprocessed.append(processed_suite)
    return preprocessed
    # preprocessed = np.copy(data)
    # for instr in instructions:
    #     preprocessed = preprocess_all_with_instr(preprocessed, instr)
    # return preprocessed


def load_data(suite_names):
    """[suite_id, file_id, x/y, point]"""
    data = []
    for suite_id, suite_name in enumerate(suite_names):
        data.append([])
        i = 0
        while isfile(get_suite_filepath(suite_name, i)):
            data[suite_id].append(load_csv_plot(get_suite_filepath(suite_name, i)))
            i = i + 1
    return data


if __name__ == '__main__':
    evaluate('sample_ml_pca')
    evaluate('sample')
    evaluate('sample_ml')
