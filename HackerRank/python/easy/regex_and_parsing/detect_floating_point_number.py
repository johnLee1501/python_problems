import re

pattern = r'^[+-]?[\d]*\.[\d]+$'
n = int(input())
for _ in range(n):
    if re.match(pattern, input()):
        print('True')
    else:
        print('False')
