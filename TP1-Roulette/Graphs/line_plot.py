import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from Graphs.subplot import general_generate_subplot
from Graphs.params import Params


def plot_graph(multi_metrics_array, n_iter, num, expected_values):
    x = np.arange(0, n_iter)

    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.5)

    specific_plot_generator = general_generate_subplot(
        figure=fig,
        x_axis=x,
        n_iter=n_iter)
        
    specific_plot_generator(
        metrics_array=multi_metrics_array[0],
        expected_value=expected_values["rf"],
        params=Params(
            title="Relative Frequency",
            xlabel="Iteration Number (n)",
            ylabel=f"RF of number {num}(rf)",
            position=1))

    specific_plot_generator(
        metrics_array=multi_metrics_array[1],
        expected_value=expected_values["avg"],
        params=Params(
            title="Mean",
            xlabel="Iteration Number (n)",
            position=2))
    
    specific_plot_generator(
        metrics_array=multi_metrics_array[2],
        expected_value=expected_values["std"],
        params=Params(
            title="Standard Deviation",
            xlabel="Iteration Number (n)",
            position=3))
    
    specific_plot_generator(
        metrics_array=multi_metrics_array[3],
        expected_value=expected_values["var"],
        params=Params(
            title="Variance",
            xlabel="Iteration Number (n)",
            position=4))

    fig.savefig("roulette_metrics.jpg")
