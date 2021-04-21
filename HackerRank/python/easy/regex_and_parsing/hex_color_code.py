import re

pattern = r'(#[0-9A-F]{6}|#[0-9A-F]{3})(?!\s*\{)'
n = int(input())
code = "".join([input() for _ in range(n)])
list_colors = re.findall(pattern, code, flags=re.I)
print(*list_colors, sep='\n')

"""
#SOLUTION N1
import re

pattern_colors = r'(#[0-9A-F]{3}|#[0-9A-F]{6})[^0-9A-F]'
pattern_selectors = r'(#[0-9A-F]{3}|#[0-9A-F]{6})\s*\{'
n = int(input())
code = "".join([input() for _ in range(n)])
list_colors = re.findall(pattern_colors, code, flags=re.I)
list_selectors = re.findall(pattern_selectors, code, flags=re.I)
list_correct_colors = [color for color in list_colors if color not in list_selectors]
print(*list_correct_colors, sep='\n')
"""

# INPUT
"""
35
.arrow-up {
	width: 0;
	height: 0;
	border-left: 5px solid transparent;
	border-right: 5px solid transparent;

	border-bottom: 5px solid black;
}

.arrow-down {
	width: 0;
	height: 0;
	border-left: 20px solid transparent;
	border-right: 20px solid transparent;

	border-top: 20px solid #f00;
}

.arrow-right {
	width: 0;
	height: 0;
	border-top: 60px solid transparent;
	border-bottom: 60px solid transparent;

	border-left: 60px solid green;
}

#f0f {
	width: 0;
	height: 0;
	border-top: 10px solid transparent;
	border-bottom: 10px solid transparent;

	border-right:10px solid blue;
}
"""
# OUTPUT
"""
#f00
"""
