order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
s = input()
print(*sorted(s, key=order.index), sep='')

"""
INPUT:
Sorting1234

OUTPUT:
ginortS1324
"""
"""print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

import string

print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')

print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x))),
      sep='')"""

"""
REGEX SOLUTION
import re

s = input()
lowercase = re.findall(r'[a-z]', s)
uppercase = re.findall(r'[A-Z]', s)
odd_digits = re.findall(r'[13579]', s)
even_digits = re.findall(r'[02468]', s)
print(''.join(sorted(lowercase) + sorted(uppercase) + sorted(odd_digits) + sorted(even_digits)))"""
