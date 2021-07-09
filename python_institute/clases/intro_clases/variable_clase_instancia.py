class ClaseEjemplo:
    varia = 1

    def __init__(self, val):
        self.varia = val


print(ClaseEjemplo.__dict__)
objetoEjemplo = ClaseEjemplo(2)

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)

"""
{'__module__': '__main__', 'varia': 1, '__init__': <function ClaseEjemplo.__init__ at 0x7f030e5bd0e0>, '__dict__': <attribute '__dict__' of 'ClaseEjemplo' objects>, '__weakref__': <attribute '__weakref__' of 'ClaseEjemplo' objects>, '__doc__': None}
{'__module__': '__main__', 'varia': 1, '__init__': <function ClaseEjemplo.__init__ at 0x7f030e5bd0e0>, '__dict__': <attribute '__dict__' of 'ClaseEjemplo' objects>, '__weakref__': <attribute '__weakref__' of 'ClaseEjemplo' objects>, '__doc__': None}
{'varia': 2}
"""


class ClaseEjemplo:
    varia = 1

    def __init__(self, val):
        ClaseEjemplo.varia = val


print(ClaseEjemplo.__dict__)
objetoEjemplo = ClaseEjemplo(2)

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)

"""
{'__module__': '__main__', 'varia': 1, '__init__': <function ClaseEjemplo.__init__ at 0x7eff94da40e0>, '__dict__': <attribute '__dict__' of 'ClaseEjemplo' objects>, '__weakref__': <attribute '__weakref__' of 'ClaseEjemplo' objects>, '__doc__': None}
{'__module__': '__main__', 'varia': 2, '__init__': <function ClaseEjemplo.__init__ at 0x7eff94da40e0>, '__dict__': <attribute '__dict__' of 'ClaseEjemplo' objects>, '__weakref__': <attribute '__weakref__' of 'ClaseEjemplo' objects>, '__doc__': None}
{}
"""
