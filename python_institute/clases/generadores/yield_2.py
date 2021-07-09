def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2


t = [x for x in potenciasDe2(5)]
print(t)

t = list(potenciasDe2(3))
print(t)

for i in range(20):
    if i in potenciasDe2(4):
        print(i)

for v in potenciasDe2(8):
    print(v)
