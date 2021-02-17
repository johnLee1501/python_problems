
def sockMerchant(n, ar):
    sum = 0
    ar_set = set(ar)
    for x in ar_set:
        sum += ar.count(x) // 2
    return sum


if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().split()))

    print(sockMerchant(n, ar))
