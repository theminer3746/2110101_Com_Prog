data = input().strip()
start, stop = [int(x) for x in input().strip().split()]

output = data[0:start] + data[start:stop+1][::-1] + data[stop+1:len(data)]

print(output)
