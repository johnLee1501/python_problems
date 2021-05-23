import numpy as np

n, m = map(int, input().split())
np_array = np.array([input().split() for _ in range(n)], int)
print(np.prod(np.sum(np_array, axis=0)))

"""
INPUT:
2 2
1 2
3 4

OUTPUT:
24"""
