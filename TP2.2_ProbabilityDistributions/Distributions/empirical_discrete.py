import numpy as np
from Utils.generic_test import generic_test

distribution = {
    1: [0.273, 0.273],
    2: [0.037, 0.31],
    3: [0.195, 0.505],
    4: [0.009, 0.514],
    5: [0.124, 0.638],
    6: [0.058, 0.696],
    7: [0.062, 0.758],
    8: [0.151, 0.909],
    9: [0.047, 0.956],
    10: [0.044, 1],
}


def find_number_by_accumulative_probability(dict_tuples, random_num):
    for (key, value) in dict_tuples:
        if random_num <= value[1]:
            return key


def calculate_mean():
    return sum([key * value[0] for (key, value) in distribution.items()])


def calculate_var(mean):
    return sum(
        [((key - mean) ** 2) * value[0] for (key, value) in distribution.items()]
    )


def empirical_discrete_num():
    r = np.random.uniform()

    return find_number_by_accumulative_probability(distribution.items(), r)


def test_empirical_discrete(length):
    expected_mean = calculate_mean()
    expected_var = calculate_var(expected_mean)

    generic_test(
        test_name=f"Empirical discrete(length: {length})",
        sequence=np.array([empirical_discrete_num() for _ in range(length)]),
        expected_mean=expected_mean,
        expected_var=expected_var,
    )
