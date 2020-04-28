from random import randint
from Utils.results import Results


def martingale_strategy(config, board):
    historic_capital_array = []
    frequency_array = []
    victories_acum = 0
    defeats_acum = 0
    iters = 0
    capital = config.initial_capital
    bet_amount = config.initial_bet_amount
    unlimited_capital = config.max_iterations is not None

    historic_capital_array.append(config.initial_capital)
    frequency_array.append(0)
    while (unlimited_capital is False and capital > bet_amount) or (
        unlimited_capital and iters < config.max_iterations - 1
    ):
        iters += 1
        board_num = board[randint(0, 36)]
        if board_num.color == config.color:
            capital += bet_amount * 2
            bet_amount = config.initial_bet_amount
            victories_acum += 1
        if board_num.color != config.color:
            capital -= bet_amount
            bet_amount = bet_amount * 2
            defeats_acum += 1
        frequency_array.append(victories_acum / (victories_acum + defeats_acum))
        historic_capital_array.append(capital)

    return Results(
        frequency=frequency_array,
        capital=historic_capital_array,
        initial_capital=config.initial_capital,
        color=config.color,
        opacity=config.opacity,
    )
