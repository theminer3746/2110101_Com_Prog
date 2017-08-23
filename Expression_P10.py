from math import ceil

input = input()

sum = 0
for i in range(0, 9):
    sum += (10 - i) * int(input[i])

checksum = (ceil(sum/11) * 11) - sum


print(input + str(checksum))
