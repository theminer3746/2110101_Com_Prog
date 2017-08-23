input = input()

array = list()
for i in range(0, 12):
    array.append(int(input[i]))

a = (13*array[0]+12*array[1]+11*array[2]+10*array[3]+9*array[4]+8*array[5]+7*array[6]+6*array[7]+5*array[8]+4*array[9]+3*array[10]+2*array[11])

n13 = (11 - (a % 11)) % 10

print(str(n13))
