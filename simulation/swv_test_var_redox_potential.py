from utils.plot import Plot
from utils.filesystem import save_csv
import simulation.swv_simulation as swv
import numpy as np


def simulate_var_redox_potential():
    new_plot = Plot()
    maxima_positions = []

    for n in range(1, 4):
        results = swv.simulate_from_json("../simulation/config/var_redox_potential/redox_potential"+str(n)+".json")
        save_csv(results, '../results/simulation/var_redox_potential/swv_curve_'+str(200*(n-2))+"_mV.csv")
        new_plot.add_plot(results, str(200*(n-2))+" mV")
        maxima_positions.append(results[0][np.argmax(results[1])])

    print(maxima_positions)

    new_plot.save('../results/simulation/var_redox_potential/swv_curve_var_redox_potential.png')


if __name__ == '__main__':
    simulate_var_redox_potential()