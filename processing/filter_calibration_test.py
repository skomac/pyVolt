from utils.filesystem import load_csv_plot
from processing.disturbing import disturb
from utils.plot import Plot
from utils.curves import generate_series_of_curves, get_maxima_from_series

import numpy as np
import scipy.signal as sig
import scipy.stats as st

sample = load_csv_plot("../results/simulation/basic/swv_curve.csv")
concentrations = np.linspace(1.0, 5.0, 5)

height = np.max(sample[1])
heights = np.linspace(height, 5 * height, 5)
signals = generate_series_of_curves(sample, range(1, 6))

disturbed = np.copy(signals)
for i in range(0, 5):
    disturbed[i] = disturb(disturbed[i], 0.03)

filtered = np.copy(disturbed)
for i in range(0, 5):
    filtered[i][1] = sig.savgol_filter(filtered[i][1], 31, 2)


heights_dist = get_maxima_from_series(disturbed)
heights_filtered = get_maxima_from_series(filtered)
print(heights)
print(heights_dist)
print(heights_filtered)
original_regress = st.linregress(concentrations, heights)
disturbed_regress = st.linregress(concentrations, heights_dist)
filtered_regress = st.linregress(concentrations, heights_filtered)
print(original_regress)
print(disturbed_regress)
print(filtered_regress)
disturbed_slope_error = np.abs((disturbed_regress.slope - original_regress.slope)/original_regress.slope)
filtered_slope_error = np.abs((filtered_regress.slope - original_regress.slope)/original_regress.slope)
print(f"Slope error disturbed: {disturbed_slope_error}; filtered: {filtered_slope_error}")


plot = Plot()
for curve in signals:
    plot.add_plot(curve, f'{np.max(curve[1])}')

plot.show()

plot2 = Plot()
for curve in disturbed:
    plot2.add_plot(curve, f'{np.max(curve[1])}')

plot2.show()

plot3 = Plot()
for curve in filtered:
    plot3.add_plot(curve, f'{np.max(curve[1])}')

plot3.show()
