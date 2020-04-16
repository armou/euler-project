# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time
start_time = time.time()

def is_evenly_divisible(n, r):
    if not n % r:
        if r == 2:
            return True
        return(is_evenly_divisible(n, r - 1)) #To reduce execution time, recursive loop from highest to lowest factor
    return False


def smallest_evenly_divisible_in_range(r):
    for t in range (r * r, 100000000000, r):
        if (is_evenly_divisible(t, r - 1)):
            return t
    return 0


print(smallest_evenly_divisible_in_range(20))
#Uncomment next line to check execution time
# print("--- %s seconds ---" % (time.time() - start_time))
