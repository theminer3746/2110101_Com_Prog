bit = input().strip()

count = 0

for x in bit:
    count += int(x)

if count % 2 == 0:
    print(bit + '0')
else:
    print(bit + '1')
