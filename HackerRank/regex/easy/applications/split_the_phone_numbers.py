import re

n = int(input())
for _ in range(n):
    codes = input()
    codes_match = re.search(r'(\d{1,3})(\s|-)(\d{1,3})\2(\d{4,10})', codes)
    if codes_match:
        codes_match = codes_match.groups()
        print(f'CountryCode={codes_match[0]},LocalAreaCode={codes_match[2]},Number={codes_match[3]}')

"""
INPUT=
6
148-809-2561957985
188-547-5864327428
891-454-9195497623
648-42-380306686
824-417-6460145493
489-16-9839392781

OUTPUT:
CountryCode=148,LocalAreaCode=809,Number=2561957985
CountryCode=188,LocalAreaCode=547,Number=5864327428
CountryCode=891,LocalAreaCode=454,Number=9195497623
CountryCode=648,LocalAreaCode=42,Number=380306686
CountryCode=824,LocalAreaCode=417,Number=6460145493
CountryCode=489,LocalAreaCode=16,Number=9839392781
"""
"""
OTHER SOLUTIONS
def Wrapper(func):
    def Decorate(Num):
        Num = func(Num)
        return "CountryCode=%s,LocalAreaCode=%s,Number=%s" % Num
    return Decorate

@Wrapper
def PhoneNumber(Num):
    return re.match(RegEx,Num).groups();

for _ in range(int(input())):
    print(PhoneNumber(input().strip()))
    
    """