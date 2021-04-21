from itertools import product


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*product(a, b))


"""
#Otra solución
a = input().rstrip().split()
b = input().rstrip().split()
c = list(product(a, b))
print(" ".join([f'({", ".join(x)})' for x in c]))
"""