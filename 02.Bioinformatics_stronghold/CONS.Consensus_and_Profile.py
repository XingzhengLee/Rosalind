import os
import re
from random import sample

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()


# function: fasta2dict
def fasta2dict(file_name):
    with open(file_name, 'r') as f:
        dict = {}
        for num, value in enumerate(f):
            line = value.strip()
            if line.startswith('>'):
                name = line[1:]
                dict[name] = ''
            else:
                dict[name] += line
        return dict


# example sequence
fasta = fasta2dict('rosalind_cons.txt')
seq_example = fasta[(sample(list(fasta.keys()), 1))[0]]

# create empty list
dict = {'A': [], 'C': [], 'G': [], 'T': [], 'S': []}
for i in range(len(seq_example)):
    dict['A'] += [0]
    dict['C'] += [0]
    dict['G'] += [0]
    dict['T'] += [0]
    dict['S'] += ['']

# sequence in vertical

for key, value in fasta.items():
    for i in range(len(value)):
        dict['S'][i] += value[i]

# count
for i in range(len(dict['S'])):
    dict['A'][i] = dict['S'][i].count('A')
    dict['C'][i] = dict['S'][i].count('C')
    dict['G'][i] = dict['S'][i].count('G')
    dict['T'][i] = dict['S'][i].count('T')

# representative sequence
test = {}
for i in range(len(dict['S'])):
    test['A'] = dict['A'][i]
    test['C'] = dict['C'][i]
    test['G'] = dict['G'][i]
    test['T'] = dict['T'][i]
    print(max(test, key=test.get), end='')
print('\r')

dict.pop('S')
for key, value in dict.items():
    print(key + ': ', end='')
    for i in range(len(dict[key])):
        print(dict[key][i], end=' ')
    print('\r')
