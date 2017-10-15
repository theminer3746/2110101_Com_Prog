d = [int(x) for x in input().split()]
n = len(d)
for k in range(n-1):
    for i in range(n-1):
        if d[i] > d[i+1]:
            d[i],d[i+1] = d[i+1],d[i]

if n % 2 == 0:
    print(float((d[int(n / 2)] + d[int(n / 2) - 1]) / 2))
else:
    print(float(d[(n // 2)]))
