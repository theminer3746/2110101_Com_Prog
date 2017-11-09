def f(d, c, s, b, m):
    if s == len(d) - 1:
        return m + 1
    elif b and d[s + 1] >= d[s]:
        return f(d, c + 1, s + 1, True, max(c + 1, m))
    elif b and d[s + 1] < d[s]:
        return f(d, 1, s + 1, False, m)
    elif not b and d[s + 1] >= d[s]:
        return f(d, 1, s + 1, True, m)
    else:
        return f(d, 0, s + 1, False, m)

d = [int(e) for e in input().split()]
print(f(d,0,0,False,0))
