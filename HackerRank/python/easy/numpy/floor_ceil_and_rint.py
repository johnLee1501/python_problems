import numpy

numpy.set_printoptions(sign=' ')

a = numpy.array(input().split(), float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


"""
INPUT:
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

OUTPUT:
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""