# The sum of the squares of the first ten natural numbers is,

# 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)^2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def square_of_sum(n):
    res = 0
    for i in range(n+1):
        res+=i
    return res * res

def sum_of_square(n):
    res = 0
    for i in range(n+1):
        res += i * i
    return res

print(square_of_sum(100) - sum_of_square(100))