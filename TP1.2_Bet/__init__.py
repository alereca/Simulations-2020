from Strategies.martingale_strategy import martingale_strategy
from Board.board import generate_board
from Graphs.generic_strategy_graph import generate_graph
from Strategies.martingale_martin_alejandro_strategy import martingale_martin_alejandro_strategy
from Strategies.fibonnaci_strategy import fibonacci_strategy
#import seaborn as sn


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
                initial_capital=35000,
                initial_bet_amount=5,
                color="black",
            ),
        ],
        "unlimited_capital": [
            martingale_strategy(
                generate_board(),
                initial_capital=35000,
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

    results2 = {
        "limited_capital": [
            martingale_martin_alejandro_strategy(
                generate_board(),
                initial_capital=15000,
                initial_bet_amount=5,
                color="red",
            ),
            martingale_martin_alejandro_strategy(
                generate_board(),
                initial_capital=35000,
                initial_bet_amount=5,
                color="black",
            ),
        ],
        "unlimited_capital": [
            martingale_martin_alejandro_strategy(
                generate_board(),
                initial_capital=35000,
                initial_bet_amount=5,
                color="red",
                unlimited_money=True,
                max_iterations=1000,
            ),
            martingale_martin_alejandro_strategy(
                generate_board(),
                initial_capital=15000,
                initial_bet_amount=5,
                color="black",
                unlimited_money=True,
                max_iterations=1000,
            ),
        ],
    }

    results3 = {
        "limited_capital": [
            fibonacci_strategy(
                generate_board(),
                initial_capital=5000,
                initial_bet_amount=233,
                color="red",
                max_iterations=1000
            ),
            fibonacci_strategy(
                generate_board(),
                initial_capital=5000,
                initial_bet_amount=233,
                color="black",
                max_iterations=1000
            ),
        ],
        "unlimited_capital": [
           fibonacci_strategy(
                generate_board(),
                initial_capital=5000,
                initial_bet_amount=233,
                color="red",
                unlimited_money=True,
                max_iterations=1000,
            ),
            fibonacci_strategy(
                generate_board(),
                initial_capital=5000,
                initial_bet_amount=233,
                color="black",
                unlimited_money=True,
                max_iterations=1000,
            ),
        ],
    }

    #sn.set()
    generate_graph(results3,"fibonacci")