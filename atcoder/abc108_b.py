x1, y1, x2, y2 = map(int, input().split())

vector = x2 - x1, y2 - y1

x3 = x2 + (-vector[1])
y3 = y2 + vector[0]

x4 = x1 + (-vector[1])
y4 = y1 + vector[0]

print(x3, y3, x4, y4)