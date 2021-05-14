import re

Regex_Pattern = r'^[A-Za-z02468]{40}[\s13579]{5}$'

print(str(bool(re.search(Regex_Pattern, input()))).lower())


"""
You have a test string S .
Your task is to write a regex that will match S using the following conditions:

S must be of length equal to 45.
The first 40  characters should consist of letters(both lowercase and uppercase), or of even digits.
The last 5 characters should consist of odd digits or whitespace characters.

Input = 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
Output = true
"""