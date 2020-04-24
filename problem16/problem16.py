
def sum_of_number_digits(n):
    res = 0
    for c in str(n):
        res += int(c)
    return res

print(sum_of_number_digits(2 ** 1000))