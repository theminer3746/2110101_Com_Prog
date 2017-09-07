s = input().strip().split()

s[0] = s[0][0].upper() + s[0][1:len(s[0])].lower()

number_sum = 0
for i in s[1]:
    if i in '0123456789':
        number_sum += int(i)

print(s[0], number_sum)
