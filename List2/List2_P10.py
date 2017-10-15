amount = int(input())
data = []

for i in range(amount):
    data.append(input().strip())

count = 0
for j in range(amount):
    for k in range(amount - j - 1):
        if len(data[k]) > len(data[k + 1]):
            data[k], data[k + 1] = data[k + 1], data[k]
            count += 1
        elif len(data[k]) == len(data[k + 1]) and data[k] > data[k + 1]:
            data[k], data[k + 1] = data[k + 1], data[k]
            count += 1

for bit in data:
    print(bit)
print(count)
