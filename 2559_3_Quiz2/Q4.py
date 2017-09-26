command = input().strip()
amount = int(input())

data = list()

for x in range(amount):
    data.append(input().strip())

previous_length = len(data[0])
for line in data:
    if len(line) != previous_length:
        print('Invalid size')
        break
else:
    if command == 'flip':
        for line in data:
            print(line[::-1])
    elif command == '90':
        for char_count in range(len(data[0])):
            for line_number in range(len(data) - 1, -1, -1):
                print(data[line_number][char_count], end='')

            print('')
    elif command == '180':
        for line_number in range(len(data) - 1, -1, -1):
            for char_count in range(len(data[0]) - 1, -1, -1):
                print(data[line_number][char_count], end='')

            print('')
