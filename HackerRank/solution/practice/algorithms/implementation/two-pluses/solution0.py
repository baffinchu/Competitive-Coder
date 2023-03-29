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
    n = len(grid[0])

    first = eng2math(grid)
    abc = eng2math(grid)

    second = math2eng(first)

    ha = first[2][4]

    # wow = []

    for i in [2]:  # range(m):
        for j in [4]:  # range(n):
            well = first[i][j]
            wow = []
            for k in range(ha):
                first[i-k][j] = 0
                first[i+k][j] = 0
                first[i][j-k] = 0
                first[i][j+k] = 0

                third = math2eng(first)

                fourth = eng2math(third)

                wow += [k + 1, sum([sum(i) for i in zip(*fourth)]), fourth]

    # first = math2eng(first)

    return wow


def eng2math(grid):

    m = len(grid)
    n = len(grid[0])

    start = min(m, n)
    start -= (start % 2 == 0)
    k = int((start - 1) / 2)

    cand = []
    pos = ()
    max1 = 0

    for i in range(m):
        newcand = []
        newi = min(i, m - i - 1) + 1
        for j in range(n):
            newj = min(j, n - j - 1) + 1
            new = min(newi, newj)
            if grid[i][j] == 'B':
                newcand += [0]
            else:

                wow = 1
                for l in range(1, new):

                    if ((grid[i - l][j] == 'G') and (grid[i + l][j] == 'G') and (grid[i][j - l] == 'G') and (grid[i][j + l] == 'G')):
                        wow += 1
                    else:
                        break

                newcand += [wow]

        cand += [newcand]

        if max(newcand) > max1:
            max1 = max(newcand)
            pos = (i, newcand.index(max1))

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
