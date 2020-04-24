from random import randint
from Board.board import generate_board


def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


def obtain_results():
    red_result_limited_money = m_s_limited_money(generate_board(), 1000, 5, "red")
    black_result_limited_money = m_s_limited_money(generate_board(), 1000, 5, "black")
    red_result_unlimited_money = m_s_unlimited_money(generate_board(), 10000, 5, "red")
    black_result_unlimited_money = m_s_unlimited_money(generate_board(), 10000, 5, "black")
    return append_results(red_result_limited_money, black_result_limited_money, red_result_unlimited_money,
                          black_result_unlimited_money)


def append_results(result1, result2, result3, result4):
    results = []
    results.append(result1)
    results.append(result2)
    results.append(result3)
    results.append(result4)
    return results


def m_s_limited_money(board, capital, bet_amount, selected_color):  # m_s_limited_money == martingale_strategy
    historic_capital_array = []
    frequency_array = []
    bet_amount_array = []
    victories_acum = 0
    defeats_acum = 0
    cont = 0

    while capital > 0:
        random_roulette_number = randint(0, 36)
        num_color = board[random_roulette_number].color
        if num_color == selected_color:
            capital += bet_amount * 2
            victories_acum += 1
        if num_color != selected_color:
            capital -= bet_amount
            bet_amount += bet_amount * 2
            defeats_acum += 1
        bet_amount_array.append(bet_amount)
        if capital > 0:
            historic_capital_array.append(capital)
        else:
            historic_capital_array.append(0)
        frequency_array.append(victories_acum / (victories_acum + defeats_acum))
        if capital < bet_amount:
            bet_amount = closest(bet_amount_array, capital)
        cont += 1

    return {"frequency": frequency_array, "capital": historic_capital_array}


def m_s_unlimited_money(board, played_times, bet_amount, selected_color):  # m_s_limited_money == martingale_strategy
    historic_capital_array = []
    frequency_array = []
    bet_amount_array = []
    victories_acum = 0
    defeats_acum = 0
    cont = 0
    capital = 1000000

    while cont != played_times:
        random_roulette_number = randint(0, 36)
        num_color = board[random_roulette_number].color
        if num_color == selected_color:
            capital += bet_amount * 2
            victories_acum += 1
        if num_color != selected_color:
            capital -= bet_amount
            bet_amount += bet_amount * 2
            defeats_acum += 1
        bet_amount_array.append(bet_amount)
        if capital > 0:
            historic_capital_array.append(capital)
        else:
            historic_capital_array.append(0)
        frequency_array.append(victories_acum / (victories_acum + defeats_acum))
        if capital < bet_amount:
            bet_amount = closest(bet_amount_array, capital)
        cont += 1

    return {"frequency": frequency_array, "capital": historic_capital_array}
