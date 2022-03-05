N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())


min_time = 2**63-1
for i in range(N):
    entrance = A[i]
    for j in range(N):
        exit = B[j]
        time = 0
        for k in range(N):
            time += abs(entrance - A[k]) + abs(A[k] - B[k]) + abs(B[k] - exit)
        min_time = min(min_time, time)
print(min_time)