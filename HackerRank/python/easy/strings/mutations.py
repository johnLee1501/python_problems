s = list(input())
index, value = input().split()
s.insert(int(index), value)
print(''.join(s))
