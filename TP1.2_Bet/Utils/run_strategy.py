from Board.board import generate_board


def run_strategy(strategy, configs):
    return {
        "limited_capital": [
            strategy(
                generate_board(),
                initial_capital=config.initial_capital,
                initial_bet_amount=config.initial_bet_amount,
                color=config.color,
            )
            for config in filter(lambda c: not (c.max_iterations), configs)
        ],
        "unlimited_capital": [
            strategy(
                generate_board(),
                initial_capital=config.initial_capital,
                initial_bet_amount=config.initial_bet_amount,
                color=config.color,
                unlimited_money=True,
                max_iterations=config.max_iterations,
            )
            for config in filter(lambda c: c.max_iterations, configs)
        ],
    }
