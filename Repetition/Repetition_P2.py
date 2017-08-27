from math import factorial

n, r, option = [int(x) for x in input().split()]

result = factorial(n)/factorial(n - r)

if option == 2:
    result /= factorial(r)

print(int(result))
