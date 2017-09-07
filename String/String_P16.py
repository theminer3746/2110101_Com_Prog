data = input().strip().replace(',', '').split('.')

base_callout = ['soon', 'nueng', 'song', 'sam', 'see', 'ha', 'hok', 'jed', 'pad', 'kao']
tenth_callout = ['sip', 'yee-sip', 'sam-sip', 'see-sip', 'ha-sip', 'hok-sip', 'jed-sip', 'pad-sip', 'kao-sip']
unit_callout = ['ed', 'song', 'sam', 'see', 'ha', 'hok', 'jed', 'pad', 'kao']

output = ''

if data[0][0] == '-':
    output += 'lop-'

fraction = ''
if len(data) == 2:
    fraction_part = data[1]
    fraction_callout = base_callout
    if len(data) == 2:
        fraction += 'jood-'
        for i in fraction_part:
            fraction += fraction_callout[int(i)] + '-'

    fraction = fraction[:-1] # To remove the last -


decimal = ''
if data[0] != '':
    decimal_part = data[0][::-1]

    if decimal_part.find('-') != -1:
        decimal_part = decimal_part.replace('-', '')
        negative = True
    else:
        negative = False

    for digit in range(len(decimal_part)):
        if digit == 0: # 1
            if decimal_part[0] != '0' or len(decimal_part) == 1:
                if len(decimal_part) == 1:
                    decimal += base_callout[int(decimal_part[digit])]
                else:
                    if decimal_part[1] != '0':
                        decimal += unit_callout[int(decimal_part[digit]) - 1]
                    else:
                        decimal += base_callout[int(decimal_part[digit])]
        elif digit == 1 and decimal_part[digit] != '0': # 10
            decimal = tenth_callout[int(decimal_part[digit]) - 1] + '-' + decimal
        elif digit == 2 and decimal_part[digit] != '0': # 100
            decimal = base_callout[int(decimal_part[digit])] + '-roey-' + decimal
        elif digit == 3 and decimal_part[digit] != '0': # 1000
            decimal = base_callout[int(decimal_part[digit])] + '-pun-' + decimal
        elif digit == 4 and decimal_part[digit] != '0': # 10000
            decimal = base_callout[int(decimal_part[digit])] + '-muen-' + decimal
        elif digit == 5 and decimal_part[digit] != '0': # 100000
            decimal = base_callout[int(decimal_part[digit])] + '-saen-' + decimal
        elif digit == 6: # 1000000
            if len(decimal_part) > 7:
                if decimal_part[7] != '0':
                    decimal = unit_callout[int(decimal_part[digit]) - 1] + '-larn-' + decimal
                else:
                    decimal = '-larn-' + decimal
            else:
                decimal = base_callout[int(decimal_part[digit])] + '-larn-' + decimal
        elif digit == 7 and decimal_part[digit] != '0': # 10000000
            decimal = tenth_callout[int(decimal_part[digit]) - 1] + '-' + decimal
        elif digit == 8 and decimal_part[digit] != '0': # 100000000
            decimal = base_callout[int(decimal_part[digit])] + '-roey-' + decimal
        elif digit == 9 and decimal_part[digit] != '0': # 1000000000
            decimal = base_callout[int(decimal_part[digit])] + '-pun-' + decimal

    if decimal[-1] == '-':
        decimal = decimal[:-1]

    decimal = decimal.replace('--', '-')

    if negative:
        decimal = 'lop-' + decimal

if decimal != '' and fraction != '':
    print(decimal + '-' + fraction)
else:
    print(decimal + fraction)
