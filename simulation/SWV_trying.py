#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:05:22 2019

@author: limhes
"""

# noinspection PyUnresolvedReferences
import PyESP
import enum
import matplotlib.pyplot as plt
import csv

plt.style.use('ggplot')


class Technique(enum.Enum):
    mode_CV = 0
    mode_SWV = 1
    mode_CA = 2
    mode_SDC = 3

    def __int__(self):
        return self.value


class IR_mode(enum.Enum):
    ir_none = 0
    ir_ru = 1
    ir_dl = 2

    def __int__(self):
        return self.value


PyESP.setup()

# simulation variables
step_potential = 0.001  # V
SWV_frequency = 5.  # Hz
SWV_pulse_height = 25  # mV

# experimental variables
initial_potential = -500  # mV
final_potential = 500  # mV
equilibration_potential = -500  # mV
equilibration_time = 10  # s

# electrochemistry model
ox_initial_concentration = 1.0  # mM
ox_diffusion_coeff = 1.0e-5  # cm2/s
red_initial_concentration = 0.0  # mM
red_diffusion_coeff = 1.0e-5  # cm2/s
equilibrium_potential = 0  # mV
number_of_electrons = 1
rate_constant = 1e3  # 1/s
charge_transfer_coefficient = 0.5

PyESP.set_params(IP=initial_potential, FP=final_potential)  # initial and final potential
PyESP.set_params(SI=int(step_potential * 1000.))  # Scan Increment (mV)
PyESP.set_params(CP=equilibration_potential, CT=equilibration_time)  # conditioning out-of-equilibrium
PyESP.set_params(Mode=int(Technique.mode_SWV), FR=SWV_frequency,
                 PH=SWV_pulse_height)  # square wave voltammetry / FR - frequency, PH - Pulse Height (mV)
PyESP.set_params(ST=step_potential / 0.1)  # / ST - step_time

A = PyESP.addSpecies(ox_initial_concentration, ox_diffusion_coeff)
B = PyESP.addSpecies(red_initial_concentration, red_diffusion_coeff)
redox1 = PyESP.addRedox(A, B, number_of_electrons, equilibrium_potential, rate_constant, charge_transfer_coefficient)

# run simulation
[potential, current] = PyESP.simulate()
# plot results
plt.plot(potential, [i * 1.0e6 for i in current], label='Scan rate {:.1f} V/s'.format(0.1))

plt.xlabel('Potential [V]')
plt.ylabel('Current [uA]')
plt.xlim(-0.5, 0.5)
plt.legend()
plt.show()

with open('swv_curve', 'w', newline='\n') as csv_file:
    fieldnames = ['Potential [V]', 'Current [uA]']
    writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fieldnames)
    for i in range(0, len(potential)):
        writer.writerow([potential[i], current[i]])

# free memory --> temporary approach (might not even be necessary...)
PyESP.destroy()
