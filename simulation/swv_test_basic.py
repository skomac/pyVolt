import simulation.swv_simulation as swv
from config.config import cfg_sim_dir
from results.results import results_sim_dir
from utils.plot import Plot
from utils.filesystem import save_csv_plot


def simulate_basic():
    results = swv.simulate_from_json(f"{cfg_sim_dir}/peak_basic.json")

    save_csv_plot(results, f'{results_sim_dir}/basic/swv_curve.csv')

    new_plot = Plot()
    new_plot.add_plot(results, 'Basic peak')
    new_plot.save(f'{results_sim_dir}/basic/swv_curve.png')


if __name__ == '__main__':
    simulate_basic()
