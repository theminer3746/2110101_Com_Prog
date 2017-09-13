file = open(input().strip())
c_sum = 0
for line in file:
    for c in line:
        c_sum = c_sum ^ ord(c)

file.close()
print(c_sum)
