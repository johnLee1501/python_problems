import re
import email.utils

pattern = re.compile(r'^[A-Za-z][\w\-\.]+\@[A-Za-z]+\.[A-Za-z]{1,3}$')
n = int(input())
for _ in range(n):
    email_address = input()
    email_parse = email.utils.parseaddr(email_address)
    if pattern.match(email_parse[1]):
        print(email.utils.formataddr(email_parse))
