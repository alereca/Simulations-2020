from random import randint
from Board.board import generate_board


def martingale_strategy(
    board,
    initial_capital,
    initial_bet_amount,
    color,
    unlimited_money=False,
    max_iterations=None,
):
    historic_capital_array = []
    frequency_array = []
    victories_acum = 0
    defeats_acum = 0
    iters = 0
    capital = initial_capital
    bet_amount = initial_bet_amount

    while (unlimited_money is False and capital > bet_amount) or (
        unlimited_money and iters < max_iterations
    ):
        iters += 1
        random_roulette_number = randint(0, 36)
        if board[random_roulette_number].color == color:
            capital += bet_amount
            bet_amount = initial_bet_amount
            victories_acum += 1
        if random_roulette_number != color:
            capital -= bet_amount
            bet_amount += bet_amount * 2
            defeats_acum += 1
        historic_capital_array.append(capital)
        frequency_array.append(victories_acum / (victories_acum + defeats_acum))

    return {
        "frequency": frequency_array,
        "capital": historic_capital_array,
        "initial_capital": initial_capital,
        "color": color,
    }
