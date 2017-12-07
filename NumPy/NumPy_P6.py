import numpy as np


def scale(img, c) :
    total = 0.0
    for row in range(c):
        total += np.sum(img[row, ::c])
    return img[::c, ::c] #+ img[1::c]


def read_img():
    row, col = [int(e) for e in input().split()]
    img = np.ndarray((row,col))
    for i in range(row):
        img[i] = [float(e) for e in input().split()]
    return img


def show_output(out):
    for i in range(out.shape[0]):
        print(" ".join([str(e) for e in out[i]]))

img = read_img()
c = int(input())
out = scale(img, c)
show_output(out)
