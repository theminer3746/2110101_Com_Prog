value = int(input())

divider = list()

for i in range(2, value):
    if value % i == 0:
        divider.append(i)

if not divider:
    print('Prime Number')
else:
    divider.reverse()
    print(*divider)
