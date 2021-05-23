import numpy as np

np_array = np.array(input().split(), float)
z = int(input())
print(np.polyval(np_array, z))

"""
input:
1.1 2 3
0
output:
3.0"""
