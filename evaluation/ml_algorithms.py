from sklearn.linear_model import LogisticRegression


def logistic_regression(training_data, training_solution, testing_data):
    estimator = LogisticRegression(random_state=0).fit(training_data, training_solution)
    ml_solution = estimator.predict(testing_data)
    return ml_solution

