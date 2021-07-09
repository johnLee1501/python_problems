from collections import deque

for _ in range(int(input())):
    _, queue = input(), deque(map(int, input().split()))

    for cube in reversed(sorted(queue)):
        if queue[-1] == cube:
            queue.pop()
        elif queue[0] == cube:
            queue.popleft()
        else:
            print('No')
            break
    else:
        print('Yes')

"""
INPUT:
2
6
4 3 2 1 3 4
3
1 3 2

OUTPUT:
Yes
No
"""

"""
for t in range(int(input())):
    input()
    lst = list(map(int, input().split()))
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i + 1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i + 1]:
        i += 1
    print("Yes" if i == l - 1 else "No")"""

"""def Solution(lst):
    pile = float('inf')
    while lst:
        num = lst.pop(0) if lst[0] > lst[-1] else lst.pop(-1)
        if num > pile: return "No"
        pile = num
    return "Yes"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().strip().split()))
        print(Solution(lst))


if __name__ == "__main__":
    main()
"""
