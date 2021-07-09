fecha = [int(x) for x in input()]

suma = sum(fecha)

while suma > 9:
    suma = sum([int(x) for x in str(suma)])
print(suma)
