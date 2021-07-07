import os

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()

# AA
k = 18
# Aa
m = 22
# aa
n = 29

p = k + m + n
# calculate the probability of aa
# Aa * Aa (1/4)
recessive1 = m * (m - 1) / (p * (p - 1) * 4)
# Aa * aa (1/2)
recessive2 = m * n / (p * (p - 1) * 2) * 2
# aa * aa (1)
recessive3 = n * (n - 1) / (p * (p - 1))

1 - (recessive1 + recessive2 + recessive3)
