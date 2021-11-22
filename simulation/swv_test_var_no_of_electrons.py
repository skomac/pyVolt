from utils.filesystem import save_csv
import simulation.swv_simulation as swv
from utils.plot import Plot

def simulate_var_no_of_electrons():
    new_plot = Plot()

    for n in range(1, 4):
        results = swv.simulate_from_json("../simulation/config/var_no_of_electrons/"+str(n)+"_electron.json")
        save_csv(results, '../results/simulation/var_no_of_electrons/swv_curve_'+str(n)+"_electron")
        new_plot.add_plot(results, str(n)+" electron")

    new_plot.save('../results/simulation/var_no_of_electrons/swv_curve_var_no_of_electrons.png')

if __name__ == '__main__':
    simulate_var_no_of_electrons()
