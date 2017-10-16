line = input().strip()
amount = int(input())

line = [line[i:i+1] for i in range(len(line))]

for i in range(amount):
    command = input().split()

    if command[0] == 'in':
        line.insert(int(command[2]), command[1])
    elif command[0] == 'out':
        line.pop(int(command[1]))
    elif command[0] == 'swap':
        line[int(command[1])], line[int(command[2])] = line[int(command[2])], line[int(command[1])]

    print(''.join(line))
