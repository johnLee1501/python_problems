Regex_Pattern = r'^[^\d][^aeiou][^cDF][^\s][^AEIOU][^\.,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())