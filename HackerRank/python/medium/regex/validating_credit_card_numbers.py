import re
groups_pattern = r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$'
consecutive_pattern = r'(\d)(-?)\1(-?)\1(-?)\1'
n = int(input())
for x in range(n):
    card_number = input()
    try:
        assert re.search(groups_pattern, card_number)
        assert not re.search(consecutive_pattern, card_number)
    except:
        print('Invalid')
    else:
        print('Valid')
"""
INPUT:
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

OUTPUT:
Valid
Valid
Invalid
Valid
Invalid
Invalid
"""
"""

import re
pattern = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if pattern.search(input()) else "Invalid")

"""

"""import re


def check(card):
    if not re.search("^[456]\d{3}(-?\d{4}){3}$", card) or re.search(r"(\d)\1{3}", re.sub("-", "", card)):
        return False
    return True


for i in range(int(input())):
    print("Valid" if check(input()) else "Invalid")
"""