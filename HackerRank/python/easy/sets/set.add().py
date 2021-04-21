n = int(input())
countries = set()
for _ in range(n):
    countries.add(input().rstrip())
print(len(countries))
