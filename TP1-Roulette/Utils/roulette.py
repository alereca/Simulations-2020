import random as rand

def generate_array_of_rf(selected_num, num_iters):
    occurrences = 0
    for num_of_iteration in range(1, num_iters):
        if selected_num == rand.randint(0, 36):
            occurrences += 1
        yield occurrences / num_of_iteration