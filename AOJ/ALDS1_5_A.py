n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
m_dict = {}

for i in range(q):
    m_dict[m[i]] = False


def nest(begin, num):
    global m_dict
    if num in m_dict:
        m_dict[num] = True
    if begin == n:
        return

    for i in range(begin, n):
        nest(i + 1, num + A[i])

for i in range(n):
    num = A[i]
    nest(i + 1, num)
        
for i in range(q):
    print("yes" if m_dict[m[i]] else "no")
