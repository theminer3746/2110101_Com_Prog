command, size = [int(x) for x in input().split()]

matrix = []

for i in range(size):
    matrix.append(input().split())

total = 0
if command == 0:
    for row in range(size):
        for column in range(row + 1):
            total += int(matrix[row][column])

else:
    for row in range(size):
        for column in range(row, size):
            total += int(matrix[row][column])

print(total)
