def int_to_binary(n):
    nums = []
    while n > 0:
        remainder = n % 2
        n //= 2
        nums.append(remainder)
    nums.reverse()
    return "".join(map(str, nums))


def count_consecutives_1s(binary):
    list_consecutive = binary.split('0')
    len_max = len(max(list_consecutive))
    return len_max


if __name__ == '__main__':
    n = int(input())
    binary = int_to_binary(n)
    print(count_consecutives_1s(binary))

"""
One Liner Solution:
print(len(max(bin(int(input().strip()))[2:].split('0'))))
"""
