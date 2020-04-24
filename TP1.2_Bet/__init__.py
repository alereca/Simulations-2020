from Strategies.martingale_strategy import obtain_results
from Graphics.martingale_strategy_graphic import graphics
import seaborn as sns

if __name__ == "__main__":
    m_s_results = obtain_results()
    sns.set()
    graphics(m_s_results)
