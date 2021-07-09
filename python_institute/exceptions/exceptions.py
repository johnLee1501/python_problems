def readint(prompt, min, max):
    try:
        v = int(input(prompt))
        assert v < max and v > min
        return v
    except ValueError:
        print("Error: entrada incorrecta")
        readint(prompt, min, max)
    except AssertionError:
        print(f"Error: el valor no está dentro del rango permitido ({min}..{max})")
        readint(prompt, min, max)


v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El número es:", v)

"""
Ingresa un número entre -10 a 10: 100
Error: el valor no está dentro del rango permitido (-10..10)
Ingresa un número entre -10 a 10: asd
Error: entrada incorrecta
Ingresa un número entre -10 a 10: 1
El número es: 1
"""
