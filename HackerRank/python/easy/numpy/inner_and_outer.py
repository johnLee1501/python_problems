import numpy as np

array_a = np.array(input().split(), int)
array_b = np.array(input().split(), int)
print(np.inner(array_a, array_b))
print(np.outer(array_a, array_b))

"""
INPUT:
0 1
2 3

OUTPUT:
3
[[0 0]
 [2 3]]
"""
