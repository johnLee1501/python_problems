class MiClase:
    pass


obj = MiClase()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.entero = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

"""
{'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'entero': 4, 'z': 5}
"""
