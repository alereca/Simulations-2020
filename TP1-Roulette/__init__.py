from Utils.single_roulette_metrics import generate_multi_metrics_array
from Utils.multiple_roulette_metrics import merge_multi_metric_arrays
from Graphs.line_plot import plot_graph

selected_num = 7
num_iters = 1000
expected_values = {
    "rf": 1 / 37,
    "avg": 18,
    "std": 10,
    "var": 110
}

if __name__ == "__main__":
    """ metrics_array = generate_multi_metrics_array(
        selected_num, num_iters) """
    merged_multi_metrics_array = merge_multi_metric_arrays(num_iters, [
        generate_multi_metrics_array(7, num_iters),
        generate_multi_metrics_array(7, num_iters),
        generate_multi_metrics_array(7, num_iters)
    ])
    plot_graph(merged_multi_metrics_array, num_iters, selected_num, expected_values)
