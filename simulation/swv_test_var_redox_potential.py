from config.config import cfg_sim_dir
from results.results import results_sim_dir
from utils.plot import Plot
from utils.filesystem import save_csv_plot, write_to_file
import simulation.swv_simulation as swv
import numpy as np


def simulate_var_redox_potential():
    new_plot = Plot(title="Zmienny potencjał równowagowy")
    maxima_positions = []

    for n in range(1, 4):
        results = swv.simulate_from_json(f"{cfg_sim_dir}/var_redox_potential/redox_potential{n}.json")
        save_csv_plot(results, f"{results_sim_dir}/var_redox_potential/swv_curve_{200 * (n - 2)}_mV.csv")
        new_plot.add_plot(results, str(200 * (n - 2)) + " mV")
        maxima_positions.append(results[0][np.argmax(results[1])])

    info = f"Maxima positions (should be -0.2, 0.0, +0.2):\n{maxima_positions}"
    write_to_file(f"{results_sim_dir}/var_redox_potential/results.txt", info)

    new_plot.save(f'{results_sim_dir}/var_redox_potential/swv_curve_var_redox_potential.png')


if __name__ == '__main__':
    simulate_var_redox_potential()