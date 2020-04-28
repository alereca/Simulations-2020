from Strategies.martingale_strategy import martingale_strategy
from Board.board import generate_board
from Graphs.generic_strategy_graph import generate_graph
from Strategies.martingale_custom_strategy import (
    martingale_custom_strategy,
)
from Strategies.fibonnaci_strategy import fibonacci_strategy
from Utils.run_strategy import run_strategy
from Utils.config_strategy import Config

# import seaborn as sn

if __name__ == "__main__":
    common_configs = [
        Config(initial_capital=1500, initial_bet_amount=5, color="red"),
        Config(initial_capital=1500, initial_bet_amount=5, color="black"),
        Config(
            initial_capital=1500,
            initial_bet_amount=5,
            color="red",
            max_iterations=1000,
        ),
        Config(
            initial_capital=1500,
            initial_bet_amount=5,
            color="black",
            max_iterations=1000,
        ),
    ]

    results_martingale = run_strategy(martingale_strategy, common_configs)

    results_martingale_custom = run_strategy(
        martingale_custom_strategy, common_configs
    )

    results_fibonacci = run_strategy(
        fibonacci_strategy, common_configs
    )

    # sn.set()
    generate_graph(results_martingale, "martingale")
    #generate_graph(results_martingale_custom, "martingale custom")
    #generate_graph(results_fibonacci, "fibonacci")
