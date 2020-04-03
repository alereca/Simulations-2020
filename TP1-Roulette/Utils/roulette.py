import random as rand


def generate_array_of_rf(selected_num, num_iters):
    matrix = [[], []]
    occurrences = 0
    last_avg = 0
    last_variance = 0
    for i in range(1, num_iters):
        random_int = rand.randint(0, 36)
        if selected_num == random_int:
            occurrences += 1

        actual_rf = occurrences / i
        avg = ((last_avg * (i-1)) + random_int) / i
        last_variance = (random_int - avg)

        matrix[0].append(actual_rf)
        matrix[1].append(avg)
        last_avg = avg

    return matrix
