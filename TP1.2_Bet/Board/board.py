from Board.roulette_number import BoardNumber


def asignColor(i):
    if i % 2 == 0:
        return "red"
    if i % 2 != 0:
        return "black"


def generate_board():
    return [BoardNumber(0, None)] + [BoardNumber(i, asignColor(i)) for i in range(1, 37)]
