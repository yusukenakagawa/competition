m = int(input())
mx, my = [], []
mxy = {}
for i in range(m):
    x, y = map(int, input().split())
    mxy[(x,y)] = True
n = int(input())
mxy = dict(sorted(mxy.items(), key=lambda x:x[0])) # sort by x
for key in mxy:
    x,y = key
    mx.append(x)
    my.append(y)

nx, ny = [], []
nxy = {}
for i in range(n):
    x, y = map(int, input().split())
    nx.append(x)
    ny.append(y)
    nxy[(x,y)] = True
nxy = dict(sorted(nxy.items(), key=lambda x:x[0])) # sort by x
for key in nxy:
    x,y = key
    nx.append(x)
    ny.append(y)

correct_diff = []
x1, y1 = mx[0], my[0]
x2, y2 = mx[1], my[1]
vec1 = x2 - x1, y2 - y1
diff = []
for k in range(n):
    tx1, ty1 = nx[k], ny[k]
    if (tx1 + vec1[0], ty1 + vec1[1]) in nxy:
        diff = tx1 - x1, ty1 - y1
        is_match = True
        for l in range(m):
            if (mx[l] + diff[0], my[l] + diff[1]) not in nxy:
                is_match = False
        if is_match:
            correct_diff = diff
            break
print(f"{correct_diff[0]} {correct_diff[1]}")