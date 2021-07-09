import re
from collections import Counter
from os import strerror

name_file = 'letras.txt'
archivo = open(f'./{name_file}', encoding='utf-8').read().lower()
archivo = re.sub(r'[^A-Za-z]', '', archivo)
count_letters = Counter(archivo)
count_sorted = sorted(count_letters.items(), key=lambda x: (-x[1], x[0]))

try:
    hist = open(f'{name_file}.hist', 'wt')
    for x in count_sorted:
        hist.write(f'{x[0]} --> {x[1]}\n')
    hist.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
