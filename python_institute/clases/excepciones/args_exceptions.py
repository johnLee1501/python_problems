def printargs(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    printargs(e.args)

try:
    raise Exception("mi excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    printargs(e.args)

try:
    raise Exception("mi", "excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    printargs(e.args)

"""
:  : 
mi excepción : mi excepción : mi excepción
('mi', 'excepción') : ('mi', 'excepción') : ('mi', 'excepción')"""
