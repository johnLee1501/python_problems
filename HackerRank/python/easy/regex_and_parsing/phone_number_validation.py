import re
# pattern = r'^[789][0-9]{9}$'
pattern = r'^[789]\d{9}$'
n = int(input())
for _ in range(n):
    if re.match(pattern, input()):
        print('YES')
    else:
        print('NO')

"""import re

n = int(input())
pattern = re.compile(r'^[7-9]\d{9}$')
numbers = [input() for _ in range(n)]

for number in numbers:
    if pattern.match(number):
        print('YES')
    else:
        print('NO')"""