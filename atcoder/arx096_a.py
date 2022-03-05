A, B, C, X, Y = map(int, input().split())

x = 0
y = 0
cost = 0
while True:
    if X <= x and Y <= y:
        break

    if (X > x and A >= C * 2) or (Y > y and B >= C * 2):
        x += 1
        y += 1
        cost += C * 2
        continue
    if X > x and Y > y and A + B > C * 2:
        x += 1
        y += 1
        cost += C * 2
        continue
    if X > x:
        x += 1
        cost += A
    if Y > y:
        y += 1
        cost += B

print(cost)