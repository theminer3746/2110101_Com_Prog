target_line = int(input()) - 1

card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K']

file = open('cards.txt', 'r')

current_line = 0
result = False
while True:
    line = file.readline().strip()

    if current_line == target_line:
        previous_index = card.index(line[0])
        for c in line[1:]:
            if card.index(c) < previous_index:
                result = True
                break
            else:
                previous_index = card.index(c)
        break

    current_line += 1

if result:
    print('N')
else:
    print('Y')
