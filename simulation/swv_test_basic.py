import simulation.swv_simulation as swv
from utils.plot import Plot
from utils.filesystem import save_csv


def simulate_basic():
    results = swv.simulate_from_json("../simulation/config/peak_basic.json")

    save_csv(results, '../results/simulation/basic/swv_curve.csv')

    new_plot = Plot()
    new_plot.add_plot(results, 'Basic peak')
    new_plot.save('../results/simulation/basic/swv_curve.png')


if __name__ == '__main__':
    simulate_basic()
