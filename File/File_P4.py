filename = input().strip()

file = open(filename, 'r')

BE = 0
SE = 0
VE = 0
ET = 0

for line in file:
    food_type = line.split()[0]

    if food_type.upper() == 'BE':
        BE += 1
    elif food_type.upper() == 'SE':
        SE += 1
    elif food_type.upper() == 'VE':
        VE += 1
    elif food_type.upper() == 'ET':
        ET += 1

print(BE, SE, VE, ET, sum([BE, SE, VE, ET]))
