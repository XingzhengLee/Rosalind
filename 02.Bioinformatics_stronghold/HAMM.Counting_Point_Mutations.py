import os

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()

with open('rosalind_hamm.txt', 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()
    dist = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            dist += 1
print(dist)
