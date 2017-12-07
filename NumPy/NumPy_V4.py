import numpy as np


def read_square_matrix():
    d = [int(e) for e in input().split()]
    m = [d]
    for k in range(len(d)-1):
        m.append([int(e) for e in input().split()])
    return np.array(m)


def min_in_each_row(m):
    return np.min(m, axis=1)


def max_in_each_column(m):
    return np.max(m, axis=0)


def diff_of_sums_of_two_diags(m):
    return abs(np.sum(m.diagonal()) - np.sum(np.fliplr(m).diagonal()))


def halve(m):
    return m[::2, ::2] + m[::2, 1::2] + m[1::2, ::2] + m[1::2, 1::2]


exec(input().strip()) # do not remove this line
