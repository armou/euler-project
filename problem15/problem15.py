
# Lattice paths
   
# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#                               Start
#                                    + - + - +
#                                    |   |   |
#                                    + - + - +
#                                    |   |   |
#                                    + - + - + End
# How many such routes are there through a 20×20 grid?



def find_all_paths(path, right, down, final):
    newPath = ""
    if right:
        newPath = path + "r"
        find_all_paths(newPath, right - 1, down, final)
    if down:
        newPath = path + "d"
        find_all_paths(newPath, right, down - 1, final)
    if not down and not right:
        final.append(path)
    return final

## Uncomment this if you want to print all possible paths (unfortunately this recursive function is too slow to handle a 20x20 grid):
# print(find_all_paths("", 3, 3, []))

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)

## Apparently there's formula that does the job. I didn't find it myself but from someone better at math than I am.
def total_paths(n):
    return factorial(n * 2) // factorial(n) ** 2

print(total_paths(20))