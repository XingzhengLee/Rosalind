import os
import re
import math
from random import sample

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()


# no matter what genotype the organism that mates with someone of genotype Aa Bb has, the probability that the
# offspring is Aa Bb is always 0.25
def prob4k(k, n):
    population = 2 ** k
    prob_sum = 0
    for i in range(n, population + 1):
        prob = math.factorial(population) / (
                math.factorial(i) * math.factorial(population - i)) * 0.25 ** i * 0.75 ** (population - i)
        prob_sum += prob
    return prob_sum


prob4k(5, 7)
