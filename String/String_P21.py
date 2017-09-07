needle = input().strip()
haystack = input().strip()

if haystack.find(needle) != -1:
    print('SUBSTRING')
elif len(haystack) >= len(needle):
    found_position = 0
    is_sub_sequence = True
    for alphabet in needle:
        found_position = haystack.find(alphabet, found_position)
        if found_position == -1:
            is_sub_sequence = False
            break

    if is_sub_sequence:
        print('SUBSEQUENCE')
    else:
        print('NONE')

else:
    print('NONE')
