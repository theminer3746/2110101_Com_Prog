import re

regex = re.compile("[\'\"\-\.\(\)\,]+")

file1 = open('file1.txt')

a = set()

for line in file1:
    line = regex.sub(' ', line)
    line = line.lower()

    a.update(line.split())

file1.close()

file2 = open('file2.txt')

b = set()

for line in file2:
    line = regex.sub(' ', line)
    line = line.lower()

    b.update(line.split())

needle = input().strip()

if needle in a and needle in b:
    print("Found in both files")
elif needle in a:
    print("Found in file1 only")
elif needle in b:
    print("Found in file2 only")
else:
    print('Not found')
