from itertools import combinations_with_replacement

a, b = input().split()
c = combinations_with_replacement(sorted(a), int(b))
print(*["".join(x) for x in c], sep='\n')
