import numpy as np
import math
from Utils.generic_test import generic_test


def poisson_num(lmda):
    multiplicative_series = 1
    e_minus_lmda = math.exp(-lmda)
    x = 0
    while True:
        r = np.random.uniform()
        multiplicative_series *= r

        if multiplicative_series > e_minus_lmda:
            x += 1
        else:
            break

    return x


def test_poisson(length, lmda):
    generic_test(
        test_name=f"Poisson (lmda: {lmda}| length: {length})",
        sequence=np.array([poisson_num(lmda) for _ in range(length)]),
        expected_mean=lmda,
        expected_var=lmda,
    )
