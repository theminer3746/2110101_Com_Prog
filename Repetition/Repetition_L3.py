base10, target_base = [int(j) for j in input().split()]

result = ''

if target_base > 9 or target_base < 2 or base10 < 0:
    result = 'Error: Cannot convert'
else:
    while True:
        mod_result = base10 % target_base
        if mod_result < target_base:
            result = str(mod_result) + result
        else:
            result = '0' + result
        base10 //= target_base

        if base10 == 0:
            break

print(result)
