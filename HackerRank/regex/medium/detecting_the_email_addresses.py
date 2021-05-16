import re

text_fragment = '\n'.join([input() for _ in range(int(input()))])
print(*sorted(set(re.findall(r"([\w.]+@[\w.]+[\w])", text_fragment))), sep=';')

