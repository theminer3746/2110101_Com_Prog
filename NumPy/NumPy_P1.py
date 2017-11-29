import numpy as np

data = np.array([
    [15, 3.78],
    [29, 2.0],
    [10, 2.5],
    [25, 2.85],
    [30, 3.96]
])

logit_pi = - 3.98 + .2 * data[:, 0] + 0.5 * data[:, 1]
p_xi = 1/(1 + np.exp(-logit_pi))

n = int(input())

if 1 > n or n > len(data):
    print('Error')
elif p_xi[n - 1] > 0.5:
    print('True')
else:
    print('False')
