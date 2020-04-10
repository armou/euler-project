
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


import time
start_time = time.time()

#Check if a number is a palindrome (can be read the same way backwards)
#Return a Boolean
def is_palindrome(n):
    return str(n) == str(n)[::-1]

#Loop through all 3 digits integers to find highest palindrome product between those 2 integers
#Return a number
def highest_palindrome_product():
    res = 0
    for x in range(100, 1000):
        for y in range(x, 1000):
            if is_palindrome(x * y) and x * y > res:
                res = x * y
    return res

print(highest_palindrome_product())

# Uncomment following line to check execution time of function
# print("--- %s seconds ---" % (time.time() - start_time))
