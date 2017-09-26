from math import ceil

distance = float(input())


if distance < 0:
    print('ERROR')
else:
    price = 0

    for current_distance in range(1, ceil(distance) + 1):
        if current_distance == 1:
            price += 35.00
        elif 10 >= current_distance > 1:
            price += 5.50
        elif 20 >= current_distance > 10:
            price += 6.50
        elif 40 >= current_distance > 20:
            price += 7.50
        elif 60 >= current_distance > 40:
            price += 8.00
        elif 80 >= current_distance > 60:
            price += 9.00
        elif current_distance > 80:
            price += 10.50

    print(price)
