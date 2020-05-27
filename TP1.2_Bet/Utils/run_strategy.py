from Board.board import generate_board
from Utils.config_strategy import Config


def run_strategy(strategy, configs, n_gens):
    board = generate_board()
    return {
        "limited_capital": [
            strategy(configs["limited_capital"], board) for _ in range(n_gens)
        ],
        "unlimited_capital": [
            strategy(configs["unlimited_capital"], board) for _ in range(n_gens)
        ],
    }
