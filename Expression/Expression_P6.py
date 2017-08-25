import numpy as np

L1 = input().split()
L2 = input().split()

A = np.matrix([[float(L1[0]), float(L1[1])], [float(L2[0]), float(L2[1])]])

L1[2] = -float(L1[2])
L2[2] = -float(L2[2])
B = np.matrix([[L1[2]], [L2[2]]])

R = A.I * B

print(str(R.getA()[0][0]) + ' ' + str(R.getA()[1][0]))
