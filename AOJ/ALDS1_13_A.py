from copy import deepcopy

k = int(input())
r, c = [0] * k, [0] * k
b = [['.'] * 8 for _ in range(8)]
for i in range(k):
    r[i], c[i] = map(int, input().split())
    b[r[i]][c[i]] = 'Q'

moves = ((0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1))

def check_board(b, q_x, q_y):
    b[q_y][q_x] = 'Q'
    for j in range(1, 8):
        for m in moves:
            x = q_x + (m[0] * j)
            y = q_y + (m[1] * j)
            if x < 0 or x >= 8 or y < 0 or y >= 8:
                continue

            if b[y][x] == 'Q':
                continue

            b[y][x] = 'f'
    return b

for i in range(k):
    b = check_board(b, c[i], r[i])

result = deepcopy(b)

def dfs(b, x, y):
    global result 

    if not '.' in b[y][x]:
        return

    b = check_board(b, x, y)

    count = 0
    for i in range(8):
        count += b[i].count('Q')
    if count == 8:
        result = b

    for i in range(y + 1, 8):
        if "Q" in b[i]:
            continue
        for j in range(8):
            dfs(deepcopy(b), j, i)

# decision start point
for y in range(8):
    if not "Q" in b[y]:
        break

for j in range(8):
    if b[y][j] != '.':
        continue
    dfs(deepcopy(b), j, y)

for s in result:
    s = "".join(s)
    print(s.replace('f','.'))