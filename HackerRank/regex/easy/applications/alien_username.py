import re

n = int(input())
for x in range(n):
    username = input()
    match_user = re.match(r'^[_.]\d+[A-Za-z]*_?$', username)
    print('VALID') if match_user else print('INVALID')

"""
INPUT:
3
_0898989811abced_
_abce
_09090909abcD0

OUTPUT:
VALID
INVALID
INVALID
"""
