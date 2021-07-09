class SuperUno:
    pass


class SuperDos:
    pass


class Sub(SuperUno, SuperDos):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperUno)
printBases(SuperDos)
printBases(Sub)

"""
( object )
( object )
( SuperUno SuperDos )
"""
