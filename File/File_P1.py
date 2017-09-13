filename = input().strip()

file = open(filename, 'r')

for line in file:
    data = line.split()

    total = 0
    for i in range(1, len(data)):
        total += int(data[i])

    if 100 >= total >= 80:
        print(data[0], 'A')
    elif 79 >= total >= 75:
        print(data[0], 'B+')
    elif 74 >= total >= 70:
        print(data[0], 'B')
    elif 69 >= total >= 65:
        print(data[0], 'C+')
    elif 64 >= total >= 60:
        print(data[0], 'C')
    elif 59 >= total >= 55:
        print(data[0], 'D+')
    elif 54 >= total >= 50:
        print(data[0], 'D')
    else:
        print(data[0], 'F')

file.close()
