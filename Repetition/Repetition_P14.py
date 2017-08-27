matrix_size, target_shape = [int(x) for x in input().split()]

output = list()

if target_shape == 1:
    for x in range(1, matrix_size + 1):
        for y in range(x, matrix_size + 1):
            output.append('(' + str(x) + ',' + str(y) + ')')
elif target_shape == 2:
    for x in range(1, matrix_size + 1):
        for y in range(1, x + 1):
            output.append('(' + str(x) + ',' + str(y) + ')')
elif target_shape == 3:
    for x in range(1, matrix_size + 1):
        output.append('(' + str(x) + ',' + str(matrix_size - x + 1) + ')')

for i in range(0, len(output)):
    print(output[i])
