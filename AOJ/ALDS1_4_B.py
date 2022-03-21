n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0
for t in T:
    L = 0
    R = n - 1
    M = (R + L) // 2

    while L <= R:
        if S[M] == t:
            count += 1
            break

        if S[M] > t:
            R = M - 1
        else:
            L = M + 1
        
        M = (R + L) // 2

print(count)