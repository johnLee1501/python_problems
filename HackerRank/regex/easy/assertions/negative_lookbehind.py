import re

Regex_Pattern = r"(?<![aeiouAEIOU])."

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

"""
Task

You have a test String S.
Write a regex which can match all the occurences of characters which are not immediately preceded by vowels (a, e, i, u, o, A, E, I, O, U).

input= 1o1s
output= Number of matches : 3
"""
