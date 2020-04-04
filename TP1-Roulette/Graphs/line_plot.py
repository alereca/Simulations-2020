import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from Graphs.subplot import general_generate_subplot
from Graphs.params import Params


def plot_graph(multi_metrics_arrays, n_iters, num, expected_values, file_out):
    x = np.arange(0, n_iters)

    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.5)

    specific_plot_generator = general_generate_subplot(
        figure=fig,
        x_axis=x,
        n_iters=n_iters)
        
    specific_plot_generator(
        metrics_arrays=[arr[0] for arr in multi_metrics_arrays],
        expected_value=expected_values["rf"],
        params=Params(
            title="Relative Frequency",
            xlabel="Iteration Number (n)",
            ylabel=f"RF of number {num}(rf)",
            position=1))

    specific_plot_generator(
        metrics_arrays=[arr[1] for arr in multi_metrics_arrays],
        expected_value=expected_values["avg"],
        params=Params(
            title="Mean",
            xlabel="Iteration Number (n)",
            position=2))
    
    specific_plot_generator(
        metrics_arrays=[arr[2] for arr in multi_metrics_arrays],
        expected_value=expected_values["std"],
        params=Params(
            title="Standard Deviation",
            xlabel="Iteration Number (n)",
            position=3))
    
    specific_plot_generator(
        metrics_arrays=[arr[3] for arr in multi_metrics_arrays],
        expected_value=expected_values["var"],
        params=Params(
            title="Variance",
            xlabel="Iteration Number (n)",
            position=4))

    fig.savefig(file_out)
