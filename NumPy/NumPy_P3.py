import numpy as np

amount = int(input())

output = []

for i in range(amount):
    splitted = input().strip().split(',')

    if len(splitted) == 1:
        continue

    if 1 <= len(splitted[1]) <= 2:
        output.append(sum([float(x) for x in splitted[1:]]))

for item in output:
        print(item)
