import re


def fun(s):
    return re.match(r"^([\w\-]+)@([A-Za-z\d]+)\.([A-Za-z]{,3})$", s)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

"""
INPUT:

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

OUTPUT:
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""


"""
OTHER SOLUTION
import re

def fun(s):
  pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
  return pattern.match(s)
  """