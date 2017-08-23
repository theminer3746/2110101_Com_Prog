import math

a = input()
b = input()
D = input()

C = math.radians(float(D))

area = 0.5 * float(a) * float(b) * math.sin(C)
print('area = ' + str(area) + ' (sq cm)')