data = []
frequency = []

while True:
    current = int(input())

    if current == -1:
        break

    if current not in data:
        data.append(current)
        frequency.append(1)
    else:
        index = data.index(current)
        frequency[index] += 1

if max(frequency) > sum(frequency) / 2:
    print(data[frequency.index(max(frequency))])
else:
    print('Not found ')
