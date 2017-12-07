import numpy as np


amount = int(input())

prep = []

for i in range(amount):
    prep.append([int(x) for x in input().strip().split()])

A = np.array(prep)


def get_A(n):
    output = A.copy()
    for i in range(2, n):
        output += power(A.copy(), i)

    return output


def power(matrix, n):
    output = matrix.copy()
    for i in range(1, n):
        output = output.dot(matrix.copy())

    return output


B = np.sign(get_A(amount))

for row in B:
    print(*row)
