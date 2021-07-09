try:
    i = int("Hola!")
except Exception as e:
    print(e)
    print(e.__str__())

    """
    invalid literal for int() with base 10: 'Hola!'
invalid literal for int() with base 10: 'Hola!'"""
