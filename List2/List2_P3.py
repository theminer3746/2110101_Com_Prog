file = open('score.txt')

id = []
score = []

for line in file:
    line = line.strip().split()
    id.append(int(line[0]))
    score.append(int(line[1]))

file.close()

while True:
    needle = int(input().strip())

    if needle == -1:
        break

    if needle not in id:
        print('Not Found')
    else:
        index = id.index(needle)
        print(score[index])
