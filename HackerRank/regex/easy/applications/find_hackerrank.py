import re

n = int(input())
for _ in range(n):
    conversation = input()
    if re.search(r'^hackerrank.+?(^hackerrank)?$', conversation, re.DOTALL):
        print('1')
    elif re.search(r'^(^hackerrank)?.+?hackerrank$', conversation):
        print('2')
    elif re.search(r'(^hackerrank$|^hackerrank.*?hackerrank$)', conversation, re.DOTALL):
        print('0')
    else:
        print('-1')
"""
INPUT:
4
i love hackerrank
hackerrank is an awesome place for programmers
hackerrank
i think hackerrank is a great place to hangout

OUTPUT:
2
1
0
-1
"""