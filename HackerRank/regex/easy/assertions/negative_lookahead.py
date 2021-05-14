import re

Regex_Pattern = r'(.)(?!\1)'
Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))


"""
Task

You have a test String S .
Write a regex which can match all characters which are not immediately followed by that same character.

Example

If S = goooo, then regex should match g and o. Because the first g is not follwed by g and the last o is not followed by o.
"""