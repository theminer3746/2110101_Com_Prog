def isPrime(candidate_value, prime_list):
    for i in range(0, len(prime_list)):
        if candidate_value % prime_list[i] == 0:
            return False

    return True

value = int(input())

prime_divider = list()

for i in range(2, value+1):
    if value % i == 0:
        if isPrime(i, prime_divider):
            prime_divider.append(i)

print(*prime_divider)
