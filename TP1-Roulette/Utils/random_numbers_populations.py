import numpy as np


def generate_random_numbers_populations(size):
    random_numbers_populations = []
    for i in range(1, size + 1):
        random_numbers_populations.append(np.random.randint(0, 36, i))
    
    return random_numbers_populations
