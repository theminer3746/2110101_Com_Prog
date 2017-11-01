input()

data = [int(x) for x in input().split()]
targets = [int(x) for x in input().split()]

uniques = list(set(data))

possible = set()
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        possible.add(data[i] + data[j])

for target in targets:
    found = False

    modified_data = [target - x for x in data]

    for i in range(len(modified_data)):
        partial_target = modified_data[i]
        if partial_target in possible:
            print('YES')
            found = True
            break

    if not found:
        print('NO')
