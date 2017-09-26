filename = input().strip()
target_line_count = int(input())

file = open(filename, 'r')
data = file.readlines()
file.close()

max_line_count = min(len(data), target_line_count + 1)

for i in range(len(data)):
    if ';Failure' in data[i]:
        output = list()
        for j in range(0, max_line_count):
            if i - j >= 0:
                to_append = data[i - j].split(';')[1] + ';' + data[i - j].split(';')[2]
                output.append(to_append)

        output.reverse()

        for line in output:
            print(line, end='')

        break
else:
    print('Not Found')
