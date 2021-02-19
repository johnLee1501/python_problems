from itertools import combinations

a, b = input().split()
a = sorted(a)
b = int(b)
for x in range(1, b + 1):
    c = combinations(a, x)
    print(*["".join(x) for x in c], sep='\n')
