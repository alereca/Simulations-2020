def check_approximation(expected, observed):
    return (0.9 <= observed / expected <= 1.1, observed / expected)
