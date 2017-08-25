from math import ceil

package_type = input().strip()
weight = int(input())

if weight < 0:
    message = 'ERROR'
else:
    if package_type == 'N':
        if weight <= 1000:
            message = 20
        elif weight <= 2000:
            message = 35
        elif weight <= 3000:
            message = 50
        elif weight <= 4000:
            message = 65
        elif weight <= 5000:
            message = 80
        elif weight <= 6000:
            message = 95
        elif weight <= 7000:
            message = 110
        elif weight <= 8000:
            message = 125
        elif weight <= 9000:
            message = 140
        elif weight <= 10000:
            message = 155
        elif weight <= 11000:
            message = 170
        else:
            message = 170 + ceil((weight - 11000) / 1000) * 15
    elif package_type == 'E':
        if weight <= 20:
            message = 32
        elif weight <= 100:
            message = 37
        elif weight <= 250:
            message = 42
        elif weight <= 500:
            message = 52
        elif weight <= 1000:
            message = 67
        elif weight <= 1500:
            message = 82
        elif weight <= 2000:
            message = 97
        elif weight <= 2500:
            message = 122
        elif weight <= 3000:
            message = 137
        elif weight <= 3500:
            message = 157
        elif weight <= 4000:
            message = 177
        elif weight <= 4500:
            message = 197
        elif weight <= 5000:
            message = 217
        elif weight <= 5500:
            message = 242
        elif weight <= 6000:
            message = 267
        elif weight <= 6500:
            message = 292
        elif weight <= 7000:
            message = 317
        elif weight <= 7500:
            message = 342
        elif weight <= 8000:
            message = 367
        elif weight <= 8500:
            message = 397
        elif weight <= 9000:
            message = 427
        elif weight <= 9500:
            message = 457
        elif weight <= 10000:
            message = 487
        else:
            message = 'ERROR'
    elif package_type == 'R':
        if weight <= 100:
            message = 18
        elif weight <= 250:
            message = 22
        elif weight <= 500:
            message = 28
        elif weight <= 1000:
            message = 38
        elif weight <= 2000:
            message = 58
        else:
            message = 'ERROR'
    else:
        message = 'ERROR'

print(message)
