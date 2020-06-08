import numpy as np


def empirical_discrete_num():
    r = np.random.uniform()

    if 0 <= r < 0.1:
        return 2
    elif 0.1 <= r < 0.2:
        return 3
    elif 0.2 <= r < 0.35:
        return 7
    elif 0.35 <= r < 0.50:
        return 6
    elif 0.5 <= r < 0.7:
        return 9
    elif 0.7 <= r < 0.8:
        return 4
    elif 0.8 <= r < 0.95:
        return 1
    elif 0.95 <= r <= 1:
        return 0
