from math import atan, degrees

ab, bc = int(input()), int(input())
angle = degrees(atan(ab / bc))
print(str(round(angle))+chr(176))

"""
INPUT:
1
10

OUTPUT:
6°
"""