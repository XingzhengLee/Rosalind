import os
import re
from random import sample

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()


# function: get_kmer
def get_kmer(seq, n):
    i = 0
    kmer = []
    while i + n <= len(seq):
        kmer.append(seq[i:(i + n)])
        i += 1
    return kmer


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


fasta = fasta2dict('rosalind_lcsm.txt')
for key, value in fasta.items():
    fasta[key] = [value, len(value)]
    min = float('inf')
    if fasta[key][1] < min:
        min = fasta[key][1]
        seq_min = fasta[key][0]

for i in reversed(range(1, len(seq_min))):
    kmer_lst = get_kmer(seq_min, i + 1)
    for kmer in kmer_lst:
        count = 0
        for key, value in fasta.items():
            seq = value[0]
            if seq.find(kmer) != -1:
                count += 1
        if count == len(fasta):
            print(kmer)
            # break
