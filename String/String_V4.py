original = input().strip() + ' '

number_in_word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

final_text = ''

for i in range(len(original)):
    if original[i] in '0123456789':
        if original[i+1].lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
            final_text += number_in_word[int(original[i])] + ' '
        else:
            final_text += number_in_word[int(original[i])]
    else:
        final_text += original[i]

print(final_text)
