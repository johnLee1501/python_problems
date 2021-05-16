import re

sentences = '\n'.join([input() for _ in range(int(input()))])
for _ in range(int(input())):
    word = input()
    print(len(re.findall(r'\b%s\b' % word, sentences)))
