if __name__ == '__main__':
    n = int(input())
    list_string = input().split()
    list_int = map(int, list_string)

    tuple_int = tuple(list_int)

    print(hash(tuple_int))
