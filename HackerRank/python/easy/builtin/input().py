x, k = map(int, input().split())
polynomial = input()
print(eval(polynomial) == k)

"""x, k = map(int, input().split())
polynomial = input()
polynomial = polynomial.replace('x', f'{x}')
if eval(polynomial) == k:
    print(True)
else:
    print(False)
"""
"""
INPUT:
1 4
x**3 + x**2 + x + 1

OUTPUT:
True
"""
