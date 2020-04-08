import random as rand
import numpy as np
from Utils.relative_frequency import get_relative_frequency_of


def generate_multi_metrics_array(random_elements_populations, selected_num, num_iters):
    results = np.zeros((4, num_iters))
    for i in range(0, num_iters):
        population = random_elements_populations[i]
        results[0][i] = get_relative_frequency_of(
            selected_num, population)
        results[1][i] = population.mean()
        results[2][i] = population.std()
        results[3][i] = results[2][i] ** 2

    return results
