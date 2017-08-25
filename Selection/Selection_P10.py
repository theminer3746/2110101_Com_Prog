from math import floor

d, m, y = [int(x) for x in input().split()]

if m < 3:
    m = m +12
    y = y - 1

c = floor(y / 100)
k = y % 100
w = (d + floor(26 * (m + 1) / 10) + k + floor(k / 4) + floor(c / 4) + 5 * c) % 7

if w == 0:
    print('SAT')
elif w == 1:
    print('SUN')
elif w == 2:
    print('MON')
elif w == 3:
    print('TUE')
elif w == 4:
    print('WED')
elif w == 5:
    print('THU')
elif w == 6:
    print('FRI')
