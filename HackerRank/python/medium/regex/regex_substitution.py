import re

text = '\n'.join([input() for _ in range(int(input()))])
text = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', text)
print(text)

"""
# OTHER SOLUTION
import re

text = '\n'.join([input() for _ in range(int(input()))])
text = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', text)
text = re.sub(r'(?<=\s)&&(?=\s)', 'and', text)
print(text)
"""
