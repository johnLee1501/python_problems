from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(F)) / len(C)))

"""from functools import reduce
n, letters, n_selected = int(input()), input().split(), int(input())
m = ''.join(letters).count('a')
print(1.0 - reduce(lambda x, y: x * y, [(1.0 - m * 1.0 / (n - i)) for i in range(n_selected)]))"""
"""
from itertools import combinations

n, letters, n_selected = int(input()), input().split(), int(input())
combinations_letters = list(combinations(letters, n_selected))
n_occurrence = sum([True if 'a' in combination_letter else False for combination_letter in combinations_letters])
print(round(n_occurrence / len(combinations_letters), 4))"""

"""
INPUT:
4 
a a c d
2

OUTPUT:
0.8333
"""
