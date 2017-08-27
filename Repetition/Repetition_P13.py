row, column = [int(x) for x in input().split()]

for i in range(1, row + 1):
    data_in_this_row = ''
    for j in range(1, column + 1):
        data_in_this_row = data_in_this_row + str(i * j) + ' '
    print(data_in_this_row.strip())
