import numpy as np
from Utils.generic_test import generic_test


def pascal_num(k, q):
    multiplicative_series = 1
    for _ in range(k):
        r = np.random.uniform()
        multiplicative_series *= r
    return round(np.log10(multiplicative_series) / np.log10(q))


def test_pascal(length, k, q):
    generic_test(
        test_name=f"Pascal successes: {k} | fail probability {q} | length: {length}",
        sequence=np.array([pascal_num(k, q) for _ in range(length)]),
        expected_mean=k * q / (1 - q),
        expected_var=k * q / ((1 - q) ** 2),
    )
