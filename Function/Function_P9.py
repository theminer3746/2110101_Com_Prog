def isSevenUp(x):
    return (x % 7 == 0) or '7' in str(x)

def nextSevenUp(x):
    y = x + 1
    found = [False, False]
    while True:
        if found[0] and found[1]:
            break

        if '7' in str(y) and not found[0]:
            contain_7 = y
            found[0] = True

        if y % 7 == 0 and not found[1]:
            can_be_divide_by_7 = y
            found[1] = True

        y += 1

    if contain_7 < can_be_divide_by_7:
        return contain_7
    else:
        return can_be_divide_by_7

def prevSevenUp(x):
    y = x - 1
    found = [False, False]
    while True:
        if found[0] and found[1]:
            break

        if '7' in str(y) and not found[0]:
            contain_7 = y
            #print('con now', contain_7)
            found[0] = True

        if y % 7 == 0 and not found[1]:
            can_be_divide_by_7 = y
            found[1] = True

        y -= 1

    if contain_7 > can_be_divide_by_7:
        return contain_7
    else:
        return can_be_divide_by_7

f,x = input().strip().split()
x = int(x)
if f == 'isSevenUp': print(isSevenUp(x))
elif f == 'nextSevenUp': print(nextSevenUp(x))
elif f == 'prevSevenUp': print(prevSevenUp(x))
