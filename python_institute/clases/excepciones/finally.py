def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n


print(reciproco(2))
print(reciproco(0))

"""
Todo salió bien
Es el momento de decir adiós
0.5
División fallida
Es el momento de decir adiós
None"""
