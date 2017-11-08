def roman_to_int(string):
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],
            ['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint=0
    for pair in table:
        check=True
        while check:
            if len(string)>=len(pair[0]):
                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]
                else: check=False
            else: check=False
    return returnint

number = []

amount = int(input())
for i in range(amount):
    current = input()
    number.append((current, roman_to_int(current)))

number.sort(key=lambda number:number[1])

for item in number:
    print(item[0])
