n = int(input())
"""phone_book = {}
for _ in range(n):
    key, value = input().split()
    phone_book[key] = value"""
phone_book = dict(input().split() for _ in range(n))
while True:
    try:
        key = input()
        value = phone_book.get(key)
        if value:
            print(f'{key}={value}')
        else:
            print('Not found')
    except:
        break
