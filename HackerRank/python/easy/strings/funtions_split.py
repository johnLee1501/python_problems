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


matriz = []
for i in range(4):
    matriz.append(clean_coefficient(input()))

