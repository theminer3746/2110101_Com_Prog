amount = int(input())

words = []
char_set = {}

for i in range(amount):
    current = input().strip().split()

    words.append(current[1])

    if current[1][:2] in char_set:
        char_set[current[1][:2]] += 1
    else:
        char_set[current[1][:2]] = 1

max_freq = []

for item in char_set:
    if char_set[item] == char_set[max(char_set)]:
        max_freq.append(item)

max_freq.sort()

print(max_freq[0])

final = []

for word in words:
    if word[:2] == max_freq[0]:
        final.append(word)

print(len(final))
for item in final:
    print(item)
