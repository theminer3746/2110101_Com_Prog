year = int(input()) - 543

if year % 400 == 0:
    print(29)
elif year % 100 == 0:
    print(28)
elif year % 4 == 0:
    print(29)
else:
    print(28)
