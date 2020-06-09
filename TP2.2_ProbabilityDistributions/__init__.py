from Distributions.exponential import test_exponential
from Distributions.pascal import test_pascal
from Distributions.normal import test_normal
from Distributions.poisson import test_poisson
from Distributions.uniform import test_uniform
from Distributions.gamma import test_gamma
from Distributions.binomial import test_binomial


if __name__ == "__main__":
    length = 1000

    test_exponential(length, lmda=4)
    test_pascal(length, k=50, q=0.40)
    test_normal(length, mean=20, std=2)
    test_poisson(length, lmda=1)
    test_uniform(length, a=1, b=2)
    test_gamma(length, lmda=1, k=5)
    test_binomial(length, p=0.7, n=1000)
