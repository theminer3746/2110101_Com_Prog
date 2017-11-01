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
frequency = sorted(frequency, key= lambda frequency:frequency[1], reverse=True)

if not found:
    print('Not Found')
elif len(frequency) == 0:
    print('No suggested event')
else:
    max_freq = []
    max_freq_in_number = max(frequency, key=lambda frequency:frequency[1])[1]

    for item in frequency:
        if item[1] == max_freq_in_number:
            max_freq.append(item[0])

    max_freq.sort()

    print(max_freq[0])
    print(max_freq_in_number)
