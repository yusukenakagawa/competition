from bisect import bisect_left, bisect_right

N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))

count = 0
for i in range(N):
    A_boundary = bisect_left(A, B[i])
    C_boundary = bisect_right(C, B[i])
    count = count + (A_boundary  * (N - (C_boundary)))

print(count)