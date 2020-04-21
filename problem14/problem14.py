
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def try_sequence(start):
    count = 1
    while start > 1:
        if start % 2:
            start = 3 * start + 1
        else:
            start //= 2
        count += 1
    return count

def collatz_sequence(r):
    start = r if r % 2 else r - 1
    highest = 0
    count = 0
    while start > r // 2:
        if try_sequence(start) > count:
            count = try_sequence(start)
            highest = start
        start -= 2
    return highest

print(collatz_sequence(1000000))