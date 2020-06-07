from Distributions.exponential import test_exponential
from Distributions.pascal import test_pascal

if __name__ == "__main__":
    lenght = 1000

    test_exponential(lenght, lmda=1)
    test_pascal(lenght, k=24, q=0.12)
