from Strategies.martingale_strategy import martingale_strategy

if __name__ == "__main__":
    results = martingale_strategy(150000, 5, 7)
    print(results)
