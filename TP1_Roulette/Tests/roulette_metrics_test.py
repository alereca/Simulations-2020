from ..Utils.roulette_metrics import generate_multi_metrics_array
import numpy as np
import numpy.testing as npt


#    execute test suite with command:
#    /usr/bin/python3 -m pytest
def test_generate_multi_metrics_array():
    # Arrange
    random_elements_populations = [
        np.array([0]),
        np.array([2, 36]),
        np.array([11, 2, 29])
    ]
    selected_num = 2
    num_iterations = len(random_elements_populations)
    # Act
    results = generate_multi_metrics_array(
        random_elements_populations,
        selected_num,
        num_iterations)
    # Arrange
    npt.assert_array_equal(results, np.array([
        np.array([
            0,
            (1/2),
            (1/3)
        ]),
        np.array([
            0,
            (2 + 36) / 2,
            (11 + 2 + 29) / 3
        ]),
        np.array([
            0,
            (((2 - 19)**2 + (36 - 19)**2) / 2) ** (1/2),
            (((11 - 14)**2 + (2 - 14)**2 + (29 - 14)**2) / 3) ** (1/2)
        ]),
        np.array([
            0,
            ((2 - 19)**2 + (36 - 19)**2) / 2,
            ((11 - 14)**2 + (2 - 14)**2 + (29 - 14)**2) / 3
        ])
    ]))
