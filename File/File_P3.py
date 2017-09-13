file = open('score.txt', 'r')

id = input().strip()

for line in file:
    data = line.split()

    found = False
    if data[0] == id:
        print(data[1])
        found = True
        break

if not found:
    print('Not Found')
