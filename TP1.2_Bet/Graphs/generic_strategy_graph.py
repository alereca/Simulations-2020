import matplotlib.pyplot as plt
from Graphs.subplot import general_generate_subplot
from Graphs.params import Params
from Graphs.metric_array import Metrics

red_colors = []
black_colors = []


def generate_graph(results, strategy_name):
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.5)
    fig.canvas.set_window_title(f"Roulette Bet Strategies Analysis: {strategy_name}")

    specific_plot_generator = general_generate_subplot(fig)

    specific_plot_generator(
        metrics_arrays=[
            Metrics(data=result.frequency) for result in results["limited_capital"]
        ],
        params=Params(
            title=f"Color frequency with Limited Capital",
            xlabel="Times Played",
            ylabel="Choosed color frequency",
            position=1,
        ),
    )

    specific_plot_generator(
        metrics_arrays=[
            Metrics(data=result.capital, expected_value=result.initial_capital,)
            for result in results["limited_capital"]
        ],
        params=Params(
            title="Limited Capital",
            xlabel="Times Played",
            ylabel="Amount of capital",
            position=2,
        ),
    )

    specific_plot_generator(
        metrics_arrays=[
            Metrics(data=result.frequency) for result in results["unlimited_capital"]
        ],
        params=Params(
            title="Color Frequency with Unlimited Capital",
            xlabel="Times Played",
            ylabel="Choosed color frequency",
            position=3,
        ),
    )

    specific_plot_generator(
        metrics_arrays=[
            Metrics(data=result.capital, expected_value=result.initial_capital,)
            for result in results["unlimited_capital"]
        ],
        params=Params(
            title="Unlimited Capital",
            xlabel="Times Played",
            ylabel="Amount of Capital",
            position=4,
        ),
    )
    plt.show()
