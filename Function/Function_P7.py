import math

def f(x):
    k = 0
    for i in range(1,2*x,2):
        k += i
    for j in range(k):
        if j%x==0:
            k += 2
    return k+3

def partial_target(x):
    return x - a_n(1) + b_n(1) - 2

def factor_n(target):
    candidate = math.ceil(math.sqrt(target))

    n = candidate
    while True:
        if n * (n + 2) > target:
            n -= 1
        elif n * (n + 2) < target:
            n += 1
        else:
            pass
        return int(n)

def f_inv(x):
    pt = partial_target(x)
    n = factor_n(pt)
    return n

def a_n(n):
    return 6 + ((n - 1) * (b_n(1) + b_n(n - 1)) / 2)

def b_n(n):
    return 5 + ((n - 1) * 2)

print(eval(input().strip()))
