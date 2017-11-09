def c(n, k):
    if 0 < k < n:
        return c(n - 1, k) + c(n - 1, k - 1)
    elif k == 0 or n == k:
        return 1
    else:
        return 0

n = int(input())
k = int(input())

print(c(n, k))
