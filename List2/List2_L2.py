s = input()
x = [int(x) for x in s.split()]

k = 0
while k < len(x) - 1:
    minIdx = k
    minVal = x[k]
    i = k

    while i < len(x):
        if x[i] < minVal:
            minIdx = i
            minVal = x[i]
        i += 1

    x[k], x[minIdx] = x[minIdx], x[k]
    k += 1

print(x)
