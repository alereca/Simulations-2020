import matplotlib.pyplot as plt


def graphics(all_results):
    fig, axs = plt.subplots(2,2)
    fig.canvas.set_window_title("Simulación de Ruleta: Análisis de tiradas)")
    axs[0,0].plot(all_results[0]["frequency"], color="red")
    axs[0,0].plot(all_results[1]["frequency"], color="black")
    axs[0,0].set_title("Color frequency with Limited Capital")
    plt.setp(axs[0,0], ylabel="Choosed color frequency")

    axs[0,1].plot(all_results[0]["capital"], color="red")
    axs[0,1].plot(all_results[1]["capital"], color="black")
    axs[0,1].set_title("Limited Capital")
    plt.setp(axs[1], ylabel="Amount of capital")

    axs[1, 0].plot(all_results[2]["frequency"], color="red")
    axs[1, 0].plot(all_results[3]["frequency"], color="black")
    axs[1, 0].set_title("Color Frequency with Unlimited Capital")
    plt.setp(axs[0, 0], ylabel="Choosed color frequency")

    axs[1, 1].plot(all_results[2]["capital"], color="red")
    axs[1, 1].plot(all_results[3]["capital"], color="black")
    axs[1, 1].set_title("Unlimited Capital")
    plt.setp(axs[1], ylabel="Amount of Capital")

    for ax in fig.get_axes():
        ax.grid(True)
        plt.setp(ax, xlabel="Times played")
    fig.tight_layout()

    plt.legend()
    plt.grid()
    plt.show()