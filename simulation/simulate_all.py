from simulation.swv_test_basic import simulate_basic
from simulation.swv_test_var_initial_concentration import simulate_var_initial_concentration
from simulation.swv_test_var_redox_potential import simulate_var_redox_potential
from simulation.swv_test_var_no_of_electrons import simulate_var_no_of_electrons


def simulate_all():
    simulate_basic()
    simulate_var_no_of_electrons()
    simulate_var_redox_potential()
    simulate_var_initial_concentration()


if __name__ == '__main__':
    simulate_all()