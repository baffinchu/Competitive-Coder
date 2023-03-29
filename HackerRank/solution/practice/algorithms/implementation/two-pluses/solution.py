# {'time': 'O(n)', 'space': 'O(n)'}
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.


def twoPluses(grid):

    # grid = eng2math(grid)

    first = chopping(grid)

    return first


def math2eng(grid):

    m = len(grid)
    n = len(grid[0])

    newgrid = []

    for i in range(m):
        wow = ''
        for j in range(n):

            if grid[i][j] > 0:
                wow += 'G'
            else:
                wow += 'B'
        newgrid += [wow]

    return newgrid


def chopping(grid):

    m = len(grid)
    n = len(grid[0]) - (grid[0][-1] == '\r')

    first = eng2math(grid)
    abc = eng2math(grid)

    # second = math2eng(first)

    ha = first[2][4]

    # wow = []

    maxlist = []

    for i in range(m):
        lst = []

        for j in range(n):

            wow = []
            second = eng2math(grid)
            well = second[i][j]
            if well == 0:
                lst += [0]
            else:
                well = int((well - 1) / 4 + 1)
                for k in range(well):
                    second[i-k][j] = 0
                    second[i+k][j] = 0
                    second[i][j-k] = 0
                    second[i][j+k] = 0

                    third = math2eng(second)

                    fourth = eng2math(third)

                    print(i, j, k, fourth)

                    wow += [(k * 4 + 1) * max([max(i) for i in zip(*fourth)])]

                lst += [max(wow)]
        maxlist += [lst]

    # first = math2eng(first)

    return max([max(i) for i in zip(*maxlist)])
    # return maxlist


def eng2math(grid):

    m = len(grid)
    n = len(grid[0])

    start = min(m, n)
    start -= (start % 2 == 0)
    k = int((start - 1) / 2)

    cand = []

    for i in range(m):
        newcand = []
        newi = min(i, m - i - 1) + 1
        for j in range(n):
            newj = min(j, n - j - 1) + 1
            new = min(newi, newj)
            if grid[i][j] == 'B':
                newcand += [0]
            elif grid[i][j] == 'G':

                wow = 1
                for l in range(1, new):

                    if ((grid[i - l][j] == 'G') and (grid[i + l][j] == 'G') and (grid[i][j - l] == 'G') and (grid[i][j + l] == 'G')):
                        wow += 4
                    else:
                        break

                newcand += [wow]

        cand += [newcand]

    return cand


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
