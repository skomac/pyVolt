import matplotlib.pyplot as plt
import numpy as np
import sys
from PIL import Image


def voltage_curve_gen():
    figure_size = (4, 3)

    v_steps = np.linspace(0, 0.1, 11)
    v_inc = v_steps[1] - v_steps[0]

    t_steps = np.linspace(0, 5, 11)
    t_inc = t_steps[1] - t_steps[0]

    scv_v = []
    scv_t = []

    for v_step, t_step in zip(v_steps, t_steps):
        if t_step != 0:
            scv_v.append(v_step - v_inc)
            scv_t.append(t_step)
        scv_v.append(v_step)
        scv_t.append(t_step)

    plt.figure(figsize=figure_size, tight_layout=True)
    plt.style.use('ggplot')
    plt.title("SCV")
    plt.xlabel("t [s]")
    plt.ylabel("E [V]")
    plt.text(0.1, 0.09, "A", fontsize="xx-large")
    plt.plot(scv_t, scv_v)
    plt.savefig("SCV.png")

    npv_v = []
    npv_t = []

    for v_step, t_step in zip(v_steps, t_steps):
        if t_step == 0:
            npv_v.append(v_step)
            npv_t.append(t_step)
        else:
            npv_v.append(v_steps[0])
            npv_t.append(t_step - t_inc * 0.2)
            npv_v.append(v_step)
            npv_t.append(t_step - t_inc * 0.2)
            npv_v.append(v_step)
            npv_t.append(t_step)
            npv_v.append(v_steps[0])
            npv_t.append(t_step)

    plt.figure(figsize=figure_size, tight_layout=True)
    plt.style.use('ggplot')
    plt.title("NPV")
    plt.text(0.1, 0.09, "B", fontsize="xx-large")
    plt.plot(npv_t, npv_v)
    plt.xlabel("t [s]")
    plt.ylabel("E [V]")
    plt.savefig("NPV.png")

    dpv_v = []
    dpv_t = []
    pulse = 5 * v_inc

    for v_step, t_step in zip(v_steps, t_steps):
        if t_step == 0:
            dpv_v.append(v_step)
            dpv_t.append(t_step)
        else:
            dpv_v.append(v_step - v_inc)
            dpv_t.append(t_step - t_inc * 0.2)
            dpv_v.append(v_step + v_inc + pulse)
            dpv_t.append(t_step - t_inc * 0.2)
            dpv_v.append(v_step + v_inc + pulse)
            dpv_t.append(t_step)
            dpv_v.append(v_step)
            dpv_t.append(t_step)

    plt.figure(figsize=figure_size, tight_layout=True)
    plt.style.use('ggplot')
    plt.title("DPV")
    plt.xlabel("t [s]")
    plt.ylabel("E [V]")
    plt.plot(dpv_t, dpv_v)
    plt.text(0.1, 0.14, "C", fontsize="xx-large")
    plt.savefig("DPV.png")

    swv_v = []
    swv_t = []
    pulse = 5 * v_inc

    for v_step, t_step in zip(v_steps, t_steps):
        if t_step == 0:
            swv_v.append(v_step)
            swv_t.append(t_step)
        else:
            swv_v.append(v_step - v_inc)
            swv_t.append(t_step - t_inc * 0.5)
            swv_v.append(v_step + v_inc + pulse)
            swv_t.append(t_step - t_inc * 0.5)
            swv_v.append(v_step + v_inc + pulse)
            swv_t.append(t_step)
            swv_v.append(v_step)
            swv_t.append(t_step)

    plt.figure(figsize=figure_size, tight_layout=True)
    plt.style.use('ggplot')
    plt.title("SWV")
    plt.xlabel("t [s]")
    plt.ylabel("E [V]")
    plt.text(0.1, 0.14, "D", fontsize="xx-large")
    plt.plot(swv_t, swv_v)
    plt.savefig("SWV.png")

    images = [Image.open(x) for x in ["SCV.png", "NPV.png", "DPV.png", "SWV.png"]]
    width, height = images[0].size

    merged = Image.new('RGB', (width * 2, height * 2))
    merged.paste(images[0], (0, 0))
    merged.paste(images[1], (width, 0))
    merged.paste(images[2], (0, height))
    merged.paste(images[3], (width, height))

    merged.save("pulse_voltammetries.png", "PNG")


if __name__ == '__main__':
    voltage_curve_gen()
