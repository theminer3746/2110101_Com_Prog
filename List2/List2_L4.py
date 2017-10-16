file = open('inventory.txt')

inventory = []
for line in file:
    current = line.strip().split(';')
    if current != []:
        inventory.append([current[0], current[1], int(current[2])])

file.close()

while True:
    command = input().strip().split()

    if command[0] == 'Q':
        print('Bye!')
        break

    found = False
    for i in range(len(inventory)):
        if inventory[i][0] == command[1]:
            found = True
            key = i
            break

    if command[0] == 'T':
        if found:
            inventory[key][2] += int(command[2])
            print(inventory[key])
        else:
            print('Product code does not exist.')
    elif command[0] == 'U':
        if found:
            inventory[key][2] = int(command[2])
            print(inventory[key])
        else:
            print('Product code does not exist.')
    elif command[0] == 'A':
        if found:
            print('Duplicate product code.')
        else:
            inventory.append([command[1], command[2], int(command[3])])
            print(inventory[-1])
    elif command[0] == 'D':
        if found:
            inventory.pop(key)
            print(command[1], 'deleted')
        else:
            print('Product code does not exist.')
