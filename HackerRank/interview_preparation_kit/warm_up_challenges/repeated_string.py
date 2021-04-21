def repeatedString(s, n):
    factor = n // len(s)
    remainder = n % len(s)
    base = s.count('a')
    return base * factor + s[:remainder].count('a')


if __name__ == '__main__':
    s = input()
    n = int(input())
    print(repeatedString(s, n))
