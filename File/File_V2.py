f = open('data.txt', 'r')

n = int(input())

i = 0
found = False
while True:
    line = f.readline()

    if line == '':
        break

    if 'Name:' in line:
        i += 1

        if i == n:
            print(line[6:])
            found = True

if not found:
    print('Not Found')
