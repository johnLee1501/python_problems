import re

str = """Please contact 
jhonjhad@gmail.com for assistance 
jhonjhad@gmail.com"""
pattern = r"Please contact[\w\s\.\@]*jhonjhad@gmail.com"

match = re.search(pattern, str)
print(match.group())
