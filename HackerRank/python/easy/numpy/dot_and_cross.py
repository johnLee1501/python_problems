import numpy as np

n = int(input())
array_a = np.array([input().split() for _ in range(n)], int)
array_b = np.array([input().split() for _ in range(n)], int)
print(np.dot(array_a, array_b))


"""
INPUT:
2
1 2
3 4
1 2
3 4

OUTPUT:
[[ 7 10]
 [15 22]]"""