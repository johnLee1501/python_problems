n = int(input())
arr = input().split()

"""arr.reverse()
print(' '.join(arr))"""

"""for x in range(len(arr) - 1, -1, -1):
    print(arr[x], end=' ')"""

print(" ".join(map(str, arr[::-1])))
