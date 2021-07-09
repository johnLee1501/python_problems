from collections import Counter

s = input()
count_dict = Counter(s)
count_dict_sort = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
print(*[f'{count_dict_sort[x][0]} {count_dict_sort[x][1]}' for x in range(3)], sep='\n')

"""
INPUT:
qwertyuiopasdfghjklzxcvbnm

OUTPUT:
a 1
b 1
c 1
"""

"""OTHER SOLUTIONS
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
"""
"""
from collections import Counter

class OrderedCounter(Counter):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]


"""