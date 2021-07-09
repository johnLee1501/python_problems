class conClase:
    varia = 1

    def __init__(self):
        self.var = 2

    def metodo(self):
        pass

    def __oculto(self):
        pass


obj = conClase()

print(obj.__dict__)
print(conClase.__dict__)

"""
{'var': 2}
{'__module__': '__main__', 'varia': 1, '__init__': <function conClase.__init__ at 0x00000139392EF820>, 
'metodo': <function conClase.metodo at 0x00000139392EF8B0>, '_conClase__oculto': 
<function conClase.__oculto at 0x00000139392EF940>, '__dict__': <attribute '__dict__' of 'conClase' objects>, 
'__weakref__': <attribute '__weakref__' of 'conClase' objects>, '__doc__': None}

"""
