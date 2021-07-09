from itertools import product

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i ** 2 for i in x) % M, product(*N))
print(max(results))

"""from itertools import product

k, m = map(int, input().split())
matrix = [list(map(int, input().split()))[1:] for _ in range(k)]
combinations_arrays = list(product(*matrix))
max_value = 0
for combination in combinations_arrays:
    result_equation = sum([i ** 2 for i in combination]) % m
    if result_equation > max_value:
        max_value = result_equation
print(max)
"""
"""INPUT:
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10

OUTPUT:
206"""
