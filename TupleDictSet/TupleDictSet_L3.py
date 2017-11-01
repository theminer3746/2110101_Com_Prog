file = open(input().strip())
count = dict()
t = 'abcdefghijklmnopqrstuvwxyz0123456789 '
for line in file :
    line_wo_symbols = ''
    for c in line.lower() :
        if c in t : line_wo_symbols += c
    for word in line_wo_symbols.split() :
        if word not in count.keys() :
            count[word] = 1
        else:
            count[word] += 1
file.close()
wordcounts = [(word, count[word]) for word in count.keys()]
wordcounts.sort(key=lambda wordcounts: wordcounts[1], reverse=True)

previous = wordcounts[0][1]
previous_pos = 0
splitted = []

for i in range(1, len(wordcounts)):
    if previous != wordcounts[i][1]:
        splitted.append(wordcounts[previous_pos:i])
        previous_pos = i
        previous = wordcounts[i][1]
splitted.append(wordcounts[previous_pos:])

for i in range(len(splitted)):
    splitted[i].sort()

flatted = [item for sublist in splitted for item in sublist]
print(flatted[:10])
