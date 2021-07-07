import os
import re

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()


def find_all(str, sub):
    index_lst = []
    index = str.find(sub)
    while index != -1:
        index_lst.append(index)
        index = str.find(sub, index + 1)
    return index_lst


with open('rosalind_subs.txt', 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()
index_lst = find_all(s, t)

with open('out.txt', 'w') as f:
    for index in index_lst:
        # f.write(str(index) + ' ')
        print(index + 1, end=' ', file=f)

# alternative
with open('out.txt', 'w') as f:
    position = ''
    for index in index_lst:
        position += str(index + 1) + ' '
position.strip()
