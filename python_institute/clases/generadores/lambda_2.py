def imprimirfuncion(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')


def poli(x):
    return 2 * x ** 2 - 4 * x + 2


imprimirfuncion([x for x in range(-2, 3)], poli)

imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)

lista1 = [x for x in range(5)]
lista2 = list(map(lambda x: 2 ** x, lista1))
print(lista2)
for x in map(lambda x: x * x, lista2):
    print(x, end=' ')
print()

print(list(map(lambda x: 2 * x ** 2 - 4 * x + 2, [x for x in range(-2, 3)])))
