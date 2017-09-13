filename = input().strip()

file = open(filename, 'r')

count = 0
for line in file:
    if line.strip() == '':
        count += 1

file.close()

print(count)
