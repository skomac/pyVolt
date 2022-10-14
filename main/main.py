from evaluation.evaluate import evaluate, evaluate_all
from misc.collect_all_data import collect_all_SGPL
from misc.collect_avg_rmse import collect_avg_rmse_sgpl
from misc.generation_results_merge import generation_results_merge
from misc.simulation_results_merge import simulation_results_merge
from preparation.prepare import prepare_from_json, prepare_all
from simulation.simulate_all import simulate_all


if __name__ == '__main__':
    simulate_all()
    prepare_all()
    evaluate_all()
    collect_all_SGPL()
    collect_avg_rmse_sgpl()
    simulation_results_merge()
    generation_results_merge()
