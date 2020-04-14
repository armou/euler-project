# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def get_triplet(a, b, n):
    c = b * b - a * a
    d = 2 * (a * b)
    e = int(math.sqrt(c * c + d * d))
    if (c + d + e) < n:
        return get_triplet(a, b + 1, n)
    return [c, d, e]

def find_triplet(n):
    a = 2
    b = a + 1
    triplet = get_triplet(a, b, n)
    while triplet[0] + triplet[1] + triplet[2] != n:
        a += 1
        b = 2
        triplet = get_triplet(a, b, n)
    return triplet[0] * triplet[1] * triplet[2]


print(find_triplet(1000))