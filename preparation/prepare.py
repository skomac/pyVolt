import json
import numpy as np

from config.config import cfg_prep_dir
from processing.disturbing import disturb
from results.results import results_prep_dir, results_sim_dir
from utils.filesystem import load_csv_plot, save_csv_plot
from scipy import interpolate

from utils.plot import Plot
from utils.unit_conversion import MV_TO_V


def prepare_shape(potential_range, shape):
    potential = np.arange(potential_range[0], potential_range[1], potential_range[2])
    current = np.zeros(np.size(potential))

    for peak in shape:
        base_peak = load_csv_plot(f"{results_sim_dir}/{peak['base_peak']}")
        height = np.max(base_peak[1])
        # linear interpolation of moved curve to align X values
        f = interpolate.interp1d(base_peak[0], base_peak[1], fill_value=0, bounds_error=False)
        interpolated = np.array(f(potential + peak['position']))
        current = current + interpolated * scale(height, peak['height'], peak['height_stderr_fraction'])

    return np.array([potential, current])


def scale(original_height, desired_height, disturbtion_fraction):
    return desired_height / original_height * (1. + np.random.default_rng().normal(size=1) * disturbtion_fraction)


def add_baseline(curve, instructions):
    if instructions['type'] == 'DOUBLE_POWER':
        alpha = instructions['params'][0]
        a = instructions['params'][1]
        b = instructions['params'][2]
        magnitude = instructions['params'][3]

        x_size = np.size(curve[0])
        y_size = np.max(curve[1])
        multiplier = y_size * magnitude

        arguments = np.linspace(0, 1, x_size)
        baseline = alpha * (a+1) * np.float_power(arguments, a)+(1-alpha) * (b+1) * np.float_power(1-arguments, b)
        baseline = baseline * multiplier
        curve[1] = curve[1] + baseline

    return curve, np.array([curve[0], baseline])


def prepare(instructions):
    all_plot = Plot()

    for i in range(instructions['amount_of_curves']):
        curve = prepare_shape(instructions['potential_range'], instructions['shape'])
        if i == 0:
            add_baseline_plot = Plot()
            raw = np.copy(curve)

            disturb_plot = Plot()
            disturbed = disturb(np.copy(raw), instructions['noise_fraction'])
            disturb_plot.add_plot(disturbed, "Po generacji szumu")
            disturb_plot.add_plot(raw, "Wyjściowa krzywa", thick=True)
            disturb_plot.save(f"{results_prep_dir}/{instructions['name']}/{instructions['name']}_noise")

            with_baseline, baseline = add_baseline(np.copy(disturbed), instructions['baseline'])
            add_baseline_plot.add_plot(disturbed, "Wyjściowa krzywa")
            add_baseline_plot.add_plot(with_baseline, "Zmodyfikowana krzywa")
            add_baseline_plot.add_plot(baseline, "Wygenerowana linia bazowa", thick=True)

            add_baseline_plot.save(f"{results_prep_dir}/{instructions['name']}/{instructions['name']}_baseline")
            save_csv_plot(with_baseline, f"{results_prep_dir}/{instructions['name']}/{instructions['name']}_raw")
            save_csv_plot(baseline, f"{results_prep_dir}/{instructions['name']}/{instructions['name']}_baseline")
            all_plot.add_plot(raw, "raw")

            sample_plot = Plot()
            sample_plot.add_plot(with_baseline, None)
            sample_plot.save(f"{results_prep_dir}/{instructions['name']}/{instructions['name']}_sample")

        curve = disturb(curve, instructions['noise_fraction'])
        curve, _ = add_baseline(curve, instructions['baseline'])
        save_csv_plot(curve, f"{results_prep_dir}/{instructions['name']}/{instructions['name']}_{i}")
        all_plot.add_plot(curve, str(i))

    all_plot.save(f"{results_prep_dir}/{instructions['name']}/{instructions['name']}")


def prepare_from_json(cfg):
    print(f"Preparing '{cfg}' curves")
    with open(f'{cfg_prep_dir}/{cfg}.json', 'r') as config_file:
        instructions = json.load(config_file)
    prepare(instructions)


if __name__ == '__main__':
    print("Start preparation of simulation curves")
    prepare_from_json('sample')
    # prepare_from_json('ml_sample_dataset_0')
    # prepare_from_json('ml_sample_dataset_1')
    # prepare_from_json('ml_sample_dataset_2')
    prepare_from_json('pca_sample_dataset_0')
    prepare_from_json('pca_sample_dataset_1')
    prepare_from_json('pca_sample_dataset_2')
    print("Prepared all simulation curves")
