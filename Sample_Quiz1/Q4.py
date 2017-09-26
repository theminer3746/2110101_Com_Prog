import math

number, target = [x for x in input().split()]

target = int(target)

output = 0

if int(number[-target]) > 5:
    output = math.ceil(int(number) / (10 ** target)) * (10 ** target)
elif int(number[-target]) < 5:
    output = math.floor(int(number) / (10 ** target)) * (10 ** target)
else:
    if int(number[-target-1]) % 2 == 0:
        output = math.floor(int(number) / (10 ** target)) * (10 ** target)
    else:
        output = math.ceil(int(number) / (10 ** target)) * (10 ** target)

print(output)
