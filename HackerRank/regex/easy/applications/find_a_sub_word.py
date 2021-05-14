import re

phrase = """"""
n = int(input())
for x in range(n):
    phrase = phrase + '\n' + input()
n1 = int(input())
for x in range(n1):
    sub_word = input()
    pattern = r'[\w\d]%s[\w\d]' % re.escape(sub_word)
    list_sub_words = re.findall(pattern, phrase)
    count_sub_words = len(list_sub_words)
    print(count_sub_words)
"""
INPUT:
1
existing pessimist optimist this is
1
is

OUTPUT:
3
"""
