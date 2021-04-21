set_a = set(input().split())
cases = int(input())
status = True
for _ in range(cases):
    set_aux = set(input().split())
    if not set_a.issuperset(set_aux):
        status = False
print(status)


"""set_a = set(input().split())
cases = int(input())
status = True
for _ in range(cases):
    set_aux = set(input().split())
    if (set_a.issuperset(set_aux) and len(set_a.difference(set_aux))==0) or ( not set_a.issuperset(set_aux)) :
        status = False
        break
print(status)"""


"""
Sample Input 

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 

False
"""