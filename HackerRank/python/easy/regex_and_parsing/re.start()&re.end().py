"""import re

s, k = input(), input()
end = 0
while end <= len(s):
    match = re.search(k, s[end:])
    if match:
        print(f'({match.start() + end}, {match.end() + end - 1})')
        end = match.end() + end - 1
    elif match is None and end == 0:
        print('(-1,-1)')
    else:
        break
"""

