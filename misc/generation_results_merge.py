import matplotlib.pyplot as plt
import numpy as np
import sys
from PIL import Image
from results.results import results_sim_dir, results_final_dir


def generation_results_merge():
    filenames = [
        f"{results_final_dir}/sample_generated_A.png",
        f"{results_final_dir}/sample_generated_B.png",
        f"{results_final_dir}/samples_generated_A.png",
        f"{results_final_dir}/samples_generated_B.png"
    ]

    images = [Image.open(x) for x in filenames]
    width, height = images[0].size

    merged = Image.new('RGB', (width * 2, height * 2))
    merged.paste(images[0], (0, 0))
    merged.paste(images[1], (width, 0))
    merged.paste(images[2], (0, height))
    merged.paste(images[3], (width, height))

    merged.save("generation_results_merge.png", "PNG")


if __name__ == '__main__':
    generation_results_merge()
