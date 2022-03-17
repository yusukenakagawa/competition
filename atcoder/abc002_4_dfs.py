N, M = map(int, input().split())
acquaintance = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    acquaintance[a - 1][b - 1] = True
    acquaintance[b - 1][a - 1] = True

max_count = 0
v = []
def dfs(v, k = 0):
    global max_count
    if k == N:
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                if not acquaintance[v[i]][v[j]]:
                    return
        max_count = max(max_count, len(v))
    else:
        dfs(v, k + 1)
        v.append(k)
        dfs(v, k + 1)
        v.pop()

dfs(v)
print(max_count)