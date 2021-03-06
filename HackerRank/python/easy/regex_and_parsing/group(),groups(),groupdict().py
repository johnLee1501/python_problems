import re

# pattern = r'([A-Za-z0-9])\1+'
# pattern = r'(\w(?!_))\1+'
pattern = r'([^\W_])\1+'
str = input()
match = re.search(pattern, str)
if match:
    print(match.group(1))
else:
    print('-1')
