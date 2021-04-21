from collections import OrderedDict


def merge_the_tools(string, k):
    length = len(string)
    f = int(length / k)
    i = 0
    j = 0
    for x in range(f):
        i = j
        j += k
        substring = string[i:j]

        result = "".join(set(substring))
        result2 = "".join(OrderedDict.fromkeys(substring))
        result3 = ''.join([n for m, n in enumerate(substring) if n not in substring[:m]])

        print(result2)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
