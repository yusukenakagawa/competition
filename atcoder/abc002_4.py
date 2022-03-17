N, M = map(int, input().split())
acquaintance = [[False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    acquaintance[a - 1][b - 1] = True
    acquaintance[b - 1][a - 1] = True

max_count = 0
for i in range(1 << N):
    count = 0
    flag = True

    for a in range(N):
        # If the a-th bit is not standing, the number is even. (The rightmost bit does not stand)
        # Examine only the relationship between the members where the bit is standing.
        if (i >> a) % 2 == 0:
            continue
        count += 1

        # See the relationship between 'a' and 'b' in the range to be examined
        for b in range(a+1, N):
            # If the b-th bit is not standing, the number is even. (The rightmost bit does not stand)
            if (i>>b) % 2 == 0:
                continue
            if not acquaintance[a][b]:
                flag = False
    
    if flag:
        max_count = max(max_count, count)

print(max_count)