import re

n = int(input())
for x in range(n):
    coordinates = input()
    if re.search((
            r'^\(([-|+]?([1-8]\d{d1}|90{d2}|[1-9]{d1})),\s([-|+]?([1-9]{d1}|[1-9]\d{d1}|1[0-7]\d{d1}|180{d2}))\)$').format(
        d1='(\.[\d]+)?', d2='(\.0+)?'), coordinates):
        print('Valid')
    else:
        print('Invalid')

"""
#Other Solution
import re

SIGN = '[\+-]?'
DECIMALS = '(\.[0-9]+)?'
ZEROS = '(\.0+)?'

LATITUDE =  f'{SIGN}(90{ZEROS}|[1-8]\d{DECIMALS}|\d{DECIMALS})'
LONGITUDE = f'{SIGN}(180{ZEROS}|1[0-7]\d{DECIMALS}|[1-9]\d{DECIMALS}|\d{DECIMALS})'

REGEX = f'\({LATITUDE}, {LONGITUDE}\)'
pattern = re.compile(REGEX)

def validate(value):
    return pattern.search(value)

for _ in range(int(input())):
    if validate(input()):
        print('Valid')
    else:
        print('Invalid')
"""
"""
INPUT:
50
(-126, -158)
(-126.400010, -158.400010)
(-95, -96)
(-95.738043, -96.738043)
(-137, -148)
(-137.5942, -148.5942)
(-120, -203)
(-120.969949, -203.969949)
(-116, -126)
(-116.894222, -126.894222)
(-112, -160)
(-112.96381, -160.96381)
(-34, -24)
(-34.834552, -24.834552)
(-141, -108)
(-141.956646, -108.956646)
(-59, -94)
(-59.158806, -94.158806)
(-87, -63)
(-87.452080, -63.452080)
(-94, -88)
(-94.697436, -88.697436)
(-51, -102)
(-51.760312, -102.760312)
(-98, -158)
(-98.177819, -158.177819)
(-92, -68)
(-92.853231, -68.853231)
(-67, -32)
(-67.76542, -32.76542)
(-99, -287)
(-99.15413, -287.15413)
(-97, -146)
(-97.582865, -146.582865)
(-22, -81)
(-22.114593, -81.114593)
(-29, -118)
(-29.15012, -118.15012)
(-53, -165)
(-53.295357, -165.295357)
(-115, -249)
(-115.599169, -249.599169)
(-54, -70)
(-54.832927, -70.832927)
(-119, -196)
(-119.821728, -196.821728)
(-110, -223)
(-110.369532, -223.369532)
(-71, -146)
(-71.616864, -146.616864)
OUPUT:
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
Valid
Valid
Invalid
Invalid
Valid
Valid
Valid
Valid
Invalid
Invalid
Valid
Valid
Invalid
Invalid
Invalid
Invalid
Valid
Valid
Invalid
Invalid
Invalid
Invalid
Valid
Valid
Valid
Valid
Valid
Valid
Invalid
Invalid
Valid
Valid
Invalid
Invalid
Invalid
Invalid
Valid
Valid
"""
