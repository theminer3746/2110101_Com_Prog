amount = int(input())

counter = {}

for i in range(amount):
    current = int(input())

    if current in counter:
        counter[current] += 1
    else:
        counter[current] = 1

final = []

for number in counter:
    if counter[number] == max(counter.values()):
        final.append(number)

print(sorted(final)[0])
