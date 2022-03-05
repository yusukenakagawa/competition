N = int(input())
S = input()

total = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            string = S
            index = string.find(str(k))
            if index >= 0:
                string = string[index + 1:]
                index = string.find(str(j))
                if index >= 0:
                    string = string[index + 1:]
                    index = string.find(str(i))
                    if index >=0:
                        total += 1
print(total)