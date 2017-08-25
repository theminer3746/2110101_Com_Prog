import math

length = [int(x) for x in input().split()]

p = (length[0] + length[1] + length[2])/2

area = math.sqrt(p * (p-length[0]) * (p-length[1]) * (p-length[2]))
print(area)
