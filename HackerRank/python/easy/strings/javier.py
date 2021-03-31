import numpy as np
import sys
import re


def clean_coefficient(function):
    coefficient_list = re.split(r'[A-Za-z]', function)
    for x in range(len(coefficient_list)):
        if coefficient_list[x] == '+':
            coefficient_list[x] = '1'
        elif coefficient_list[x] == '-':
            coefficient_list[x] = '-1'
        elif '+' in coefficient_list[x]:
            coefficient_list[x] = coefficient_list[x].replace('+', '').strip()
        elif '=' in coefficient_list[x]:
            coefficient_list[x] = coefficient_list[x].replace('=', '').strip()
    coefficient_list = list(map(int, coefficient_list))
    return coefficient_list


print("Ingresa \"f\" para escribir funciones o \"m\" para llenar la matriz")
chose = input("\"f\" o \"m\"")
n = 4
matrix = np.zeros((n, n + 1))
solution = np.zeros(n)
if chose == "f":
    matriz = []
    for i in range(4):
        print("Ingrese la función " + str(i + 1))
        matriz.append(clean_coefficient(input()))
    for i in zip(matriz):
        for j in range(n + 1):
            matrix[i][j] = matriz[int(i)]
    print(matrix)
elif chose == "m":
    print('Ingrese los números de la matríz por posición:')
    for i in range(n):
        for j in range(n + 1):
            matrix[i][j] = float(input('matríz[' + str(i) + '][' + str(j) + ']='))
for i in range(n):
    if matrix[i][i] == 0.0:
        sys.exit('¡División por 0 en la diagonal!')
for j in range(n):
    if i != j:
        ratio = matrix[j][i] / matrix[i][i]
        for k in range(n + 1):
            matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]
            if k == 4:
                print("LA MATRIZ")
for i in range(n):
    solution[i] = matrix[i][n] / matrix[i][i]
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' % (i, solution[i]), end='\t')
