import re

Regex_Pattern = r'^[A-z]*s$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())

"""
Write a RegEx to match a test string, S , under the following conditions:

S should consist of only lowercase and uppercase letters (no numbers or symbols).
S should end in s.

INPUT = Kites
OUTPUT = true
"""