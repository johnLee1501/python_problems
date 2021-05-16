import re

html_fragment = '\n'.join([input() for _ in range(int(input()))])
print(*sorted(set(re.findall(r"://(?:www.|ww2.)?([\w.-]+\.[\w]+)[/?\"]", html_fragment))), sep=';')
