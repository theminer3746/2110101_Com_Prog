data = input().strip().split('-')

base_callout = ['soon', 'nueng', 'song', 'sam', 'see', 'ha', 'hok', 'jed', 'pad', 'kao']
tenth_callout = ['sip', 'yee', 'sam', 'see', 'ha', 'hok', 'jed', 'pad', 'kao']
unit_callout = ['ed', 'song', 'sam', 'see', 'ha', 'hok', 'jed', 'pad', 'kao']

if data.count('jood') == 1:
    decimal_reading = data[:data.index('jood')]
    fraction_reading = data[data.index('jood') + 1:]
else:
    decimal_reading = data.copy()
    fraction_reading = []

negative = False
if len(decimal_reading) >= 1:
    if decimal_reading[0] == 'lop':
        negative = True
        decimal_reading = decimal_reading[1:]

decimal = ''
decimal_int = 0
if decimal_reading != list():
    if decimal_reading.count('larn') != 0:
        larn_position = decimal_reading.index('larn')
        million = decimal_reading[:larn_position]
        less_than_million = decimal_reading[larn_position + 1:]

        for i in range(len(million)):
            if million[i] == 'pun':
                decimal_int += int(base_callout.index(million[i - 1])) * 1e9
            elif million[i] == 'roey':
                decimal_int += int(base_callout.index(million[i - 1])) * 1e8
            elif million[i] == 'sip':
                if million[i - 1] in tenth_callout:
                    decimal_int += int(tenth_callout.index(million[i - 1]) + 1) * 1e7
                else:
                    decimal_int += 1e7
            elif (million[i] in base_callout or million[i] in unit_callout) and i == len(million) - 1:
                if million[i - 1] == 'sip':
                    decimal_int += int(unit_callout.index(million[i]) + 1) * 1e6
                else:
                    decimal_int += int(base_callout.index(million[i])) * 1e6
    else:
        less_than_million = decimal_reading

    for j in range(len(less_than_million)):
        if less_than_million[j] == 'saen':
            decimal_int += int(base_callout.index(less_than_million[j - 1])) * 1e5
        elif less_than_million[j] == 'muen':
            decimal_int += int(base_callout.index(less_than_million[j - 1])) * 1e4
        elif less_than_million[j] == 'pun':
            decimal_int += int(base_callout.index(less_than_million[j - 1])) * 1e3
        elif less_than_million[j] == 'roey':
            decimal_int += int(base_callout.index(less_than_million[j - 1])) * 1e2
        elif less_than_million[j] == 'sip':
            if less_than_million[j - 1] in tenth_callout:
                decimal_int += int(tenth_callout.index(less_than_million[j - 1]) + 1) * 1e1
            else:
                decimal_int += 1e1
        elif (less_than_million[j] in base_callout or less_than_million[j] in unit_callout) and j == len(less_than_million) - 1:
            if less_than_million[j - 1] == 'sip':
                decimal_int += int(unit_callout.index(less_than_million[j]) + 1)
            else:
                decimal_int += int(base_callout.index(less_than_million[j]))
else:
    decimal = '0'

formatted_decimal = ''
decimal_int = int(decimal_int)
for x in range(1, len(str(decimal_int)) + 1):
    if x % 3 == 0:
        formatted_decimal = ',' + str(decimal_int)[-x] + formatted_decimal
    else:
        formatted_decimal = str(decimal_int)[-x] + formatted_decimal

if formatted_decimal[0] == ',':
    formatted_decimal = formatted_decimal[1:]

if negative:
    formatted_decimal = '-' + formatted_decimal

formatted_fraction = ''
if len(fraction_reading) >= 1:
    for k in range(len(fraction_reading)):
        formatted_fraction += str(base_callout.index(fraction_reading[k]))

if formatted_fraction != '' and formatted_decimal != '':
    print(formatted_decimal + '.' + formatted_fraction)
else:
    print(formatted_decimal + formatted_fraction)
