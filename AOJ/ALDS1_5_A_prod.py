from itertools import product

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
m_dict = {}

for i in range(q):
    m_dict[m[i]] = False

for prod in product((0,1), repeat=n):
    total = 0
    for j in range(n):
        if prod[j] == 1:
            total += A[j]
    if total in m_dict:
        m_dict[total] = True

for i in range(q):
    print("yes" if m_dict[m[i]] else "no")
        