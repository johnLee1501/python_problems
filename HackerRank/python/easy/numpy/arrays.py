import numpy


def arrays(arr):
    numpy_array = numpy.array(arr, float)
    numpy_array_reversed = numpy.flip(numpy_array)
    return numpy_array_reversed


arr = input().strip().split(' ')
result = arrays(arr)
print(result)


"""
OTHER SOLUTIONS
def arrays(arr):
   #revrser array first, convert to float array with numpy
   return(numpy.array(arr[::-1], float))
"""

"""
INPUT:
1 2 3 4 -8 -10
OUTPUT:
[-10.  -8.   4.   3.   2.   1.]
"""