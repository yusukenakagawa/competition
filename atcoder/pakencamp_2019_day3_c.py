N, M = map(int, input().split())
A = []

for _ in range(N):
    A.append(list(map(int, input().split())))

score =  0
for i in range(M):
    for j in range(i + 1, M):
        s = 0
        for k in range(N):
            s += max(A[k][i], A[k][j])

        score = max(score, s)

print(score)