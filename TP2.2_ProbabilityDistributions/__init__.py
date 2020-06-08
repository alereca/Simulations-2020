from Distributions.exponential import test_exponential
from Distributions.pascal import test_pascal
from Distributions.normal import test_normal
from Distributions.poisson import test_poisson

if __name__ == "__main__":
    length = 1000

    test_exponential(length, lmda=4)
    test_pascal(length, k=50, q=0.40)
    test_normal(length, mean=20, std=2)
    test_poisson(length, lmda=1)
