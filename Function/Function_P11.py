from math import sqrt

def zscore(L):
    output = []
    for value in L:
        output.append((value - mean(L)) / sd(L))

    return output

def mean(L):
    return sum(L) / len(L)

def sd(L):
    total = 0
    for value in L:
        total += (value - mean(L)) ** 2

    total /= len(L)

    return sqrt(total)

L = [float(e) for e in input().split()]
for i in zscore(L):
    print(i)
