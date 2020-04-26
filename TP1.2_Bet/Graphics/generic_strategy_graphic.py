import matplotlib.pyplot as plt
from Graphics.subplot import general_generate_subplot
from Graphics.params import Params


def generate_graphic(results):
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.5)
    fig.canvas.set_window_title("Simulación de Ruleta: Análisis de tiradas)")

    specific_plot_generator = general_generate_subplot(fig)

    specific_plot_generator(
        metrics_arrays=[result["frequency"] for result in results["limited_capital"]],
        expected_values=[],
        params=Params(
            title="Color frequency with Limited Capital",
            xlabel="Times Played",
            ylabel="Choosed color frequency",
            position=1,
        ),
    )

    specific_plot_generator(
        metrics_arrays=[result["capital"] for result in results["limited_capital"]],
        expected_values=[
            result["initial_capital"] for result in results["limited_capital"]
        ],
        params=Params(
            title="Limited Capital",
            xlabel="Times Played",
            ylabel="Amount of capital",
            position=2,
        ),
    )

    specific_plot_generator(
        metrics_arrays=[result["frequency"] for result in results["unlimited_capital"]],
        expected_values=[],
        params=Params(
            title="Color Frequency with Unlimited Capital",
            xlabel="Times Played",
            ylabel="Choosed color frequency",
            position=3,
        ),
    )

    specific_plot_generator(
        metrics_arrays=[result["capital"] for result in results["unlimited_capital"]],
        expected_values=[
            result["initial_capital"] for result in results["unlimited_capital"]
        ],
        params=Params(
            title="Unlimited Capital",
            xlabel="Times Played",
            ylabel="Amount of Capital",
            position=4,
        ),
    )
    plt.show()
