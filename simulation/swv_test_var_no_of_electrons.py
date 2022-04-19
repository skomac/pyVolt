from config.config import cfg_sim_dir
from results.results import results_sim_dir
from utils.filesystem import save_csv_plot
import simulation.swv_simulation as swv
from utils.plot import Plot


def simulate_var_no_of_electrons():
    new_plot = Plot(title="Zmienne n")

    for n in range(1, 4):
        results = swv.simulate_from_json(f"{cfg_sim_dir}/var_no_of_electrons/{n}_electron.json")
        save_csv_plot(results, f"{results_sim_dir}/var_no_of_electrons/swv_curve_{n}_electron")
        new_plot.add_plot(results, f"n = {n}")

    new_plot.save(f'{results_sim_dir}/var_no_of_electrons/swv_curve_var_no_of_electrons.png')


if __name__ == '__main__':
    simulate_var_no_of_electrons()
