filename = input().strip()

file = open(filename, 'r')

output = []

for line in file:
    data = line.strip().split(';')

    score = float(data[3]) + float(data[4])

    if score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 60:
        grade = 'C'
    elif score >= 50:
        grade = 'D'
    else:
        grade = 'F'

    output.append([data[0], data[1] + ' ' + data[2], grade])

print(output)
