import os
import re
from random import sample

os.chdir('D:\\Leroy\GitHub\\2021\Rosalind\\02.Bioinformatics_stronghold\\data')
os.getcwd()

from itertools import product
crossing = list(product('Aa', 'Bb', repeat=2))
[''.join(sorted(x, key=lambda x: x.lower()))) for x in crossing]

















