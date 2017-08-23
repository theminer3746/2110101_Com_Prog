number = int(input())

message = ''

if number > 0:
    message += 'positive'
elif number < 0:
    message += 'negative'
else:
    message += 'zero'

message += ' '

if number % 2 == 0:
    message += 'even'
else:
    message += 'odd'

print(message)
