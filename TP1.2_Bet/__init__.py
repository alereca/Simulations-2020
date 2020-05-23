from Strategies.martingale_strategy import martingale_strategy
from Board.board import generate_board
from Graphs.generic_strategy_graph import generate_graph
from Strategies.martingale_custom_strategy import martingale_custom_strategy
from Strategies.fibonnaci_strategy import fibonacci_strategy
from Utils.run_strategy import run_strategy
from Utils.config_strategy import Config

import seaborn as sn

if __name__ == "__main__":
    common_configs = {
        "limited_capital": [
            Config(
                initial_capital=10000,
                initial_bet_amount=120,
                color="red",
                plot_color="#ff1100",
                max_iterations=50,  # Rojo
            ),
            Config(
                initial_capital=10000,
                initial_bet_amount=1500,
                color="red",
                plot_color="#800c04",
                max_iterations=50,  # Bordo
            ),
            Config(
                initial_capital=10000,
                initial_bet_amount=300,
                color="red",
                plot_color="#f56056",
                max_iterations=50,  # Rojo claro
            ),
            Config(
                initial_capital=10000,
                initial_bet_amount=20,
                color="black",
                plot_color="#000000",
                max_iterations=50,  # Negro
            ),
            Config(
                initial_capital=10000,
                initial_bet_amount=10,
                color="black",
                plot_color="#454545",
                max_iterations=50,  # Gris oscuro
            ),
            Config(
                initial_capital=10000,
                initial_bet_amount=30,
                color="black",
                plot_color="#858585",
                max_iterations=50,  # Gris claro
            ),
        ],
        "unlimited_capital": [
            Config(
                initial_capital=100,
                initial_bet_amount=1,
                color="red",
                plot_color="#ff1100",
                max_iterations=100,
                unlimited_capital=True,
            ),
            Config(
                initial_capital=100,
                initial_bet_amount=1,
                color="red",
                plot_color="#800c04",
                max_iterations=100,
                unlimited_capital=True,
            ),
            Config(
                initial_capital=100,
                initial_bet_amount=1,
                color="red",
                plot_color="#f56056",
                max_iterations=100,
                unlimited_capital=True,
            ),
            Config(
                initial_capital=100,
                initial_bet_amount=1,
                color="black",
                plot_color="#000000",
                max_iterations=100,
                unlimited_capital=True,
            ),
            Config(
                initial_capital=100,
                initial_bet_amount=1,
                color="black",
                plot_color="#454545",
                max_iterations=100,
                unlimited_capital=True,
            ),
            Config(
                initial_capital=100,
                initial_bet_amount=1,
                color="black",
                plot_color="#858585",
                max_iterations=100,
                unlimited_capital=True,
            ),
        ],
    }

    sn.set()
    strategy = int(
        input(
            "Ingrese 1 para martingala, 2 para martingala custom o 3 para fibonacci\n"
        )
    )
    while strategy not in (1, 2, 3):
        strategy = input(
            "Ingrese 1 para martingala, 2 para martingala custom o 3 para fibonacci\n"
        )

    if strategy == 1:
        results_martingale = run_strategy(martingale_strategy, common_configs)
        generate_graph(results_martingale, "martingale")
    elif strategy == 2:
        results_martingale_custom = run_strategy(
            martingale_custom_strategy, common_configs
        )
        generate_graph(results_martingale_custom, "martingale custom")
    elif strategy == 3:
        results_fibonacci = run_strategy(fibonacci_strategy, common_configs)
        generate_graph(results_fibonacci, "fibonacci")
