import numpy as np
from Utils.generic_test import generic_test


def exponential_num(lmda):
    r = np.random.uniform()
    return -(1 / lmda) * np.log(r)


def test_exponential(length, lmda):
    generic_test(
        test_name=f"Exponential lambda: {lmda} | length: {length}",
        sequence=np.array([exponential_num(lmda) for _ in range(length)]),
        expected_mean=1 / lmda,
        expected_var=1 / (lmda ** 2),
    )
