from config.config import cfg_sim_dir
from results.results import results_sim_dir
from utils.plot import Plot
from utils.filesystem import save_csv_plot, write_to_file
import simulation.swv_simulation as swv
import numpy as np


def simulate_var_initial_concentration():
    new_plot = Plot(title="Zmienne stężenie analitu")
    maxima = []

    for n in range(1, 4):
        results = swv.simulate_from_json(
            f"{cfg_sim_dir}/var_initial_concentration/initial_concentration_x{n}.json")
        save_csv_plot(results, f"{results_sim_dir}/var_initial_concentration/swv_curve_{n}_mM.csv")
        new_plot.add_plot(results, f"{n}" + " mmol/dm$^{-3}$")
        maxima.append(np.max(results[1]))

    info = f"Maxima values:\n{maxima}\n"
    info += f"max(double concentration)/max(normal concentration) - should be 2.0:\n{maxima[1] / maxima[0]}\n"
    info += f"max(triple concentration)/max(normal concentration) - should be 3.0:\n{maxima[2] / maxima[0]}\n"
    write_to_file(f'{results_sim_dir}/var_initial_concentration/results.txt', info)

    new_plot.save(f'{results_sim_dir}/var_initial_concentration/swv_curve_var_initial_concentration.png')


if __name__ == '__main__':
    simulate_var_initial_concentration()
