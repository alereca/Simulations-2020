import numpy as np


def general_generate_subplot(figure, x_axis, n_iters):
    def specific_generate(metrics_arrays, expected_value, params):
        ax = figure.add_subplot(2, 2, params.position)
        for metrics_array in metrics_arrays:
            ax.plot(x_axis, metrics_array)
        ax.axhline(expected_value, 0, n_iters, color="red", linestyle="dashed")
        ax.set_title(label=params.title)
        ax.set_xlabel(xlabel=params.xlabel)
        ax.set_ylabel(ylabel=params.ylabel)

    return specific_generate
