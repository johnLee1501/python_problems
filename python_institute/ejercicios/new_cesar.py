text = input()
desplazamiento = int(input())
cifrado = ''
for char in text:
    if char.isupper():
        code = ord(char) + desplazamiento
        if code > 90:
            code -= (90 - 64)
        cifrado += chr(code)
    elif char.islower():
        code = ord(char) + desplazamiento
        if code > 122:
            code -= (122 - 96)
        cifrado += chr(code)
    else:
        cifrado += char
print(cifrado)
