w = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]
W = int(input())

def KS(i, w, v, x):
    if i < 0:
        return 0
    elif x >= w[i]:
        return max(KS(i - 1, w, v, x), KS(i - 1, w, v, x - w[i]) + v[i])
    else:
        return KS(i - 1, w, v, x)

print(KS(len(w) - 1, w, v, W))
