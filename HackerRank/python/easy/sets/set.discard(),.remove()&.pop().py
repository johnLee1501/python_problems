n = int(input())
numbers = set(map(int, input().split()))
for _ in range(int(input())):
    cmd, *args = input().split()
    args = map(int, args)
    getattr(numbers, cmd)(*args)

print(sum(numbers))
