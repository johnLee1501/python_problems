import re

n = int(input())
text = ''
for _ in range(n):
    text += input()
n2 = int(input())
for _ in range(n2):
    word = input()
    print(len(re.findall(r'(%s|%s)' % (word, word[:-2] + 'se'), text)))
"""
INPUT:
7
unfair arrival faint region pride realise paralyse length officially disturbing
call fashionable room take claim capable biscuit cough qualified realze
decoration indeed caramelise gas habit downward salad realize on knee
catalyse blade artistic put careless league final waste catalyse bedroom
door materialize catalyse round point routine celebration paralyse stranger weather
artificially materialise personally elegant lane celebration statement whom tend bone
realise infect coloured planet pet estimate lane infectious destroy exchange
9
materialize
catalyze
realize
hydrolyze
caramelize
recognize
organize
paralyze
colonize

OUTPUT:
2
3
3
0
1
0
0
2
0
"""

"""
OTHER SOLUTION

import re

str = ' '.join([input() for _ in range(int(input()))])

for _ in range(int(input())):
    print(len(re.findall(input()[:-2]+'[zs]e', str)))
    

import re

data = [input() for _ in range(int(input()))]

for _ in range(int(input())):
    pattern = re.compile("%s[sz]e" % input()[:-2])
    print(sum([len(pattern.findall(line)) for line in data]))    
"""