
#NO RESUELTO
def maxElement(n, maxSum, k):
    div_int = maxSum // n
    div_mod = maxSum % n
    return div_int if div_mod == 0 else div_int + 1


if __name__ == '__main__':
    n = int(input().strip())

    maxSum = int(input().strip())

    k = int(input().strip())

    result = maxElement(n, maxSum, k)

    print(str(result))
