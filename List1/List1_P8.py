target = int(input())

li = list()

for x in range(1, target + 1):
    li.append(x)

while True:
    val1, val2 = [int(x) for x in input().split()]

    if val1 == val2 == 0:
        break

    pos1 = li.index(val1)
    pos2 = li.index(val2)

    li[pos1] = val2
    li[pos2] = val1

print(li)
