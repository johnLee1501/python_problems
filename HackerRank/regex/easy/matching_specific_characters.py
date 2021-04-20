Regex_Pattern = r'^[123][120][xs0][30aA][xsu][\.,]$'

import re

string = input()
print(str(bool(re.search(Regex_Pattern, string))).lower())
