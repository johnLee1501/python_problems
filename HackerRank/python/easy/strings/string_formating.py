


def print_formatted(number):
    w = len(bin(number)[2:])
    for x in range(1, number + 1):
        print(str(x).rjust(w, ' '), str(oct(x)[2:]).rjust(w, ' '), str(hex(x)[2:].upper().rjust(w, ' ')),
              str(bin(x)[2:].rjust(w, ' ')))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
