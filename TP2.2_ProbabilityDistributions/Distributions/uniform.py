import numpy as np
from Utils.generic_test import generic_test

def uniform_num(a,b):
    r = np.random.uniform()
    return r*(b-a) + a

def inverse_uniform_num(a,b):
    r = np.random.uniform()
    return a + (b-a) * r

def test_uniform(length, a, b):
    generic_test(
        test_name=f"Uniform (a: {a}|b: {b}| length: {length})",
        sequence=np.array([uniform_num(a,b) for _ in range(length)]),
        expected_mean=(b + a)/2,
        expected_var=((b-a)**2)/12,
    )


