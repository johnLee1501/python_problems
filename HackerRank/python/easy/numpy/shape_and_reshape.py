import numpy as np

print(np.array(input().split(), int).reshape(3, 3))

"""import numpy

numpy_array = numpy.array(list(map(int, input().split())))
numpy_array.shape = (3, 3)
print(numpy_array)"""

"""
INPUT:
1 2 3 4 5 6 7 8 9
OUTPUT:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
