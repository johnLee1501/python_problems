from collections import Counter

if __name__ == '__main__':
    amount = 0
    num_shoes = int(input())
    shoes = map(int, input().split())
    counter = Counter(shoes)
    num_customers = int(input())
    for _ in range(num_customers):
        size, price = map(int, input().split())
        if counter.get(size, 0) > 0:
            counter[size] += -1
            amount += price
    print(amount)


"""Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output
200"""