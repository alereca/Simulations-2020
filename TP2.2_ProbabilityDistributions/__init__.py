from Distributions.exponential import test_exponential
from Distributions.pascal import test_pascal

if __name__ == "__main__":
    length = 1000

    test_exponential(length, lmda=35)
    test_pascal(length, k=50, q=0.40)
