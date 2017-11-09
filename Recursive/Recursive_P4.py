from math import floor

def value(a, k, m):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return (((a ** floor(k / 2)) % m) ** 2) % m
    else:
        return (a * (((a ** floor(k / 2)) % m) ** 2)) % m

a, k, m = [int(x) for x in input().split()]

print(value(a, k, m))
