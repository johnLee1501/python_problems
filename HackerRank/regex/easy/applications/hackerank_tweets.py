import re

n = int(input())
c = 0
for _ in range(n):
    tweet = input()
    if re.search(r'hackerrank', tweet, re.I):
        c += 1
print(c)
