data = [int(x) for x in input().split()]
target = int(input())

counter = 0

for i in range(len(data) - 1):
    for j in [y for y in range(i, len(data)) if y != i]:
        if data[i] + data[j] == target:
            counter += 1

print(counter)
