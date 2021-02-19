from itertools import product, permutations

a, b = input().split()
c = permutations(sorted(a), int(b))
print(*["".join(x) for x in c], sep='\n')
