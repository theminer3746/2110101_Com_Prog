data = input().strip().lower().replace(' ', '')

if data == data[::-1]:
    print('yes')
else:
    print('no')
