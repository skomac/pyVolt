from config.config import cfg_sim_dir
from results.results import results_sim_dir
from utils.filesystem import save_csv_plot, write_to_file
import simulation.swv_simulation as swv
from utils.plot import Plot
import numpy as np
from evaluation.single_peak_parameters import collect_single_peak_params


def simulate_var_no_of_electrons():
    new_plot = Plot(title="Symulacja - proces n-elektronowy", figsize=[4.8, 3.6])
    peak_params = []

    for n in range(1, 4):
        results = swv.simulate_from_json(f"{cfg_sim_dir}/var_no_of_electrons/{n}_electron.json")
        save_csv_plot(results, f"{results_sim_dir}/var_no_of_electrons/swv_curve_{n}_electron")
        peak_params.append(collect_single_peak_params(results))
        results[1] = results[1] * 1.0e6
        new_plot.add_plot(results, f"n = {n}", thick=True)

    new_plot.save(f'{results_sim_dir}/var_no_of_electrons/swv_curve_var_no_of_electrons.png')

    info = f"Peak params:\n{peak_params}\n"
    write_to_file(f'{results_sim_dir}/var_no_of_electrons/maxima.txt', info)


if __name__ == '__main__':
    simulate_var_no_of_electrons()
