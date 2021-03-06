# Largest prime factor
   
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math


def is_prime(n):
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

def largest_prime_factor(n):
    i = int(math.sqrt(n))
    while i > 1:
        if n % i == 0 and is_prime(i):
            return i
        i -= 1
    return 1


print(largest_prime_factor(600851475143))