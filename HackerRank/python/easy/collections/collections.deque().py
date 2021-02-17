from collections import deque

d = deque()
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(d, cmd)(*args)

print(*[item for item in d])

