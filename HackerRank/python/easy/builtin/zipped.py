n, x = map(int, input().split())
matriz = []
for _ in range(x):
    matriz.append(list(map(float, input().split())))
zip_matriz = zip(*matriz)
[print(sum(student) / len(student)) for student in zip_matriz]


"""
INPUT:
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

OUTPUT:
90.0 
91.0 
82.0 
90.0 
85.5 
"""