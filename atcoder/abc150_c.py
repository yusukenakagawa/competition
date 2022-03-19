N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
p, q = 0, 0
count = 0

def bfs(n):
    global p, q, count
    if len(n) == N:
        count += 1
        if P == n:
            p =  count
        if Q == n:
            q =  count
        return
    for i in range(N):
        if i + 1 in n:
            continue
        bfs(n + [i + 1])
        
for i in range(N):
    bfs([i + 1])

print(abs(p - q))