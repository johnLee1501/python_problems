import re

regex_Pattern = r"(\d{2}\D){2}\d{4}"
print(str(bool(re.search(regex_Pattern, input()))).lower())
