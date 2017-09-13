filename = input().strip()

file = open(filename, 'r')

search_type = file.readline().strip()
needle = file.readline().strip()

for line in file:
    data = line.split()
    if search_type == 'find':
        found_pos = data[0].find(needle, int(data[1]), int(data[2]))
        #print('HERE', found_pos)
    else:
        found_pos = data[0].rfind(needle, int(data[1]), int(data[2]))
        #print('here', found_pos)

    if found_pos != -1:
        if found_pos == 0:
            print(data[0][0:len(needle) + 1])
        else:
            print(data[0][found_pos - 1 : found_pos + len(needle) + 1])
    else:
        print('not found')
