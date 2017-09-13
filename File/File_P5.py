filename1 = input().strip()
filename2 = input().strip()

file1 = open(filename1, 'r')
file2 = open(filename2, 'r')

data1 = file1.readlines()
data2 = file2.readlines()

file1.close()
file2.close()

for i in range(len(data1)):
    if data2[i].strip() in data1[i].strip():
        print('True')
    else:
        print('False')
