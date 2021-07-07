import os

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()

with open('rosalind_revc.txt', 'r') as f:
    # DNA
    DNA = f.read()
    # complement
    trans = DNA.maketrans('ATCG', 'TAGC')
    complement = DNA.translate(trans)
    # reverse
    reverse = complement[::-1]
    print(reverse)
