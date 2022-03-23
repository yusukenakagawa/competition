d = int(input()) # 環状線の長さ
n = int(input()) # 店舗の数
m = int(input()) # 注文の数
S = [0] # 本店の位置は0
for _ in range(n - 1):
    S.append(int(input()))
S.append(d) # ダミーの本店を最後に入れておく。
S.sort()
n = n + 1
K = [] # 注文の位置
for _ in range(m):
    K.append(int(input()))


total_distance = 0
for i in range(m):
    L = 0
    R = n - 1
    M = (L + R) // 2
    while L <= R:
        if S[M] == K[i]:
            total_distance += abs(K[i] - S[M])
            break

        if S[M] > K[i]:
            R = M - 1
        else:
            L = M + 1

        M = (L + R) // 2
    else:
        total_distance += min( K[i] - S[M], S[M + 1] - K[i])


print(total_distance)