from utils.filesystem import load_csv_plot
from processing.disturbing import disturb
from utils.plot import Plot
from processing.assessment import signal_recovery, residual_curve

import numpy as np
import scipy.signal as sig

sample = load_csv_plot("../results/simulation/basic/swv_curve.csv")
disturbed = disturb(np.copy(sample), 0.01)
filtered = np.copy(disturbed)
print(filtered)
filtered[1] = sig.savgol_filter(filtered[1], 31, 2)

residual_org = residual_curve(sample, disturbed)
residual_filt = residual_curve(sample, filtered)
print(residual_org)
height_org = np.max(sample[1])
height_dis = np.max(disturbed[1])
height_fil = np.max(filtered[1])
print(f"org:{height_org}, dis:{height_dis}, fil:{height_fil}")
dist_fact = (height_dis-height_org)/height_org
filt_fact = (height_fil-height_org)/height_org
print(f"disturbtion factor:{dist_fact}")
print(f"filtered factor:{filt_fact}")
print(f"correctness factor:{np.abs(np.array([dist_fact/filt_fact]))}")

res_org = np.sqrt(np.sum(residual_org[1] * residual_org[1]))
res_fil = np.sqrt(np.sum(residual_filt[1] * residual_filt[1]))
recov = signal_recovery(sample, disturbed, filtered)
print(res_org)
print(res_fil)
print(res_fil/res_org)
print(f"recov: {recov}")

plot = Plot()
plot.add_plot(disturbed, 'disturbed')
plot.add_plot(filtered, 'filtered')
plot.add_plot(residual_org, 'residual')
plot.add_plot(residual_filt, 'residual-filt')
plot.show()

arr = np.array([[0, 1, 2], [1, 2, 3]])
print(arr)
print(arr * arr)
