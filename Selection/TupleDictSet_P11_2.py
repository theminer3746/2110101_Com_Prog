amount = int(input())

suggestions = []

for i in range(amount):
    suggestions.append(sorted(set(input().split())))

#print(suggestions)

needle = input().strip()

duplicate = {}

for suggestion in suggestions:
    #print(suggestion)
    if needle in suggestion:
        for data in suggestion:
            if data != needle:
                if data in duplicate:
                    duplicate[data] += 1
                else:
                    duplicate[data] = 1

print(duplicate)

duplicate = duplicate.items()

#print(sorted(duplicate, key=duplicate.items()))

print(sorted(duplicate, key=lambda duplicate:duplicate[1], reverse=True))
