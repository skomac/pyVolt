import numpy as np


def for_each_curve(data, function, *args, shape_change=False):
    #modifying input!
    shape = np.shape(data)
    for suite_id, suite in enumerate(data):
        for i, curve in enumerate(suite):
            data[suite_id][i] = function(curve, *args)
    if not shape_change:
        print(shape)
        print(np.shape(data))
        assert shape == np.shape(data)
    return data