def tiling(x, c):
    if x == 1:
        return 1
    else:
        if c == 'G':
            return tiling(x - 1, 'R') + tiling(x - 1, 'B')
        else:
            return tiling(x - 1, 'R') + tiling(x - 1, 'B') + tiling(x - 1, 'G')

N = int(input())
print(tiling(N,'G')+tiling(N,'R')+tiling(N,'B'))
