dos = lambda: 2  # No recibe nada y retorna un 2
cuadrado = lambda x: x * x  # Recibe x y retorna x*x
potencia = lambda x, y: x ** y

for a in range(-2, 3):
    print(cuadrado(a), end=" ")
    print(potencia(a, dos()))

with_map = list(map(cuadrado, [1, 2, 3, 4, 5]))
