def compare(a, b):
    if b[1] > a[1]:
        return True
    elif b[1] == a[1]:
        return b[0] < a[0]
    else:
        return False

n = int(input().strip())
d = []
for i in range(n):
    x, y = input().strip().split()
    d.append((x, float(y)))

for k in range(n-1):
    for i in range(n-1):
        if compare(d[i], d[i+1]):
            d[i], d[i+1] = d[i+1], d[i]

for i in d:
    print(i[0], i[1])
