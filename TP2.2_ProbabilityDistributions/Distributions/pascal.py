import numpy as np
from Utils.check_approximation import check_approximation


def pascal_num(k, q):
    multiplicative_series = 1
    for _ in range(k):
        r = np.random.uniform()
        multiplicative_series *= r
    return round(np.log10(multiplicative_series) / np.log10(q))


def test_pascal(length, k, q):
    sequence = np.array([pascal_num(k, q) for _ in range(length)])

    expected_mean = k * q / (1 - q)
    observed_mean = sequence.mean()

    expected_var = k * q / ((1 - q) ** 3)
    observed_var = sequence.var()

    print(f"Pascal successes: {k} fail probability {q} length: {length}")
    print("Mean: ", check_approximation(expected_mean, observed_mean))
    print(expected_mean, observed_mean)
    print("Var: ", check_approximation(expected_var, observed_var))
    print(expected_var, observed_var)
