n = int(input())
for x in range(n):
    px, py, qx, qy = map(int, input().split())
    dx = qx - px
    dy = qy - py
    print(qx + dx, qy + dy)
