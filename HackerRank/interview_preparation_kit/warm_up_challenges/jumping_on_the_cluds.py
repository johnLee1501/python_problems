def jumpingOnClouds(c, length):
    s = 0
    jumps = 0
    while s < length - 1:
        if s < length - 2:
            if c[s + 2] == 0:
                s += 2
                jumps += 1
                continue
        s += 1
        jumps += 1
    return jumps


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    print(jumpingOnClouds(c, n))
