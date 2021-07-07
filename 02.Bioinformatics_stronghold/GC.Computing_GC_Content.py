import os

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


# find the highest GC-content
seq = fasta2dict('rosalind_gc.txt')
gc = {}
for key, value in seq.items():
    gc[key] = (value.count('G') + value.count('C')) / len(value) * 100

# print the highest GC-content
for key, value in gc.items():
    if gc[key] == max(gc.values()):
        print(key + '\n' + str(value))
