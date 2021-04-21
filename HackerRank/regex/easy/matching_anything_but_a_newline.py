# regex_pattern = r"^[^\n]{3}\.[^\n]{3}\.[^\n]{3}\.[^\n]{3}$"

import re

regex_pattern = r"^(.{3}\.?){4}$"

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
