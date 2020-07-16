# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

def get_single_name_score(name):
    name_sum = 0
    for char in name:
        name_sum += ord(char) - 64
    return name_sum


def sum_names_score():
    f = open('names.txt', 'r')
    names = f.read().replace('\"', '').split(',')

    total = 0
    position = 0
    names.sort()
    for name in names:
        position += 1
        total += position * get_single_name_score(name)
    return total
            
print(sum_names_score())
