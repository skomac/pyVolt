import matplotlib.pyplot as plt
import numpy as np
import sys
from PIL import Image
from results.results import results_sim_dir


def simulation_results_merge():
    filenames = [
        f"{results_sim_dir}/visual/swv_visual.png",
        f"{results_sim_dir}/var_initial_concentration/swv_curve_var_initial_concentration.png",
        f"{results_sim_dir}/var_no_of_electrons/swv_curve_var_no_of_electrons.png",
        f"{results_sim_dir}/var_redox_potential/swv_curve_var_redox_potential.png"
    ]

    images = [Image.open(x) for x in filenames]
    width, height = images[0].size

    merged = Image.new('RGB', (width * 2, height * 2))
    merged.paste(images[0], (0, 0))
    merged.paste(images[1], (width, 0))
    merged.paste(images[2], (0, height))
    merged.paste(images[3], (width, height))

    merged.save("simulation_results_merge.png", "PNG")


if __name__ == '__main__':
    simulation_results_merge()
