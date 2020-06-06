import numpy as np
import math
from pytest import approx
from Utils.check_approximation import check_approximation


def exponential_num(lmda):
    r = np.random.uniform()
    return -(1 / lmda) * math.log(r)


def test_exponential(length, lmda):
    sequence = np.array([exponential_num(lmda) for _ in range(length)])

    expected_mean = 1 / lmda
    observed_mean = sequence.mean()

    expected_var = 1 / (lmda ** 2)
    observed_var = sequence.var()

    print(f"Exponential lambda: {lmda} length: {length}")
    print("Mean: ", check_approximation(expected_mean, observed_mean))
    print(expected_mean, observed_mean)
    print("Var: ", check_approximation(expected_var, observed_var))
    print(expected_mean, observed_var)
