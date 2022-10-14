from matplotlib import pyplot as plt

import simulation.swv_simulation as swv
from config.config import cfg_sim_dir
from results.results import results_sim_dir
from utils.plot import Plot
from utils.filesystem import save_csv_plot
from mpl_toolkits.axes_grid1.inset_locator import (zoomed_inset_axes, InsetPosition,
                                                   mark_inset)


def simulate_visual():
    results = swv.simulate_from_json(f"{cfg_sim_dir}/peak_basic.json")
    results_raw = swv.simulate_from_json(f"{cfg_sim_dir}/peak_basic.json", useful_format=False)
    save_csv_plot(results_raw, f'{results_sim_dir}/visual/swv_visual_raw.csv')
    save_csv_plot(results, f'{results_sim_dir}/visual/swv_visual_processed.csv')
    results[1] = results[1]*1.0e6
    results_raw[1] = results_raw[1]*1.0e6

    new_plot = Plot(dotted=True, markersize=3, figsize=[4.8, 3.6], title="Przetwarzanie danych symulacyjnych")
    new_plot.add_plot(results_raw, 'wynik symulacji')
    new_plot.add_plot(results, 'dane przetworzone')

    new_plot.save(f'{results_sim_dir}/visual/swv_visual.png')


if __name__ == '__main__':
    simulate_visual()
