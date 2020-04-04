from Utils.roulette import generate_metrics_array
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
    metrics_array = generate_metrics_array(
        selected_num, num_iters)
    plot_graph(metrics_array, num_iters, selected_num, expected_values)
