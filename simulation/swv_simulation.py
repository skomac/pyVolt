# noinspection PyUnresolvedReferences
import PyESP
import enum
import numpy as np
import json


class Technique(enum.Enum):
    mode_SWV = 1

    def __int__(self):
        return self.value


def simulate(cfg):
    PyESP.setup()
    PyESP.set_params(IP=cfg["initial_potential"], FP=cfg["final_potential"])  # initial and final potential
    PyESP.set_params(SI=int(cfg["step_potential"] * 1000.))  # Scan Increment (mV)
    PyESP.set_params(CP=cfg["equilibration_potential"], CT=cfg["equilibration_time"])  # conditioning out-of-equilibrium
    PyESP.set_params(Mode=int(Technique.mode_SWV), FR=cfg["SWV_frequency"],
                     PH=cfg["SWV_pulse_height"])  # square wave voltammetry / FR - frequency, PH - Pulse Height (mV)
    PyESP.set_params(ST=cfg["step_potential"] / 0.1)  # / ST - step_time

    ox_species = PyESP.addSpecies(cfg["ox_initial_concentration"], cfg["ox_diffusion_coeff"])
    red_species = PyESP.addSpecies(cfg["red_initial_concentration"], cfg["red_diffusion_coeff"])
    redox1 = PyESP.addRedox(ox_species, red_species, cfg["number_of_electrons"], cfg["equilibrium_potential"],
                            cfg["rate_constant"], cfg["charge_transfer_coefficient"])
    # run simulation
    [potential, current] = PyESP.simulate()

    # free memory --> temporary approach (might not even be necessary...)
    PyESP.destroy()

    result_potential = []
    result_current = []
    for i in range(1, len(potential) - 1):
        if potential[i] - potential[i - 1] < - cfg["SWV_pulse_height"] * 1.999 * 0.001:
            result_potential.append((potential[i] + potential[i - 1]) / 2.0)
            result_current.append(current[i] - current[i - 1])

    return np.array([result_potential, result_current])


def simulate_from_json(json_config):
    with open('../simulation/config/peak_basic.json', "r") as sim_config_file:
        config = json.load(sim_config_file)
    with open(json_config, "r") as sim_config_file:
        changes = json.load(sim_config_file)

    for k, v in changes.items():
        config[k] = v

    return simulate(config)
