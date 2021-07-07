import os

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()

with open('rosalind_dna.txt', 'r') as f:
    # DNA
    DNA = f.read()
    # count
    print(DNA.count('A'), DNA.count('C'), DNA.count('G'), DNA.count('T'))
