import math

n = int(input())
x,y = [], []
xy = {}
for _ in range(n):
    tx, ty = map(int, input().split())
    x.append(tx)
    y.append(ty)
    xy[(tx,ty)] = True

max_rect = 0
for i in range(n):
    x1, y1 = x[i], y[i]
    for j in range(i + 1, n):
        x2, y2 = x[j], y[j]
        vector = x2 - x1, y2 - y1
        x3, y3 = x2 + (-vector[1]), y2 + vector[0]
        x4, y4 = x1 + (-vector[1]), y1 + vector[0]
        if (x3,y3) in xy and (x4,y4) in xy:
            max_rect = max(max_rect, (vector[0] ** 2) + (vector[1] ** 2))
print(max_rect)