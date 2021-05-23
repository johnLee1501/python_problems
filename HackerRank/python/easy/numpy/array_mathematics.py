import numpy as np

n, m = map(int, input().split())
np_array1 = np.array([input().split() for _ in range(n)], int)
np_array2 = np.array([input().split() for _ in range(n)], int)
print(np_array1 + np_array2, np_array1 - np_array2, np_array1 * np_array2, np_array1 // np_array2,
      np_array1 % np_array2, np_array1 ** np_array2, sep='\n')

"""
INPUT:
1 4
1 2 3 4
5 6 7 8

OUTPUT:
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
"""

"""
OTHER SOLUTION

import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
"""