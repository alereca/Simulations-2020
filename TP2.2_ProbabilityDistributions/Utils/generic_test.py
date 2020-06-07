from Utils.check_approximation import check_approximation


def generic_test(test_name, sequence, expected_mean, expected_var):
    observed_mean = sequence.mean()
    observed_var = sequence.var()

    print(test_name)
    print("Mean: ", check_approximation(expected_mean, observed_mean))
    print(expected_mean, observed_mean)
    print("Var: ", check_approximation(expected_var, observed_var))
    print(expected_var, observed_var)
