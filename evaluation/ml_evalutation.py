import json

import numpy as np
from numpy import sqrt

import evaluation.ml_algorithms as algo
from config.config import cfg_eval_dir


def ml_assessment(raw, preprocessed, cfg):
    correct_raw, size, solution_raw, solution = MLAssessor(raw, cfg).solve()
    correct_preprocessed, _, solution_preprocessed, _ = MLAssessor(preprocessed, cfg).solve()

    improved = 0
    worsened = 0
    for raw_guess, preprocessed_guess, correct in zip(solution_raw, solution_preprocessed, solution):
        if raw_guess == correct and preprocessed_guess != correct:
            worsened = worsened + 1
        elif raw_guess != correct and preprocessed_guess == correct:
            improved = improved + 1

    return {'correct_raw': correct_raw / size, 'correct_preprocessed': correct_preprocessed / size,
            'improved': improved / size, 'worsened': worsened / size, 'stderr': 1 / sqrt(size)}


class MLAssessor:
    def __init__(self, data, cfg):
        self.data = data
        with open(f'{cfg_eval_dir}/{cfg}') as config_file:
            self.config = json.load(config_file)

        self.training_data = []
        self.training_solution = []
        self.testing_data = []
        self.testing_solution = []

        for suite_id, suite in enumerate(data):
            for i, curve in enumerate(suite):
                if i * 100 < self.config["training_curves_percent"] * len(suite):
                    self.training_data.append(curve[1])
                    self.training_solution.append(suite_id)
                else:
                    self.testing_data.append(curve[1])
                    self.testing_solution.append(suite_id)

    def solve(self):
        ml_solution = []
        if self.config["algorithm"] == "DUMMY":
            ml_solution = np.zeros(len(self.testing_solution))
        elif self.config["algorithm"] == "LOGISTIC_REGRESSION":
            ml_solution = algo.logistic_regression(self.training_data, self.training_solution, self.testing_data)

        correct = 0
        for ml, real in zip(self.testing_solution, ml_solution):
            if ml == real:
                correct = correct + 1

        return correct, len(self.testing_solution), ml_solution, self.testing_solution
