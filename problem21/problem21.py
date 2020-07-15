# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def sum_of_divisors(num):
    ret = 0
    for n in range(1, num//2 + 1):
        if num % n == 0:
            ret += n
    return ret

def amicable_numbers(r):
    amicable_sum = 0
    for n in range(1, r):
        if (sum_of_divisors(sum_of_divisors(n)) == n and sum_of_divisors(n) != n):
            amicable_sum += n
    return amicable_sum

print(amicable_numbers(10000))