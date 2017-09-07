date = input().strip().split('/')

month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

print(date[1], month[int(date[0]) - 1], date[2])
