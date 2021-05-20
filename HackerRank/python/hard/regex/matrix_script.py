import re

n, m = map(int, input().split())
words, text = [], ""
for _ in range(n):
    words.append(input())

for column_words in zip(*words):
    text += "".join(column_words)

print(re.sub(r"(?<=\w)(\W+)(?=\w)", " ", text))

"""
#Other solution
import re

matrix, text = [], ""
n, m = map(int, input().split())

[matrix.append(input()) for _ in range(n)]

for x in range(m):
    for y in range(n):
        text += matrix[y][x]

text = re.sub(r'(?<=[A-Za-z\d])[^A-Za-z\d]+(?=[A-Za-z\d])', ' ', text)
print(text)
"""
"""
INPUT:
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

OUTPUT:
This is Matrix#  %!
"""
