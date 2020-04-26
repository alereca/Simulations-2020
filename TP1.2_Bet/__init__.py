from Strategies.martingale_strategy import martingale_strategy
from Board.board import generate_board
from Graphics.generic_strategy_graphic import generate_graphic


if __name__ == "__main__":
    results = {
        "limited_capital": [
            martingale_strategy(
                generate_board(),
                initial_capital=15000,
                initial_bet_amount=5,
                color="red",
            ),
            martingale_strategy(
                generate_board(),
                initial_capital=15000,
                initial_bet_amount=5,
                color="black",
            ),
        ],
        "unlimited_capital": [
            martingale_strategy(
                generate_board(),
                initial_capital=15000,
                initial_bet_amount=5,
                color="red",
                unlimited_money=True,
                max_iterations=1000,
            ),
            martingale_strategy(
                generate_board(),
                initial_capital=15000,
                initial_bet_amount=5,
                color="black",
                unlimited_money=True,
                max_iterations=1000,
            ),
        ],
    }

    generate_graphic(results)
