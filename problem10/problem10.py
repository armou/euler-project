
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True

def sum_prime(range):
    i = 5
    res = 5 # let's already add 2 + 3 and iterate on odd number only
    while (i < range):
        if is_prime(i):
            res += i
        i += 2
    return res

print(sum_prime(2000000))