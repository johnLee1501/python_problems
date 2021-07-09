class ClaseEjemplo:
    def __init__(self, val=1):
        self.__primera = val

    def setSegunda(self, val):
        self.__segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.__tercera = 5

print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)

"""
{'_ClaseEjemplo__primera': 1}
{'_ClaseEjemplo__primera': 2, '_ClaseEjemplo__segunda': 3}
{'_ClaseEjemplo__primera': 4, '__tercera': 5}
"""
