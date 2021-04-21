input()
set_a = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    cmd, len_set_b = input().split()
    set_b = set(map(int, input().split()))
    getattr(set_a, cmd)(set_b)
print(sum(set_a))
