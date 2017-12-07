import numpy as np


def fib(n, k):
    output = np.array([[0, 1], [1, 1]])

    if n == 0:
        return 0

    for i in range(n - 1):
        output = np.dot(np.array([[0, 1], [1, 1]]), output) % k

    return output[0][1]


n, k = [int(e) for e in input().split()]
print(fib(n, k))

