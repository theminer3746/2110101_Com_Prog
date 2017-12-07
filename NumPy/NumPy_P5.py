import numpy as np
import math


def fib(n, k):
    output = power(np.array([[0, 1], [1, 1]]), n)

    return output[0][1]


result = dict()


def power(matrix, n):
    print('N :', n)
    if n not in result:
        if n == 0:
            result[n] = np.identity(2, dtype=int)
        elif n % 2 == 0:
            result[n] = power(power(matrix, math.floor(n / 2)), 2)
        else:
            result[n] = matrix.dot(power(power(matrix, math.floor(n / 2)), 2))

    return result[n]


n, k = [int(e) for e in input().split()]
print(fib(n, k))

