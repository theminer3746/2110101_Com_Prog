length = [int(x) for x in input().split()]

if max(length) < (length[0] + length[1] + length[2] - max(length)):
    print('YES')
else:
    print('NO')
