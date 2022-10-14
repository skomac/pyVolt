import numpy as np

from results.results import results_prep_dir
from utils.filesystem import load_csv_plot
from utils.plot import Plot

plot = Plot(title='Wygenerowane krzywe')

sample1 = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_0/ml_sample_dataset_0_0")
plot.add_plot(sample1, "Zestaw 1")

sample2 = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_1/ml_sample_dataset_1_0")
plot.add_plot(sample2, "Zestaw 2")

sample3 = load_csv_plot(f"{results_prep_dir}/ml_sample_dataset_2/ml_sample_dataset_2_0")
plot.add_plot(sample3, "Zestaw 3")


plot.show()