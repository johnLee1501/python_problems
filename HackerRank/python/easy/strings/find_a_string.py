"""def count_substring(string, sub_string):
    c = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            c += 1
    return c"""


def count_substring(string, sub_string):
    count = 0
    i = string.find(sub_string)
    while i != -1:
        count += 1
        i = string.find(sub_string, i + 1)
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
