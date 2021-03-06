import re

pattern = re.compile(r'^(?!.*(.).*\1)[a-zA-Z0-9]{10}')
n = int(input())
for _ in range(n):
    str = input()
    match = pattern.match(str)
    if match:
        print(f'Valid')
    else:
        print('Invalid')
"""
#Solution 1
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')"""

"""#Solution 2

import re

checks = {
  "alpha"     : lambda uid: re.match(r".*[A-Z].*[A-Z].*", uid),
  "num"       : lambda uid: re.match(r".*[0-9].*[0-9].*[0-9].*", uid),
  "alpha_num" : lambda uid: re.match(r"[A-Za-z0-9]{10}", uid),
  "repeat"    : lambda uid: not re.match(r".*(.).*\1.*", uid)
}

def main():
  for _ in range(int(input())):
    uid = input()
    print("Valid" if all(checks[check](uid) for check in checks.keys()) else "Invalid")

if __name__ == "__main__":
  main()"""

"""#Solution 3
import re
for _ in range(int(input())):
    s = input()
    print('Valid' if all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s) else 'Invalid')"""

"""#Solution 4
[print('Valid' if all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s) else 'Invalid') for s in [raw_input() for _ in range(int(raw_input()))]]"""

"""#Solution 5
import re

MATCH_UPPER = re.compile(r'[A-Z]')
MATCH_DIGIT = re.compile(r'\d')
MATCH_ALPHANUMERIC = re.compile(r'^[a-zA-Z0-9]+$')
MATCH_REPEAT_CHARACTERS = re.compile(r'^.*(.).*(\1).*$')
MATCH_LENGTH_10 = re.compile(r'^.{10}$')


def is_valid(uid):
    validators = [
        # it must contain at least 2 uppercase characters
        contains_match(MATCH_UPPER, count=2, op='>='),

        # it must contain at least 3 digits
        contains_match(MATCH_DIGIT, count=3, op='>='),

        # it should only contain alphanumeric characters
        contains_match(MATCH_ALPHANUMERIC),

        # no character should repeat
        contains_match(MATCH_REPEAT_CHARACTERS, count=0),

        # there must be exactly 10 characters
        contains_match(MATCH_LENGTH_10)
    ]
    return all(validator(uid) for validator in validators)


def contains_match(regex, count=1, op='=='):
    op_def = {
        '>=': lambda a, b: a >= b,
        '==': lambda a, b: a == b,
    }

    def validator(uid):
        op_compare = op_def[op]
        return op_compare(len(regex.findall(uid)), count)

    return validator


def main():
    from fileinput import input

    # get input
    uids = [line.rstrip() for line in input()]
    n = int(uids.pop(0))

    # for each uid ... print (In)Valid
    for i in range(n):
        uid = uids[i]
        print('Valid' if is_valid(uid) else 'Invalid')


if __name__ == '__main__':
    main()"""
"""
#Solution 6
import re

no_repeats = r"(?!.*(.).*\1)"
two_or_more_upper = r"(.*[A-Z]){2,}"
three_or_more_digits = r"(.*\d){3,}"
ten_alphanumerics = r"[a-zA-Z0-9]{10}"
filters = no_repeats, two_or_more_upper, three_or_more_digits, ten_alphanumerics

for uid in [input() for _ in range(int(input()))]:
    if all(re.match(f, uid) for f in filters):
        print("Valid")
    else:
        print("Invalid")"""