import matplotlib.pyplot as plt
import csv
import json
# noinspection PyPep8Naming
import SWV_simulation as swv

with open("config/peak_basic.json", "r") as sim_config_file:
    config = json.load(sim_config_file)

[potential, current] = swv.simulate(config)

# save results to file
with open('swv_curve', 'w', newline='\n') as csv_file:
    fieldnames = ['Potential [V]', 'Current [uA]']
    writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fieldnames)
    for i in range(0, len(potential)):
        writer.writerow([potential[i], current[i]])

# plot results
plt.style.use('ggplot')

plt.plot(potential, [i * 1.0e6 for i in current], label='Scan rate {:.1f} V/s'.format(0.1))

plt.xlabel('Potential [V]')
plt.ylabel('Current [uA]')
plt.xlim(-0.5, 0.5)
plt.legend()

plt.show()
