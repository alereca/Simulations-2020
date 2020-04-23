from Strategies.martingale_strategy import martingale_strategy
from Board.board import generate_board

if __name__ == "__main__":
    results = martingale_strategy(generate_board(), 150000, 5, "red")
    print(results)
