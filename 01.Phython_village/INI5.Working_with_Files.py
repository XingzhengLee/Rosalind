import os
os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\01.Phython_village')
os.getcwd()

with open('rosalind_ini5.txt', 'r') as f:
    for (num, value) in enumerate(f):
        num_r = num + 1
        content = value.strip()
        if num_r % 2 == 0:
            print(content)
