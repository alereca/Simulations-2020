import random as rand
import numpy as np


def generate_multi_metrics_array(selected_num, num_iters):
    selected_elements = np.ndarray(num_iters)
    results = np.ndarray((4, num_iters))
    occurrences = 0
    for i in range(0, num_iters):
        random_int = rand.randint(0, 36)
        selected_elements[i] = random_int

        if selected_num == random_int:
            occurrences += 1

        results[0][i] = occurrences / (i + 1)
        results[1][i] = selected_elements[0:i+1].mean()
        results[2][i] = selected_elements[0:i+1].std()
        results[3][i] = results[2][i] ** 2

    return results
