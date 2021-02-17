n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swap_count = 0
while True:
    for i in range(n - 1):
        if a[i + 1] < a[i]:
            swap_count += 1
            a[i + 1], a[i] = a[i], a[i + 1]
            break
    else:
        break
print(f'Array is sorted in {swap_count} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}')
