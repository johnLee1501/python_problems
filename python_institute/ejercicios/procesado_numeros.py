# Procesador de números

linea = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = linea.split()
total = 0
try:
    assert strings
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except AssertionError:
    print("no ingresó ningún número.")
except ValueError:
    print(substr, "no es un numero.")
