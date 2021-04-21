import re

s, k = input(), input()
end = 0
while end <= len(s):
    match = re.search(k, s[end:])
    if match:
        print(f'({match.start() + end}, {match.end() + end - 1})')
        if len(k) > 1:
            end = match.end() + end - 1
        else:
            end = match.end() + end
    elif match is None and end == 0:
        print('(-1, -1)')
        break
    else:
        break
