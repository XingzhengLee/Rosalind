import os
import re
import math
import urllib.request
from random import sample

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()


# function: fasta2dict
def fasta_page2dict(page_decode):
    dict = {}
    for index, line in enumerate(page_decode.split(sep='\n')):
        if line.startswith('>'):
            name = line.strip()[1:]
            dict[name] = ''
        else:
            dict[name] += line.strip()
    return dict


# finding protein motifs
with open('rosalind_mprt.txt', 'r') as f:
    for index, line in enumerate(f):
        # obtain protein name
        protein = line.strip()
        # request protein database
        req = urllib.request.Request('http://www.uniprot.org/uniprot/' + protein + '.fasta')
        response = urllib.request.urlopen(req)
        page = response.read()
        page_decode = page.decode()
        # fasta (in page) to dict type
        fasta = fasta_page2dict(page_decode)
        seq = list(fasta.values())[0]
        # regular expression pattern
        pattern = re.compile(r'N(?=[^P][ST][^P])')
        location = []
        # location list
        for i in re.finditer(pattern, seq):
            location.append(str(i.span()[0] + 1))
        # print results
        if location != []:
            with open('out.txt', 'a') as f:
                print(protein)
                print(protein, file=f)
                print(' '.join(location))
                print(' '.join(location), file=f)
