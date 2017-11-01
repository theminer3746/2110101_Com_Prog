file = open('address.txt')

addr = {}
for line in file:
    data = line.strip().split()
    addr[(data[0], data[1])] = (data[2], data[3])
file.close()

while True:
    needle = input().strip()
    if needle == '':
        break

    fname, lname = needle.split()

    if (fname, lname) in addr:
        print(*addr[(fname, lname)])
    else:
        print('Not found')
