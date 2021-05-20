import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))


"""
# Other Solution
import string


def print_rangoli(size):
    alphabet = list(string.ascii_lowercase)
    size_rangoli = (size * 4 - 3)
    for x in range(size, 0, -1):
        letter = alphabet[x - 1]
        for i in range(x, size):
            letter = f'{alphabet[i]}-{letter}-{alphabet[i]}'
        print(letter.center(size_rangoli, '-'))
    for x in range(2, size + 1):
        letter = alphabet[x - 1]
        for i in range(x, size):
            letter = f'{alphabet[i]}-{letter}-{alphabet[i]}'
        print(letter.center(size_rangoli, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
"""