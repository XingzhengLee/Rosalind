import os
import re
from random import sample

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()


# function: fasta2dict
def fasta2dict(file_name):
    with open(file_name, 'r') as f:
        dict = {}
        for index, line in enumerate(f):
            if line.startswith('>'):
                name = line.strip()[1:]
                dict[name] = ''
            else:
                dict[name] += line.strip()
        return dict


fasta = fasta2dict('rosalind_grph.txt')

for key, value in fasta.items():
    fasta[key] = [value, value[:3], value[-3:]]

with open('out.txt', 'w') as f:
    for key1, value1 in fasta.items():
        for key2, value2 in fasta.items():
            if key1 == key2:
                continue
            elif value1[2] == value2[1]:
                print(key1, key2, file=f)
                print(key1, key2)
