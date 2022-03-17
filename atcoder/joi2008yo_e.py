R, C = map(int, input().split())
A = []
for _ in range(R):
    A.append(list(map(int, input().split())))

max_count = 0
for i in range(1 << (R - 1)):
    tmp_A = A.copy()
    for bit in range(i):
        if i >> bit & 1:
            tmp_A[bit] = list(map(lambda x:0 if x else 1,tmp_A[bit]))


    count = 0
    for j in range(C):
        head = 0
        tail = 0
        for k in range(R):
            if tmp_A[k][j]:
                head += 1
            else:
                tail += 1
        if head >= tail:
            count += head
        else:
            count += tail
    
    max_count = max(max_count, count)

print(max_count)