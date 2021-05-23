import numpy as np

n, m = map(int, input().split())
np_array = np.array([input().split() for _ in range(n)], int)
print(max(np.min(np_array, axis=1)))


"""
INPUT:
4 2
2 5
3 7
1 3
4 0
OUTPUT:
3
"""