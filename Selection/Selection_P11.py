from math import sqrt

input = [float(i) for i in input().split()]

c1 = [input[a] for a in range(0, 3)]
c2 = [input[b] for b in range(3, 6)]

distance_between_central = sqrt(pow((c1[0] - c2[0]), 2) + pow((c1[1] - c2[1]), 2))
combine_radius_length = c1[2] + c2[2]

if abs(distance_between_central - combine_radius_length) < (combine_radius_length * (10 ** -5)):
    print(1)
else:
    if combine_radius_length > distance_between_central:
        print(2)
    else:
        print(3)
