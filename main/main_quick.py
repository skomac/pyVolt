from evaluation.evaluate import evaluate
from preparation.prepare import prepare_from_json
from simulation.simulate_all import simulate_all


def prepare_all():
    prepare_from_json('sample')


def evaluate_all():
    evaluate('sample')


if __name__ == '__main__':
    prepare_all()
    evaluate_all()