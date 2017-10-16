size = int(input())

data = []

for row in range(size):
    data.append([int(k) for k in input().split()])

for y in range(size):
    sum_y = 0
    for y_up_down in range(size):
        sum_y += data[y_up_down][y]

    if sum(data[y]) == 1 and sum_y == size:
        break
else:
    y = -1

print(y)
