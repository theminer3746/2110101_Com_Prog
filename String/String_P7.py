data = input().strip()

digits = '0123456789'

for i in data:
    if i in digits:
        digits = digits.replace(i, '')

if digits == '':
    print('No missing digits')
else:
    print(*digits)
