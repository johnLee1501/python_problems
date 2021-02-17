def hourglassSum(arr):
    max = -100
    for y in range(4):
        for x in range(4):
            sum = arr[y][x] + arr[y][x + 1] + arr[y][x + 2] \
                  + arr[y + 1][x + 1] \
                  + arr[y + 2][x] + arr[y + 2][x + 1] + arr[y + 2][x + 2]
            if sum > max:
                max = sum
    return max


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglassSum(arr))



"""
sum = []
for i in range(len(arr) - 2):
    for j in range(len(arr) - 2):
        sum.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] +
                   arr[i + 2][j + 2])

print(max(sum))
"""
