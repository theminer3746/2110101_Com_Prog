row = int(input())
column = int(input())

data = []

for x in range(row):
    data.append([int(k) for k in input().split()])

found = False
for n1 in range(row):
    for n2 in range(n1 + 1, row):
        for j in range(column):
            if data[n1][j] != data[n2][j]:
                break
        else:
            found = True

        if found:
            break

    if found:
        break

print(n1 + 1)
print(*data[n1])
print(n2 + 1)
print(*data[n2])
