from results.results import results_eval_dir
from utils.filesystem import load_csv_table, load_csv_dict

print(load_csv_dict(f"{results_eval_dir}/sample_name_of_machine_learning_evaluation", 0))
print(load_csv_table(f"{results_eval_dir}/sample_name_of_signal_recovery_evaluation", 1))
