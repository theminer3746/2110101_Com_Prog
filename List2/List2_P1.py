data = input().strip()

counter = [0] * 10

for number in data:
    counter[int(number)] += 1

for c in counter:
    print(c)
