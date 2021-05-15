import re

n = int(input())
fragment_html = ''

for x in range(n):
    fragment_html += input()

fragment_html = re.sub(r'<!--.*?-->', '', fragment_html)

tags = re.findall(r'<(\w+)(.*?)>', fragment_html)

for tag in tags:
    print(tag[0])
    attributes = re.findall(r'([\w-]+)="(.*?)"', tag[1])

    if attributes:
        for attribute in attributes:
            print(f'-> {attribute[0]} > {attribute[1]}')
