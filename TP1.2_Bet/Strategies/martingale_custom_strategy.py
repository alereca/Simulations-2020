from random import randint
from Utils.results import Results

def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


def martingale_custom_strategy(
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
    bet_amount_array = []
    capital = initial_capital
    bet_amount = initial_bet_amount

    bet_amount_array.append(initial_bet_amount)

    while (unlimited_money is False and capital > bet_amount) or (
        unlimited_money and iters < max_iterations
    ):
        random_roulette_number = randint(0, 36)
        historic_capital_array.append(capital)
        if capital < bet_amount:
            bet_amount = closest(bet_amount_array, capital)
        if board[random_roulette_number].color == color:
            capital += bet_amount * 2
            victories_acum += 1
        if board[random_roulette_number].color != color:
            capital -= bet_amount
            bet_amount = bet_amount * 2
            defeats_acum += 1

        frequency_array.append(victories_acum / (victories_acum + defeats_acum))
        iters += 1

    return Results(
        frequency=frequency_array,
        capital=historic_capital_array,
        initial_capital=initial_capital,
        color=color,
    )
