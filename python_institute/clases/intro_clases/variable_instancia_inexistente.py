class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


objetoEjemplo = ClaseEjemplo(1)

print(objetoEjemplo.a)
print(objetoEjemplo.b)

"""
1
Traceback (most recent call last):
  File "main.py", line 11, in <module>
    print(objetoEjemplo.b)
AttributeError: 'ClaseEjemplo' object has no attribute 'b'
"""
