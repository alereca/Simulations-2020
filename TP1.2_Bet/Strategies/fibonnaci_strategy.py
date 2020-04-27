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


def fibonacci_strategy(
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

    fibonacci_list = fib()

    if initial_bet_amount in fibonacci_list:
        fb_index = fibonacci_list.index(initial_bet_amount)
        while (
            unlimited_money is False and capital > bet_amount and iters < max_iterations
        ) or (unlimited_money and iters < max_iterations):
            random_roulette_number = randint(0, 36)
            if board[random_roulette_number].color == color:
                capital += bet_amount * 2
                fb_index += 1
                bet_amount = fibonacci_list[fb_index]
                victories_acum += 1
            if board[random_roulette_number].color != color:
                fb_index -= 2
                if fb_index < 0:
                    fb_index = 0
                capital -= bet_amount
                bet_amount = fibonacci_list[fb_index]
                defeats_acum += 1

            historic_capital_array.append(capital)
            frequency_array.append(victories_acum / (victories_acum + defeats_acum))
            iters += 1

    return Results(
        frequency=frequency_array,
        capital=historic_capital_array,
        initial_capital=initial_capital,
        color=color,
    )
