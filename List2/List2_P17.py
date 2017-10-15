score = []
id = []
needle = ''

while True:
    value = input().split()

    if len(value) == 1:
        needle = int(value[0])
        break

    id.append(int(value[0]))
    score.append(float(value[1]))

for j in range(len(id)):
    for k in range(len(id) - j - 1):
        if score[k] < score[k + 1]:
            score[k], score[k + 1] = score[k + 1], score[k]
            id[k], id[k + 1] = id[k + 1], id[k]
        elif score[k] == score[k + 1]:
            if id[k] > id[k + 1]:
                score[k], score[k + 1] = score[k + 1], score[k]
                id[k], id[k + 1] = id[k + 1], id[k]

if needle in id:
    print(id.index(needle) + 1)
else:
    print('Not Found')
