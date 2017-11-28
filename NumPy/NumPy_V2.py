import numpy as np

cost = np.array([int(x) for x in input().strip().split()])

rental = np.array([
    [int(x) for x in input().strip().split()],
    [int(x) for x in input().strip().split()],
    [int(x) for x in input().strip().split()],
    [int(x) for x in input().strip().split()]
])
total_rental = 0
sum_by_day = np.sum(rental, axis=0)

print(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'][np.argmax(sum_by_day)], float(np.max(sum_by_day)))
print(*[float(x) for x in cost.dot(rental)])
