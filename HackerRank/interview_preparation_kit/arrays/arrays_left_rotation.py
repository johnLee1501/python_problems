from collections import deque


def rotLeft(a, d):
    x = deque(a)
    x.rotate(len(a) - d)
    return x

"""
def array_left_rotation(a, n, k):
    alist = list(a)
    b = alist[k:] + alist[:k]
    return b
"""

"""
def left_shift(n,k,a):
   for _ in range(k):
      a.append(a.pop(0))
   print(*a)
"""
if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    print(' '.join(map(str, result)))
