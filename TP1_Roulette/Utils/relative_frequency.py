def get_relative_frequency_of(number, array):
    occurrences = (array == number).sum()

    return occurrences / array.size
