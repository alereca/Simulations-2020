import numpy as np
from Utils.generic_test import generic_test
import math

def binomial_num(p,n):
    x = 0
    for i in range(n):
        r = np.random.uniform()
        if r <= p:
            x += 1
    return x

def test_binomial(length, p, n):
    generic_test(
        test_name=f"Binomial (p: {p}|n: {n}| length: {length})",
        sequence=np.array([binomial_num(p, n) for _ in range(length)]),
        expected_mean=n*p,
        expected_var=n*p*(1-p),
    )