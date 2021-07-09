text = input().lower().replace(" ", "")
if text == text[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
