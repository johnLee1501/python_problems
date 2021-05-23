import numpy as np

n = int(input())
np_array = np.array([input().split() for _ in range(n)], float)
print(round(np.linalg.det(np_array), 2))

"""
INPUT:
2
1.1 1.1
1.1 1.1

OUTPUT:
0.0
"""
