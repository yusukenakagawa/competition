n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
m_dict = {}

for i in range(q):
    m_dict[m[i]] = False

for bit in range(1 << n):
    total = 0
    for i in range(n):
        if (bit & (1 << i)):
            total += A[i]
    if total in m_dict:
        m_dict[total] = True

for i in range(q):
    print("yes" if m_dict[m[i]] else "no")
        