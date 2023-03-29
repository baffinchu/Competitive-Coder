# {'time': 'O(1)', 'space': 'O(1)'}
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.


def compareTriplets(a, b):

    aliceScore = 0
    bobScore = 0

    for round in range(3):
        aliceScore += (a[round] > b[round])
        bobScore += (b[round] > a[round])

    return [aliceScore, bobScore]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
