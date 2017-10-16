data = [int(x) for x in input().split()]

for i in range(len(data)):
    if data[i] % 2 == 0:
        data[i] = 0
    else:
        data[i] = 1

print(data)
print(sum(data))
