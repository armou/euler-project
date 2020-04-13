# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def next_prime(n):
    if n < 2:
        return 2
    while not is_prime(n):
        n += 1
    return n

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True

def prime_index(index):
    i = 0
    j = 0
    for j in range(0, index):
        while not is_prime(i):
            i += 1
        else:
            i += 1
            j += 1 
    return i - 1

print(prime_index(10001))