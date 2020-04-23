from random import randint


def martingale_strategy(capital, bet_amount, bet_number):
    historic_capital_array = []
    frequency_array = []
    victories_acum = 0
    defeats_acum = 0

    while capital > bet_amount:
        random_roulette_number = randint(0, 36)
        if random_roulette_number == bet_number:
            capital += bet_amount * 36
            victories_acum += 1
        if random_roulette_number != bet_number:
            capital -= bet_amount
            bet_amount += bet_amount * 2
            defeats_acum += 1
        historic_capital_array.append(capital)
        frequency_array.append(
            victories_acum / (victories_acum + defeats_acum)
        )

    return {"frequency": frequency_array, "capital": historic_capital_array}
