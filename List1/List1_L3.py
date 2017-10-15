data = [int(x) for x in input().split()]

odd = []
even = []
for i in range(len(data) - 1):
    diff = data[i + 1] - data[i]

    if i % 2 == 0:
        odd.append(diff)
    else:
        even.append(diff)

if len(odd) > len(even):
    next_is_even = True
else:
    next_is_even = False

if len(odd + even) >= 4:
    odd_diff1 = odd[1] - odd[0]
    even_diff1 = even[1] - even[0]

    if len(odd) >= 3:
        odd_diff2 = odd[2] - odd[1]

        if odd_diff2 != odd_diff1:
            odd_diff_diff = odd_diff2 - odd_diff1
        else:
            odd_diff_diff = 0
    else:
        odd_diff_diff = 0

    if len(even) >= 3:
        even_diff2 = even[2] - even[1]

        if even_diff2 != even_diff1:
            even_diff_diff = even_diff2 - even_diff1
        else:
            even_diff_diff = 0
    else:
        even_diff_diff = 0

    if next_is_even:
        print(data[-1] + even[-1] + even[-1] - even[-2] + even_diff_diff)
    else:
        print(data[-1] + odd[-1] + odd[-1] - odd[-2] + odd_diff_diff)
else:
    if odd[0] == even[0]:
        print(data[-1] + odd[0])
    else:
        if next_is_even:
            print(data[-1] + even[0] + odd[1] - odd[0])
        else:
            print(data[-1] + even[1] + odd[0] - even[0])
