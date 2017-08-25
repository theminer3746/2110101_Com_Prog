while True:
    value = int(input())

    if value < 0:
        break

    if value > 100:
        print('Error')
    elif 80 <= value <= 100:
        print('A')
    elif 75 <= value <= 79:
        print('B+')
    elif 70 <= value <= 74:
        print('B')
    elif 65 <= value <= 69:
        print('C+')
    elif 60 <= value <= 64:
        print('C')
    elif 55 <= value <= 59:
        print('D+')
    elif 50 <= value <= 54:
        print('D')
    else:
        print('F')
