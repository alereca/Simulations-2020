import numpy
from random import randint
from Utils.results import Results


def fib(nterms=100, fb_list=[]):
    n1 = 1
    n2 = 1
    fb_list.append(n1)
    fb_list.append(n2)
    for i in range(nterms):
        nth = n1 + n2
        n1 = n2
        n2 = nth
        fb_list.append(nth)
    return fb_list


def fibonacci_strategy(config, board):
    historic_capital_array = []
    frequency_array = []
    victories_acum = 0
    defeats_acum = 0
    iters = 0
    capital = config.initial_capital
    bet_amount = config.initial_bet_amount
    unlimited_capital = config.max_iterations is not None

    fibonacci_list = fib()

    if config.initial_bet_amount in fibonacci_list:
        fb_index = fibonacci_list.index(config.initial_bet_amount)
        while (unlimited_capital is False and capital > bet_amount) or (
            unlimited_capital and iters < config.max_iterations
        ):
            historic_capital_array.append(capital)
            board_num = board[randint(0, 36)]
            if board_num.color == config.color:
                capital += bet_amount * 2
                fb_index -= 2
                if fb_index < 0:
                    fb_index = 0
                bet_amount = fibonacci_list[fb_index]
                victories_acum += 1
            if board_num.color != config.color:
                fb_index += 1
                capital -= bet_amount
                bet_amount = fibonacci_list[fb_index]
                defeats_acum += 1
            frequency_array.append(victories_acum / (victories_acum + defeats_acum))
            iters += 1

    return Results(
        frequency=frequency_array,
        capital=historic_capital_array,
        initial_capital=config.initial_capital,
        color=config.color,
        opacity=config.opacity,
    )
