from Board.board import generate_board
from Utils.config_strategy import Config


def run_strategy(strategy, configs):
    board = generate_board()
    return {
        "limited_capital": [
            strategy(config, board) for config in configs["limited_capital"]
        ],
        "unlimited_capital": [
            strategy(config, board) for config in configs["unlimited_capital"]
        ],
    }
