# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial_digit_sum(num):
    fac = 1
    while num > 0:
        fac *= num
        num -= 1
    ret = 0
    for c in str(fac):
        ret += int(c)
    return ret

print(factorial_digit_sum(100))