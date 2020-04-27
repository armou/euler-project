# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

zero_to_twenty = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty"
)

decimals = (
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
)

def count_letters_in_n(n):
    res = 0

    for i in range(n + 1):
        tmp = i
        if tmp >= 1000:
            if tmp == 1000:
                res += len("one")
                res += len("thousand")
            else:
                ## Not implemented for numbers > 1000
                pass
            tmp -= (tmp // 1000) * 1000
        if tmp >= 100:
            if tmp == 100:
                res += len("one")
                res += len("hundred")
            else:
                res += len(zero_to_twenty[tmp//100])
                res += len("hundred")
            tmp -= (tmp // 100) * 100
            if tmp > 0:
                res += len("and")
        if tmp >= len(zero_to_twenty):
            res += len(decimals[tmp//10 - 2])
            tmp -= (tmp // 10) * 10
        if tmp < len(zero_to_twenty) and tmp != 0:
            res += len(zero_to_twenty[tmp])
    return res

print(count_letters_in_n(1000))

