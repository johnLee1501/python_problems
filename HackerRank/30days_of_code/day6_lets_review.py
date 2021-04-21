n = int(input())
for _ in range(n):
    odd = ''
    even = ''
    word = input()
    for x in range(len(word)):
        if x % 2 == 0:
            odd += word[x]
        else:
            even += word[x]
    print(f'{odd} {even}')
