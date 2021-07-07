import os

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()


def rabbit(month, production):
    if month <= 2:
        return 1
    else:
        return production * rabbit(month - 2, production) + rabbit(month - 1, production)


n = 30
k = 2
rabbit(n, k)
