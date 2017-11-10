def list2dict(x):
    d = dict()

    for item in x:
        if item[1][1] not in d.keys():
            d[item[1][1]] = []

        d[item[1][1]].append((item[0], item[1][0]))

    return d

def dict2list(d) :
    x = list()
    for province in d:
        for data in d[province]:
            x.append([data[0], (data[1], province)])
    return x

def get_empty(d) :
    ans = set()

    for key in d:
        if len(d[key]) == 0:
            ans.add(key)

    return ans

def compress_string(s) :
    compressed = [()]
    previous = ''
    for char in s:
        if compressed[-1] == ():
            compressed[-1] = (char, 1)
            previous = char
        else:
            if char == previous:
                compressed[-1] = (char, compressed[-1][1] + 1)
            else:
                compressed.append((char, 1))
                previous = char

    if s == '':
        compressed = []

    return tuple(compressed)

def a(n) :
    if n == 0:
        return 3
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * a(n - 1) + a(n - 2) + 3
    else:
        return 3 * a(n - 1) - 2 * a(n - 2) - n

exec(input().strip())
exec(input().strip())
