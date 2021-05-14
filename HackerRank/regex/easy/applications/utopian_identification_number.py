import re

n = int(input())
for _ in range(n):
    identification = input()
    if re.match(r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$', identification):
        print('VALID')
    else:
        print('INVALID')


"""
INPUT: 
2
abc012333ABCDEEEE
0123AB

OUTPUT:
VALID
INVALID
"""