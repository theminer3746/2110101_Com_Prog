file = open('address.txt')
address = {}

for line in file:
    line = line.strip().split()

    address[(line[0], line[1])] = line[2]
file.close()

while True:
    needle = input().strip()

    if needle == '':
        break

    if needle.isnumeric():
        for key in address:
            if address[key] == needle:
                print(*key)
                break
        else:
            print('Not Found')
    else:
        needle = needle.split()
        if (needle[0], needle[1]) in address:
            print(address[(needle[0], needle[1])])
        else:
            print('Not Found')
