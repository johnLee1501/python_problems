import re

Regex_Pattern = r'[\d]{1,2}[A-z]{3,}[\.]{0,3}'

print(str(bool(re.search(Regex_Pattern, input()))).lower())

"""
You have a test string .
Your task is to write a regex that will match S using the following conditions:

S should begin with 1 or 2 digits.
After that, S should have 3 or more letters (both lowercase and uppercase).
Then S should end with up to 3 . symbol(s). You can end with 0 to 3 . symbol(s), inclusively.

Input = 3threeormorealphabets.
Output = true
"""