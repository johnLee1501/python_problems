from itertools import groupby

s = input()
result = []
for k, g in groupby(s):
    result.append(f'({len(list(g))}, {k})')
print(*result, sep=' ')

"""
INPUT:
1222311

OUTPUT:
(1, 1) (3, 2) (1, 3) (2, 1)
"""

"""
OTHER SOLUTIONS

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
"""