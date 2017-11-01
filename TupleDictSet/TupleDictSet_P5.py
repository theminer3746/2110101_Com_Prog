data = [int(x) for x in input().split()]
data.sort()

target = int(input())

data_count = {}

for y in data:
    if y in data_count.keys():
        data_count[y] += 1
    else:
        data_count[y] = 1

uniques = sorted(list(set(data)))

counter = 0

for unique in uniques:
    if target - unique in data_count:
        if target - unique != unique:
            counter += data_count[target - unique] * data_count[unique]
        else:
            counter += data_count[target - unique] * (data_count[unique] - 1)

print(int(counter / 2))
