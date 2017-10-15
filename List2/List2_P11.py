row, column = [int(x) for x in input().split()]

students = []

for row in range(row):
    students.append(input().strip().split())

results = []

for student in students:
    total_credit = 0
    total_score = 0

    for grade in student:
        if grade != 'X':
            total_credit += 1

            if grade == 'A':
                total_score += 4
            elif grade == 'B+':
                total_score += 3.5
            elif grade == 'B':
                total_score += 3
            elif grade == 'C+':
                total_score += 2.5
            elif grade == 'C':
                total_score += 2
            elif grade == 'D+':
                total_score += 1.5
            elif grade == 'D':
                total_score += 1
            else:
                total_score += 0

    results.append(total_score / total_credit)

for result in results:
    print("{:.2f}".format(result))
