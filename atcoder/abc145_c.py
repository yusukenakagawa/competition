import math

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())

distances = []

def bfs(n):

    if len(n) == N:
        d = 0
        for k in range(N - 1):
            d += math.sqrt(((x[n[k]] - x[n[k + 1]]) ** 2) + ((y[n[k]] - y[n[k + 1]]) ** 2))
        distances.append(d)
        return

    for j in range(N):
        if not j in n:
            bfs(n + [j])


for i in range(N):
    bfs([i])

print(sum(distances) / len(distances))