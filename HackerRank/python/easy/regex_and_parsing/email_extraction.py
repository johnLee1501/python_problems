import re

str = "Please contact info@sololearn.com for assistance jhonjhad@gmail.com"
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

match = re.findall(pattern, str)
print(match.group())
