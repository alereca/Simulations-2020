from random import randint
from Utils.results import Results


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

    historic_capital_array.append(initial_capital)
    frequency_array.append(0)
    while (unlimited_money is False and capital > bet_amount) or (
        unlimited_money and iters < max_iterations - 1
    ):
        iters += 1
        random_roulette_number = randint(0, 36)
        if board[random_roulette_number].color == color:
            capital += bet_amount * 2
            bet_amount = initial_bet_amount
            victories_acum += 1
        if board[random_roulette_number].color != color:
            capital -= bet_amount
            bet_amount = bet_amount * 2
            defeats_acum += 1
        frequency_array.append(victories_acum / (victories_acum + defeats_acum))
        historic_capital_array.append(capital)

    lasts = historic_capital_array[-6: len(historic_capital_array)]

    return Results(
        frequency=frequency_array,
        capital=historic_capital_array,
        initial_capital=initial_capital,
        color=color,
    )
