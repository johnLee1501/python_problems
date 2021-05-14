import re

n = int(input())
for x in range(n):
    ip = input()
    ipv4_match = re.match(r'^(\d+).(\d+).(\d+).(\d+)$', ip)
    ipv6_match = re.match(r'^[\dA-Fa-f]{1,4}(?::[\dA-Fa-f]{1,4}){7}$', ip)
    if ipv4_match:
        ip_subs = list(ipv4_match.groups())
        try:
            for ip_sub in ip_subs:
                ip_sub = int(ip_sub)
                assert ip_sub <= 255
        except:
            print('Neither')
        else:
            print('IPv4')
    elif ipv6_match:
        print('IPv6')
    else:
        print('Neither')
"""
INPUT: 3
This line has junk text.
121.18.19.20
2001:0db8:0000:0000:0000:ff00:0042:8329

OUTPUT:
Neither
IPv4
IPv6
"""

"""
#Other solutions


# n1
import re
n = int(input())
s4 = ('^'+"{v}\."*3+"{v}$").format(v = "(25[0-5]|2[0-4]\d|[01]?\d?\d)")
s6 = ('^'+"{v}:"*7+"{v}$").format(v = "[\da-f]{1,4}")
ip4 = re.compile(s4)
ip6 = re.compile(s6)
while n:
    s = input()
    if ip4.match(s):
        print('IPv4')
    elif ip6.match(s):
        print('IPv6')
    else:
        print('Neither')
    n-=1
    
# n2
import re

number = int(input())

for n in range(number):
    string = input()
    if re.search(r'^([a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4}:[a-f0-9]{0,4})$', string):
        print('IPv6')
    elif re.search(r'^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', string):
        print('IPv4')
    else:
        print('Neither')
"""
