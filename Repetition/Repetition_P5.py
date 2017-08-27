counter = 0
total = 0

while True:
    value = float(input())

    if value == -1:
        break

    total += value
    counter += 1

if counter == 0:
    print('No Data')
else:
    print(total/counter)
