import numpy

n, m = map(int, input().split())
matriz = []
[matriz.append(input().split()) for _ in range(n)]
numpy_array = numpy.array(matriz, int)
print(numpy.transpose(numpy_array))
print(numpy_array.flatten())


"""INPUT:
2 2
1 2
3 4

OUTPUT:
[[1 3]
 [2 4]]
[1 2 3 4]
"""

"""OTHER SOLUTIONS AND ANOTATIONS
# Shortcut to create Transpose:

arr=numpy.array([[1,2,3],[4,5,6]])
print(arr.T)

n, m = map(int, input().split())
array = numpy.array([input().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())
"""