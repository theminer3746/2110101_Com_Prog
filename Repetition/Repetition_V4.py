from math import factorial

x = float(input())

cos = 0
k = 0
while True:
    term = (((-1) ** k) * (x ** (2 * k)))/(factorial(2*k))

    if abs(term) < 1e-8:
        break

    k += 1
    cos += term


print(cos, k - 1)
