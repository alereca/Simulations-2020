from Utils.random_numbers_populations import generate_random_numbers_populations
from Utils.roulette_metrics import generate_multi_metrics_array
from Graphs.line_plot import plot_graph

selected_num = 7
num_iters = 10000
expected_values = {
    "rf": 1 / 37,
    "avg": 18,
    "std": 114**(1/2),
    "var": 114
}

if __name__ == "__main__":
    plot_graph(
        n_iters=num_iters,
        num=selected_num,
        expected_values=expected_values,
        multi_metrics_arrays=[
            generate_multi_metrics_array(
                generate_random_numbers_populations(num_iters),
                selected_num, num_iters
            )
        ],
        file_out="single_run_roulette_metrics.jpg"
    )
    plot_graph(
        n_iters=num_iters,
        num=selected_num,
        expected_values=expected_values,
        multi_metrics_arrays=[
            generate_multi_metrics_array(
                generate_random_numbers_populations(num_iters),
                selected_num, num_iters
            ),
            generate_multi_metrics_array(
                generate_random_numbers_populations(num_iters),
                selected_num, num_iters
            ),
            generate_multi_metrics_array(
                generate_random_numbers_populations(num_iters),
                selected_num, num_iters
            ),
            generate_multi_metrics_array(
                generate_random_numbers_populations(num_iters),
                selected_num, num_iters
            ),
            generate_multi_metrics_array(
                generate_random_numbers_populations(num_iters),
                selected_num, num_iters
            ),
            generate_multi_metrics_array(
                generate_random_numbers_populations(num_iters),
                selected_num, num_iters
            )
        ],
        file_out="multi_run_roulette_metrics.jpg"
    )
