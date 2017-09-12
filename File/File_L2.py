file = open('data.txt', 'r')

section = input()

n = 0
sum = 0

for line in file:
    data = line.split(':')

    if data[2] == section:
        n += 1
        sum += float(data[3])

file.close()

if n > 0:
    print(sum / n)
else:
    print('Not Found')
