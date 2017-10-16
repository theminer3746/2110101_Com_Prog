data = [int(x) for x in input().strip().split()]

player1 = 0
player2 = 0

for i in range(len(data)):
    if data[0] > data[-1]:
        if i % 2 == 0:
            player1 += data[0]
        else:
            player2 += data[0]

        data.pop(0)
    else:
        if i % 2 == 0:
            player1 += data[-1]
        else:
            player2 += data[-1]

        data.pop(-1)

print(player1)
print(player2)

if player1 > player2:
    print(1)
elif player1 == player2:
    print(0)
else:
    print(2)
