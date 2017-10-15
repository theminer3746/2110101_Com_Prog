from math import ceil, floor

amount = int(input())

data = []

for i in range(amount):
    data.append(int(input()))

data.sort()

avg = sum(data) / len(data)

if (len(data) + 1) % 2 == 0:
    median = data[int((len(data) + 1) / 2) - 1]
else:
    median = (data[int(ceil((len(data) + 1) / 2)) - 1] + data[int(floor((len(data) + 1) / 2)) - 1]) / 2

in_list = []
frequency = []

for bit in data:
    if bit not in in_list:
        in_list.append(bit)
        frequency.append(1)
    else:
        index = in_list.index(bit)
        frequency[index] += 1
mode = in_list[frequency.index(max(frequency))]

print(avg, median, mode)
