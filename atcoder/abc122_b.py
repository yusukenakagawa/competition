S = input()

pattern = ['A','T','G','C']

count = 0
max = 0
for i in range(len(S)):
    if S[i] in pattern:
        count += 1
    else:
        count = 0
    if max < count:
        max = count

print(max)
