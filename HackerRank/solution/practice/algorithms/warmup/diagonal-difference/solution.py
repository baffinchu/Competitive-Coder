# {'time': 'O(n)', 'space': 'O(n^2)'}
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
# <- potentially faster without using array


def diagonalDifference(arr):
    n = len(arr[0])
    leftDiagonal = 0
    rightDiagonal = 0

    for row in range(n):
        leftDiagonal += arr[row][row]
        rightDiagonal += arr[row][n - row - 1]
    return abs(leftDiagonal - rightDiagonal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
