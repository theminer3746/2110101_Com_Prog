amount = int(input())

words = []

for x in range(amount):
    words.append(input().strip())

chars = 'abcdefghijklmnopqrstuvwxyz'

scores = []

for word in words:
    current = []
    for y in range(len(chars)):
        current.append(word.count(chars[y]))

    scores.append(current)

for i in range(amount):
    for j in range(amount - i - 1):
        for k in range(len(chars)):
            if scores[j][k] > scores[j + 1][k]:
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
                words[j], words[j + 1] = words[j + 1], words[j]
                break
            elif scores[j][k] < scores[j + 1][k]:
                break
        else:
            if sum(scores[j]) == sum(scores[j + 1]) and words[j] > words[j + 1]:
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
                words[j], words[j + 1] = words[j + 1], words[j]

print(*words)
