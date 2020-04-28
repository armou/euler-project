

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

#                75
#               95 64
#              17 47 82
#             18 35 87 10
#            20 04 82 47 65
#           19 01 23 75 03 34
#          88 02 77 73 07 63 67
#         99 65 04 28 06 16 70 92
#        41 41 26 56 83 40 80 70 33
#       41 48 72 33 47 32 37 16 94 29
#      53 71 44 65 25 43 91 52 97 51 14
#     70 11 33 28 77 73 17 78 39 68 17 57
#    91 71 52 38 17 14 91 43 58 50 27 29 48
#   63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

grid = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def create_grid(grid):
    tmp = grid.split("\n")
    g = []
    for i in range(len(tmp)):
        g.append([])
        g[i] = tmp[i].split(" ")
        for j in range(len(g[i])):
            g[i][j] = int(g[i][j])
    return g

g = create_grid(grid)
# print(g[-2])

def graph_path(g):
    graph = []
    step = 0
    for j in range(-2, -(len(g) + 1), -1):
        print(j)
        for i in range(len(g[j])):
            graph.append([])
            # print(i)
            if g[j][i] + g[j+1][i] > g[j][i] + g[j+1][i + 1]:
                # print(sum(x[j][i], x[j+1][i]))
                # graph[step].append([x[j][i], x[j+1][i]])
                graph[step].append([i, g[j][i] + g[j+1][i]])
            else:
                graph[step].append([i, g[j][i] + g[j+1][i + 1]])
            # r = 0
            # for x in range(len(graph)):
            #     print(graph[x][r])
                # r += 1
            step += 1
        break
    print(sum(graph[0]))

graph_path(g)