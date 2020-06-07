import numpy as np
from Utils.generic_test import generic_test


def normal_num(mean, std):
    acum = 0
    for _ in range(12):
        r = np.random.uniform()
        acum += r
    return std * (acum - 6) + mean


def test_normal(length, mean, std):
    generic_test(
        test_name=f"Normal (mean: {mean}| std: {std}| length: {length})",
        sequence=np.array([normal_num(mean, std) for _ in range(length)]),
        expected_mean=mean,
        expected_var=std ** 2
    )
