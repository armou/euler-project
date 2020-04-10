
import time
start_time = time.time()

def is_evenly_divisible(n, r):
    if not n % r:
        if r == 2:
            return True
        return(is_evenly_divisible(n, r - 1)) #To reduce execution time, recursion loop from highest to lowest factor
    return False


def smallest_evenly_divisible_in_range(r):
    for t in range (r * r, 100000000000, r):
        if (is_evenly_divisible(t, r - 1)):
            return t
    return 0


print(smallest_evenly_divisible_in_range(20))
#Uncomment next line to check execution time
# print("--- %s seconds ---" % (time.time() - start_time))
