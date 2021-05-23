input()
numbers = input().split()

if all([number >= 0 for number in map(int, numbers)]):
    print(any([number == number[::-1] for number in numbers]))
else:
    print(False)

"""
OTHER SOLUTION
N,n = int(input()),input().split()
print all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n])
"""

"""
INPUT:
5
12 9 61 5 14 

OUTPUT:
True
"""