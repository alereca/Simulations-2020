import numpy as np
from Utils.generic_test import generic_test
import math


def gamma_num(lmda, k, tr=1):
    trg = tr
    for i in range(k):
        r = np.random.uniform()
        trg = tr * r
    return -math.log(trg) / lmda


def test_gamma(length, lmda, k, tr=1):
    generic_test(
        test_name=f"Gamma (a: {lmda}|k: {k}| length: {length})",
        sequence=np.array([gamma_num(lmda, k) for _ in range(length)]),
        expected_mean=k / lmda,
        expected_var=k / lmda ** 2,
    )
