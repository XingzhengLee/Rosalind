import os
os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\01.Phython_village')
os.getcwd()

with open('rosalind_ini6.txt', 'r') as f:
    lst = f.read().split()
    dict = {}
    for word in lst:
        dict[word] = dict.get(word, 0) + 1
    for key, value in dict.items():
        print(key, value)
