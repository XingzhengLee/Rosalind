import os

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()

with open('rosalind_rna.txt', 'r') as f:
    # DNA
    DNA = f.read()
    # RNA
    RNA = DNA.replace('T', 'U')
    print(RNA)
