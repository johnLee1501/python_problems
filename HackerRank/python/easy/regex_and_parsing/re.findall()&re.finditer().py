import re

v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
string_main = input()
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), string_main, flags=re.I)
print('\n'.join(m or ['-1']))
