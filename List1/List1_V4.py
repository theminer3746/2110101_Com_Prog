filename = input().strip()

file = open(filename, 'r')

output = []
fruits = []

for line in file:
    if line.strip() == '':
        continue

    data = line.strip().split()

    if data[0] not in fruits:
        output.append([data[0], [data[1]]])
        fruits.append(data[0])
    else:
        output[fruits.index(data[0])][1].append(data[1])

file.close()

maximum = 0
max_fruit = ''
for i in range(len(output)):
    if max(maximum, len(output[i][1])) > maximum:
        maximum = max(maximum, len(output[i][1]))

        max_fruit = output[i][0]

print(output)
print('The most favorite fruit is', max_fruit)
