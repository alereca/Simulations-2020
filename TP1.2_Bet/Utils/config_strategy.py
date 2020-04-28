from Board.board import generate_board


class Config:
    def __init__(
        self,
        initial_capital,
        initial_bet_amount,
        color,
        opacity=1,
        max_iterations=None,
    ):
        self.initial_capital = initial_capital
        self.initial_bet_amount = initial_bet_amount
        self.color = color
        self.opacity = opacity
        self.max_iterations = max_iterations
