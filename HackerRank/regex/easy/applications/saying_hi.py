import re

n = int(input())
for _ in range(n):
    phrase = input()
    if re.search(r'^hi\s[^d]', phrase, re.I):
        print(phrase)
