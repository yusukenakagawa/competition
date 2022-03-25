N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

def meguru_bisect(ok, ng, func):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok

def bileft(a, k):
    def is_ok(i):
        if a[i] >= k:
            return True
        else:
            return False
    return meguru_bisect(len(a), -1, is_ok)

def biright(a, k):
    def is_ok(i):
        if a[i] > k:
            return True
        else:
            return False
    return meguru_bisect(len(a), -1, is_ok)


count = 0
for i in range(N):
    A_boundary = bileft(A, B[i])
    C_boundary = biright(C, B[i])
    count = count + (A_boundary  * (N - (C_boundary)))

print(count)