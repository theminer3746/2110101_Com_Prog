data = [int(x) for x in input().split()]

data.sort()
counter = {}

for element in data:
    if element in counter.keys():
        counter[element] += 1
    else:
        counter[element] = 1

if 1 in list(counter.values()):
    unique = []

    for key, value in counter.items():
        if value == 1:
            unique.append(key)
    unique.sort()
    print(unique[0])
else:
    print('NONE')
