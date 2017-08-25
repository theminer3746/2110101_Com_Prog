a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

b_acceptable = b[0] - b[1]

if a[1] > b_acceptable:
    a[1] = a[1] - b_acceptable
    b[1] = b[1] + b_acceptable
else:
    b[1] = b[1] + a[1]
    a[1] = 0

print(a[1], b[1])
