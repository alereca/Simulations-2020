import numpy as np
import functools

def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]

def empirical_discrete_num():
    r = np.random.uniform()

    distribution = {
        1: [0.273, 0.273],
        2: [0.037, 0.31],
        3: [0.195, 0.505],
        4: [0.009, 0.514],
        5: [0.124, 0.638],
        6: [0.058, 0.696],
        7: [0.062, 0.758],
        8: [0.151, 0.909],
        9: [0.047, 0.956],
        10: [0.044, 1],
    }

    return closest(distribution.items(), r)
