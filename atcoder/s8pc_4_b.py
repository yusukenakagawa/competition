N, K = map(int, input().split())
a = list(map(int, input().split()))

min_cost = 10 ** 23
for bit in range(1 << N):
    # First building does not need to be changed
    if bit & 1:
        continue

    tmp_a = a.copy()
    max_height = tmp_a[0]
    cost = 0
    color_variation = 1

    for i in range(N):
        # if color_variation >= K:
        #     break
        if bit & (1 << i):
            if max_height >= tmp_a[i]:
                cost += max_height - tmp_a[i] + 1
                tmp_a[i] = max_height + 1

            color_variation += 1

        if max_height < tmp_a[i]:
            max_height = tmp_a[i]

    if color_variation >= K:
        min_cost = min(min_cost, cost)

print(min_cost)