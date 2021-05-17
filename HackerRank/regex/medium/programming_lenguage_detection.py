import re
import sys
code = sys.stdin.read()
if re.findall(r'int main\(\)',code):
    print('C')
elif re.findall(r'static void main',code):
    print('Java')
else:
    print('Python')

"""
Regex pattern

C = "(?s).*(#\\s*include\\s*(<\\s*[\\w/]+(\\.\\w+)?\\s*>|\"[\\w/]+(\\.\\w+)?\"\\s*))(?s).*"

JAVA = "(?s).*(^(public\\s+|private\\s+|protected\\s+)*.*\\w+\\(.*?\\)\\s*\\{|import\\s+[\\w\\.\\*]+;)(?s).*"

PYTHON = "(?s).*(^print\\s\".*\"$|^#\\s.*$|def\\s.*$|^if\\s[^()]+:)(?s).*"
"""