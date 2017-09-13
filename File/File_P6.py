filename1 = input().strip()
filename2 = input().strip()

file1 = open(filename1, 'r')
file2 = open(filename2, 'r')

for line in file1:
    total = 0
    count = 0
    for i in range(0, int(line)):
        total += float(file2.readline())
        count += 1

    print(total / count)

file1.close()
file2.close()
