

from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


d = OrderedCounter(input() for _ in range(int(input())))

print(len(d))
print(*d.values())

"""words = OrderedDict()
n = int(input())
for _ in range(n):
    word = input()
    words[word] = 1 + words.get(word, 0)
print(len(words))

for key in words.items():
    print(key[1], end=' ')
"""
