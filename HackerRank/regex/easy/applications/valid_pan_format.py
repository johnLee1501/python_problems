import re

n = int(input())
for _ in range(n):
    identification = input()
    if re.match(r'^[A-Z]{5}\d{4}[A-Z]$', identification):
        print('YES')
    else:
        print('NO')

"""
INPUT:
3
ABCDS1234Y
ABAB12345Y
avCDS1234Y

OUTPUT:
YES
NO
NO
"""
