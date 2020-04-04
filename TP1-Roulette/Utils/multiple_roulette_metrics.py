from Utils.single_roulette_metrics import generate_multi_metrics_array
import numpy as np


def merge_multi_metric_arrays(iters, multi_metric_array_list):
    merged_multi_metric_array = np.ndarray((4, iters))

    for i in range(iters):
        sum_of_averages = 0
        for array in multi_metric_array_list:
            sum_of_averages = sum_of_averages + array[1][i]
        merged_multi_metric_array[1][i] = sum_of_averages / len(multi_metric_array_list)
