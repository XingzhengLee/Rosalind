import os
import re
from random import sample

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()

couple = [16700, 16775, 16329, 17143, 16531, 19274]

# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa

(couple[0] + couple[1] + couple[2] + 0.75 * couple[3] + 0.5 * couple[4]) * 2









