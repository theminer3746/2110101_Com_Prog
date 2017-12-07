import numpy as np


def fib(n, k):
    output = power(np.array([[0, 1], [1, 1]]), n, k)

    return output[0][1]


result = dict()


def power(matrix, n, k):
    if n not in result:
        if n == 0:
            result[n] = np.identity(2, dtype=int)
        elif n % 2 == 0:
            result[n] = power(matrix, n // 2, k).dot(power(matrix, n // 2, k)) % k
        elif n % 2 == 1:
            result[n] = matrix.dot(power(matrix, n // 2, k).dot(power(matrix, n // 2, k)) % k) % k

    return result[n]


n, k = [int(e) for e in input().split()]
print(fib(n, k))
