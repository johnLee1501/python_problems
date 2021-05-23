import numpy as np

n, m = map(int, input().split())
np_array = np.array([input().split() for _ in range(n)], int)
print(np.mean(np_array, axis=1))
print(np.var(np_array, axis=0))
print(round(np.std(np_array), 11))

"""INPUT:
2 2
1 2
3 4

OUTPUT:
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
"""
