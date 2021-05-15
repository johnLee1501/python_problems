import re

str = ' '.join([input() for _ in range(int(input()))])

for _ in range(int(input())):
    word = input()
    index = word.find('our')
    print(len(re.findall(r'\b%s(o|ou)r%s\b' % (word[:index], word[index + 3:]), str)))

"""
#OTHER SOLUTION
import re

str = ' '.join([input() for _ in range(int(input()))])

for _ in range(int(input())):
    print(len(re.findall(input().replace('our','ou?r')+r'\b', str)))
"""
"""
INPUT:
10
splendour wealth piece recognition savoury endeavour oil cannot reality fish
sincere savor argument vigour chain awake cap surprising savoury jump
natural study process immoral flag vigour habit assist candy pet
shoulder aside slightly onto crash later disagreement savour rumour entrance
splendour petrol unable inevitably crowd growth fasten leading responsibility artificially
equally alarmed also knowledge ok splendor armory pick sale be
activity rumour ending alcoholic savory curve splendour honestly enjoyable rumour
determined used rumor union affair odor granddaughter elect endeavor alter
savor hour enjoyable waiter divorce at mental prepared folding primary
cheaply vegetable upon splendor disease savor it cast hear cardboard
9
endeavour
savoury
savour
vigour
valour
splendour
rumour
odour
armoury

OUTPUT:
2
3
4
2
0
5
4
1
1
"""