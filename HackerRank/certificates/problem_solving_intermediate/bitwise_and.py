#NO RESUELTO

from itertools import combinations


def countPairs(arr):
    list_combinations = combinations(arr, 2)
    list_bitwise_and = [int(bin(combination[0] & combination[1]), 2) for combination in list_combinations]
    count = 0
    for x in list_bitwise_and:
        if (x & (x-1) == 0) and x != 0:
            count += 1
    return count


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = []
    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countPairs(arr)

    print(str(result))
