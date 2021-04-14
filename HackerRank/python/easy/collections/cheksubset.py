cases = int(input())
for _ in range(cases):
    len_a, set_a, len_b, set_b = input(), set(input().split()), input(), set(input().split())
    print(set_a.issubset(set_b))
