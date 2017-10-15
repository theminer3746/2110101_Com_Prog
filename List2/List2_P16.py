row_count, column_count = [int(x) for x in input().split()]

n1 = []
for i in range(row_count):
    n1.append([int(x) for x in input().split()])

n2 = []
for i in range(row_count):
    n2.append([int(x) for x in input().split()])

output = []
for row in range(row_count):
    output.append([])
    for column in range(column_count):
        output[row].append(n1[row][column] + n2[row][column])

for line in output:
    print(*line)
