from Utils.roulette import generate_array_of_rf
from Graphs.line_plot import plot_graph

selected_num = 21
num_iters = 1500
expected_rf = 18

if __name__ == "__main__":
    rf_list = generate_array_of_rf(
        selected_num, num_iters)
    print(rf_list[1])
    plot_graph(rf_list[1], num_iters, selected_num, expected_rf)
