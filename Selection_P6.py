L1 = [int(x) for x in input().split()]
L2 = [int(x) for x in input().split()]

if L1[1] != 0:
    L1_slope = L1[0] / L1[1]
else:
    L1_slope = 'inf'

if L2[1] != 0:
    L2_slope = L2[0] / L2[1]
else:
    L2_slope = 'inf'


message = ''

if L1_slope == L2_slope:
    if L1[0] != 0 and L2[0] != 0:
        multiplier = L1[0] / L2[0]
    elif L1[1] != 0 and L2[1] != 0:
        multiplier = L1[1] / L2[1]
    elif L1[2] != 0 and L2[2] != 0:
        multiplier = L1[2] / L2[2]
    else:
        message = 'many solution'

    if message == '':
        if ((L2[0] * multiplier) == L1[0]) and ((L2[1] * multiplier) == L1[1]):
            if L2[2] * multiplier == L1[2]:
                message = 'many solutions'
            else:
                message = 'no solution'
        else:
            message = 'one solution'
else:
    message = 'one solution'

print(message)
