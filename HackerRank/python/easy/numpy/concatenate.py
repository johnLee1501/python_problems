import numpy

n, m, p = map(int, input().split())
array = numpy.array([input().split() for _ in range(n + m)], int)
print(array)
"""
OTHER SOLUTION

import numpy as np
a, b, c = map(int,input().split())
arrA = np.array([input().split() for _ in range(a)],int)
arrB = np.array([input().split() for _ in range(b)],int)
print(np.concatenate((arrA, arrB), axis = 0))
"""
"""
INPUT:
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

OUTUPUT:
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
"""
