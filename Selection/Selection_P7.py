income = int(input())

total_tax = 0

if income != 0:
    if income >= 4000001:
        income_in_range = income - 4000000
        total_tax += income_in_range * 37 / 100
        income = income - income_in_range

    if income >= 1000001:
        income_in_range = income - 1000000
        total_tax += income_in_range * 30 / 100
        income = income - income_in_range

    if income >= 500001:
        income_in_range = income - 500000
        total_tax += income_in_range * 20 / 100
        income = income - income_in_range

    if income >= 100001:
        income_in_range = income - 100000
        total_tax += income_in_range * 10 / 100
        income = income - income_in_range

    if income >= 1:
        income_in_range = income
        total_tax += income_in_range * 5 / 100

print(total_tax)
