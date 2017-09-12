filename = input().strip()
n1, n2, n3 = [input().strip() for x in range(0, 3)]

n1_count, n2_count, n3_count = 0, 0, 0

file = open(filename, 'r')
data = file.read()
file.close()

n1_count = data.count(n1)
n2_count = data.count(n2)
n3_count = data.count(n3)

if n1_count == max(n1_count, n2_count, n3_count):
    if n2_count >= n3_count:
        print(n1 + n2 + n3)
    else:
        print(n1 + n3 + n2)
elif n2_count == max(n1_count, n2_count, n3_count):
    if n1_count >= n3_count:
        print(n2 + n1 + n3)
    else:
        print(n2 + n3 + n1)
else: #n3 is the max
    if n1_count >= n2_count:
        print(n3 + n1 + n2)
    else:
        print(n3 + n2 + n1)
