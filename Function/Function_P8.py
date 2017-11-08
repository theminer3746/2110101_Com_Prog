def isSet(c1,c2,c3):
    for key in range(4):
        unique_length = len({c1[key], c2[key], c3[key]})
        if unique_length == 2:
            return False
    else:
        return True

cards = []
for i in range(12):
    cards.append(input().strip().split())

for i in range(12):
    for j in range(i+1,12):
        for k in range(j+1,12):
            if isSet(cards[i],cards[j],cards[k]):
                print(i,j,k)
