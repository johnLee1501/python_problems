# cube = lambda x: x ** 3

"""
#Solución #1

def fibonacci(n):
    list_fibonacci = []
    if n == 0:
        return list_fibonacci
    elif n == 1:
        list_fibonacci.append(0)
        return list_fibonacci
    else:
        list_fibonacci = [0, 1]
        for x in range(n - 2):
            list_fibonacci.append(list_fibonacci[x] + list_fibonacci[x + 1])
        return list_fibonacci
"""

"""
#Solución #2

def fibonacci(n):
    lis = [0, 1]
    for i in range(n - 2):
        lis.append(lis[i] + lis[i + 1])
    return (lis[0:n])"""

cube = lambda x: x ** 3


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
