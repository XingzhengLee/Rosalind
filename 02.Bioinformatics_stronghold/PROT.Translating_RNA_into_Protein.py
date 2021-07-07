import os
import re

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()

lst = []
with open('RNA_codon_table.txt', 'r') as f:
    for index, line in enumerate(f):
        lst_tmp = re.split('\s{2,}', line.strip())
        lst += lst_tmp

RNA_codon_table = {}
for i in lst:
    element = i.split()
    key = element[0]
    value = element[1]
    RNA_codon_table[key] = value

with open('rosalind_prot.txt', 'r') as f:
    RNA = f.read()
    protein = ''
    i = 0
    while i + 3 <= len(RNA):
        codon = RNA[i:(i + 3)]
        peptide = RNA_codon_table[codon]
        if peptide == 'Stop':
            break
        else:
            protein += peptide
        i += 3
print(protein)
