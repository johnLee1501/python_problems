import numpy

n, m = map(int, input().split())
print(str(numpy.eye(n, m)).replace('1', ' 1').replace('0', ' 0'))

"""
INPUT:
3 3
OUTPUT:
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
 
 You need to add a space before one's and zero's
"""