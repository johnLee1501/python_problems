def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return n


print(reciproco(2))
print(reciproco(0))

"""
Todo salió bien
0.5
División fallida
None"""
