row, column = [int(k) for k in input().split()]

data = []

for i in range(row):
    data.append([int(n) for n in input().strip().split()])

found = False

for y_pos in range(row):
    x_pos = data[y_pos].index(min(data[y_pos]))
    for y_up_down in [m for m in range(row) if m != y_pos]:
        if data[y_up_down][x_pos] > data[y_pos][x_pos]:
            break
    else:
        found = True
        break

if found:
    print(data[y_pos][x_pos])
else:
    print(-1)
