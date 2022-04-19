import numpy as np


def get_gram_polynomial(m, k):
    if k == -1:
        return np.array([])
    elif k == 0:
        return np.array([1.])

    numerator1 = 2 * (2 * k - 1)
    numerator2 = (k - 1) * (2 * m + k)
    denominator = k * (2 * m - k + 1)

    result = numerator1 / denominator * get_gram_polynomial(m, k - 1)
    result = np.append(result, [0.])

    result2 = numerator2 / denominator * get_gram_polynomial(m, k - 2)
    result2 = np.append(np.array([0., 0.]), result2)

    return result - result2


def average_to_reduce(data, target_no_points):
    length = np.size(data)
    new_points = np.linspace(0, length, target_no_points+1)
    new_points = np.floor(new_points)

    new_data = []

    for pointA, pointB in zip(new_points[0:np.size(new_points)-1], new_points[1:]):
        new_data.append(np.average(data[int(pointA):int(pointB)]))

    return np.array(new_data)