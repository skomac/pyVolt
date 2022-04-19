from evaluation.evaluate import evaluate
from preparation.prepare import prepare_from_json
from simulation.simulate_all import simulate_all


def prepare_all():
    prepare_from_json('sample')
    prepare_from_json('ml_sample_dataset_0')
    prepare_from_json('ml_sample_dataset_1')


def evaluate_all():
    evaluate('sample_ml')
    evaluate('sample')


if __name__ == '__main__':
    simulate_all()
    prepare_all()
    evaluate_all()