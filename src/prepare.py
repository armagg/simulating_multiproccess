import numpy as np


def prepare_first_conditions():

    y = np.arange(-9, -6.5, 0.5)
    y = np.append(y, np.arange(6.5, 9, 0.5))
    x = np.arange(6.5, 9, 0.5)
    z = np.arange(20, 25, 0.5)
    args = []
    for x0 in x:
        for y0 in y:
            for z0 in z:
                for func_n in range(2):
                    args.append((x0, y0, z0, func_n, ))

    return args
