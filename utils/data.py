import numpy as np


def for_each_curve(data, function, *args):
    # modifying input!
    shape = np.shape(data)
    for suite_id, suite in enumerate(data):
        for i, curve in enumerate(suite):
            data[suite_id][i] = function(curve, *args)
    assert shape == np.shape(data)
    return data


def for_each_curve_modify_shape(data, function, *args):
    processed = []
    for suite in data:
        processed_suite = []
        for curve in suite:
            processed_suite.append(function(curve, *args))
        processed.append(processed_suite)
    data = processed
    return data


def for_each_first_curve_in_suite(data, function, *args):
    for suite in data:
        function(suite[0], *args)
    return data