import numpy as np
from Utils.generic_test import generic_test
import math

def gamma_num(tr, a):
    r = np.random.uniform()
    tr = tr * r
    return -math.log(tr)/a

def test_gamma(length, a, k, tr=1):
    generic_test(
        test_name=f"Gamma (a: {a}|k: {k}| length: {length})",
        sequence=np.array([gamma_num(a, tr) for _ in range(length)]),
        expected_mean=k/a,
        expected_var=k/a**2,
    )