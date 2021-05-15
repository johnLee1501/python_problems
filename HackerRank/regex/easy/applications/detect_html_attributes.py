import re

n = int(input())
fragment_html = ''
dict_tags = {}

for x in range(n):
    fragment_html += input()
tags = re.findall(r'<(\w+)(.*?)>', fragment_html)

for tag in tags:
    attributes = re.findall(r'\s(\w+)=', tag[1])
    tag_attributes = dict_tags.get(tag[0])

    if tag_attributes:
        attributes = tag_attributes + attributes
    dict_tags[tag[0]] = attributes
dict_tags = dict(sorted(dict_tags.items()))

for key, value in dict_tags.items():
    value = ','.join(sorted(list(set(value))))
    print(f'{key}:{value}')
"""
#Other Solution

#N1
import re
from collections import defaultdict

inputs = []
for _ in range(int(input())):
    inputs.append(input())

string = ''.join([inp for inp in inputs])

results = re.findall(r'<(\w+)(|\s+[^>]*)>', string, re.I)

tag_attributes = defaultdict(list)
for res in results:
    tag, attr = res
    tag_attributes[tag].extend(
        re.findall(r'(\w+)=[\'\"]', attr)
    )

for tag, attr in sorted(tag_attributes.items()):
    print(':'.join([tag, ','.join(sorted(set(attr)))]))
    
# N2
import re
from collections import defaultdict

tags = defaultdict(set)

for _ in range(int(input())):
    for tag, attrs in re.findall(r'<(\w+)(.*?)?>', input()):
        tags[tag].update(
            re.findall(r'\s(\w+)=', attrs)
        )

for tag, attrs in sorted(tags.items()):
    print(tag + ":" + ",".join(sorted(attrs)))
"""
