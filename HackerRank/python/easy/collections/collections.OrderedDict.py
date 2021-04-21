from collections import OrderedDict

n = int(input())
items_market = OrderedDict()
for _ in range(n):
    name, space, price = input().rpartition(" ")
    items_market[name] = int(price) + items_market.get(name, 0)
for k, j in items_market.items():
    print(f'{k} {j}')
