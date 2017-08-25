amount_of_line = int(input())

sum = 0
for j in range(amount_of_line):
    sum += float(input())

if amount_of_line == 0:
    print('No Data')
else:
    print(sum/amount_of_line)
