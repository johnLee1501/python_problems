class conClase:
    def __init__(self, valor = None):
        self.var = valor

obj1 = conClase("objeto")
obj2 = conClase()

print(obj1.var)
print(obj2.var)