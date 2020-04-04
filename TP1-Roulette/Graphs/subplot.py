import numpy as np


def general_generate_subplot(figure, x_axis, n_iter):
    def specific_generate(metrics_array, expected_value, params):
        ax = figure.add_subplot(2, 2, params.position)
        ax.plot(x_axis, metrics_array)
        ax.hlines(expected_value, 0, n_iter,
                  colors="red", linestyles="dashed")
        ax.set_title(label=params.title)
        ax.set_xlabel(xlabel=params.xlabel)
        ax.set_ylabel(ylabel=params.ylabel)
    return specific_generate
