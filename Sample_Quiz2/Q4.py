data = input().strip()

longest_palindrome = ''

for start in range(0, len(data)):
    for length in range(1, len(data) - start + 1):
        current = data[start:start + length]

        if current[::-1] in data and (data.find(current) == data.find(current[::-1])):
            if len(longest_palindrome) < len(current):
                longest_palindrome = current
            elif len(longest_palindrome) == len(current):
                array = [longest_palindrome, current]
                array.sort()
                longest_palindrome = array[0]

print(longest_palindrome)
