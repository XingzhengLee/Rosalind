import os
import re
from random import sample

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()


def mortal_rabbits(month, death):
    rabbits = [0, 1, 1]
    for i in range(3, month + 1):
        if i <= death:
            population = rabbits[i - 1] + rabbits[i - 2]
        elif i == death + 1:
            population = rabbits[i - 1] + rabbits[i - 2] - 1
        else:
            population = rabbits[i - 1] + rabbits[i - 2] - rabbits[i - death - 1]
        rabbits.append(population)
    return rabbits[month]


month = 83
death = 16
mortal_rabbits(month, death)
