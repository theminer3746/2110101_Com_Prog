def gcd(x, y):
    if x >= y and x % y == 0:
        return y
    else:
        return gcd(y, x % y)

x, y = [int(h) for h in input().split()]
print(gcd(x, y))
