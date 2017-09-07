commands = input().strip()

x_pos = 0
y_pos = 0

for command in commands:
    if command == 'U':
        y_pos += 1
    elif command == 'R':
        x_pos += 1
    elif command == 'D' and y_pos - 1 >= 0:
        y_pos -= 1
    elif command == 'L' and x_pos - 1 >= 0:
        x_pos -= 1

print('(' + str(x_pos) + ',' + str(y_pos) + ')')
