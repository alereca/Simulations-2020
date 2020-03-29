import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_graph(rf_list, n_iter, num, expected_rf):
    x = np.arange(1, n_iter)
    y = np.array(rf_list)

    plt.plot(x, y)
    plt.hlines(expected_rf, 1, n_iter, colors="red", linestyles="dashed")

    plt.title = "probability law test"
    plt.xlabel = "iterations(n)"
    plt.ylabel = f"relative frequency of number {num}(rf)"
    
    plt.savefig("rf_roulette.jpg")
    
