from utils.plot import Plot
from utils.filesystem import save_csv
import simulation.swv_simulation as swv
import numpy as np


def simulate_var_initial_concentration():
    new_plot = Plot()
    maxima = []

    for n in range(1, 4):
        results = swv.simulate_from_json("../simulation/config/var_initial_concentration/initial_concentration_x"+str(n)+".json")
        save_csv(results, '../results/simulation/var_initial_concentration/swv_curve_'+str(n)+"_mM.csv")
        new_plot.add_plot(results, str(n)+" mM")
        maxima.append(np.max(results[1]))

    print(maxima)
    print(maxima[1]/maxima[0])
    print(maxima[2]/maxima[0])

    new_plot.save('../results/simulation/var_initial_concentration/swv_curve_var_initial_concentration.png')


if __name__ == '__main__':
    simulate_var_initial_concentration()
