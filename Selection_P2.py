score = float(input())

if 0 <= score <= 100:
    if 80 <= score <= 100:
        message = 'A'
    elif 75 <= score < 80:
        message = 'B+'
    elif 70 <= score < 75:
        message = 'B'
    elif 65 <= score < 70:
        message = 'C+'
    elif 60 <= score < 65:
        message = 'C'
    elif 55 <= score < 60:
        message = 'D+'
    elif 50 <= score < 55:
        message = 'D'
    else:
        message = 'F'
else:
    message = 'ERROR'

print(message)
