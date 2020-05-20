from random import randint
from Utils.results import Results


def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


def martingale_custom_strategy(config, board):
    historic_capital_array = []
    frequency_array = []
    victories_acum = 0
    defeats_acum = 0
    iters = 0
    bet_amount_array = []
    capital = config.initial_capital
    bet_amount = config.initial_bet_amount
    unlimited_capital = config.unlimited_capital

    bet_amount_array.append(config.initial_bet_amount)
    frequency_array.append(0)
    while (unlimited_capital is False and capital > bet_amount and iters < config.max_iterations - 1) or (
        unlimited_capital and iters < config.max_iterations
    ):
        historic_capital_array.append(capital)
        if capital < bet_amount and not unlimited_capital:
            bet_amount = closest(bet_amount_array, capital)
        board_num = board[randint(0, 36)]
        if board_num.color == config.color:
            capital += bet_amount * 2
            victories_acum += 1
        if board_num.color != config.color:
            capital -= bet_amount
            bet_amount = bet_amount * 2
            defeats_acum += 1

        frequency_array.append(victories_acum / (victories_acum + defeats_acum))
        iters += 1

    return Results(
        frequency=frequency_array,
        capital=historic_capital_array,
        initial_capital=config.initial_capital,
        color=config.color,
        plot_color=config.plot_color,
    )
