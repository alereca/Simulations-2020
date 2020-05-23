from Board.board import generate_board


class Config:
    def __init__(
        self,
        initial_capital,
        initial_bet_amount,
        color,
        plot_color=None,
        max_iterations=None,
        unlimited_capital=False,
    ):
        self.initial_capital = initial_capital
        self.initial_bet_amount = initial_bet_amount
        self.color = color
        self.plot_color = plot_color
        self.max_iterations = max_iterations
        self.unlimited_capital = unlimited_capital
