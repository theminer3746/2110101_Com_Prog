amount = int(input())

suggestions = []

for i in range(amount):
    suggestions.append(set(input().strip().split()))

needle = input().strip()

frequency = {}

found = False

for suggestion in suggestions:
    if needle in suggestion:
        if not found:
            found = True

        for data in suggestion:
            if data != needle:
                if data in frequency:
                    frequency[data] += 1
                else:
                    frequency[data] = 1

frequency = list(frequency.items())
frequency = sorted(frequency, key= lambda frequency:frequency[1])

if not found:
    print('Not Found')
elif len(frequency) == 0:
    print('No suggested event')
else:
    previous = 0
    ordered = []
    for item in frequency:
        if item[1] > previous:
            previous = item[1]

            ordered.append(([item[0]], item[1]))
        else:
            ordered[-1][0].append(item[0])

            ordered[-1][0].sort()

    ordered.reverse()

    for chunk in ordered:
        current = chunk[1]
        for item in chunk[0]:
            print(item, current)
