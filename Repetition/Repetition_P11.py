def isPrime(candidate_value, prime_list):
    for i in range(0, len(prime_list)):
        if candidate_value % prime_list[i] == 0:
            return False

    return True

value = int(input())

if value < 0:
    print('input unavailable')
elif value == 0 or value == 1:
    print('none')
else:
    prime = list()
    for candidate in range(2, value + 1):
        if isPrime(candidate, prime):
            prime.append(candidate)

    print(*prime)
